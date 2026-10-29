"""Comprueba únicamente los CSV ficticios adjuntos; no valida ni emite CFDI."""
import csv
from datetime import date, datetime
from decimal import Decimal as D
from pathlib import Path

BASE = Path(__file__).resolve().parent


def leer(nombre):
    with (BASE / f'{nombre}.csv').open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def igual(actual, esperado, contexto):
    if actual != esperado:
        raise AssertionError(f'{contexto}: obtenido {actual}, esperado {esperado}')


def limite(fecha):
    return date(fecha.year + (fecha.month == 12), fecha.month % 12 + 1, 5)


op, ret, ev, cob, caja, fac = map(leer, (
    'operacion', 'retornos', 'evidencias', 'cobros', 'caja', 'facturas'))
for tabla, clave in ((op, 'documento'), (ret, 'id'), (ev, 'documento'),
                     (cob, 'id'), (caja, 'ruta'), (fac, 'documento')):
    igual(len({r[clave] for r in tabla}), len(tabla), f'unicidad {clave}')
ids = {r['documento'] for r in op}
for tabla in (ret, ev, cob, fac):
    if not {r['documento'] for r in tabla} <= ids:
        raise AssertionError('Referencia sin documento')

for salida in leer('salida-rutas'):
    ruta = salida['ruta']
    lineas = [r for r in op if r['ruta'] == ruta]
    retornos = [r for r in ret if r['ruta'] == ruta]
    pagos = [r for r in cob if r['ruta'] == ruta]
    efectivo = sum(D(r['confirmado']) for r in pagos if r['medio'] == 'efectivo')
    banco_d = sum(D(r['declarado']) for r in pagos if r['medio'] == 'transferencia')
    banco_c = sum(D(r['confirmado']) for r in pagos if r['medio'] == 'transferencia')
    c = next(r for r in caja if r['ruta'] == ruta)
    esperado = D(c['fondo']) + efectivo - D(c['gastos_autorizados']) - D(c['retiros_acreditados'])
    carga = sum(D(r['carga']) for r in lineas)
    entregado = sum(D(r['entregado']) for r in lineas)
    recibido = sum(D(r['recibido']) for r in retornos)
    valores = dict(carga=carga, entregado=entregado,
                   retorno_declarado=sum(D(r['declarado']) for r in retornos),
                   retorno_recibido=recibido, diferencia_fisica=carga-entregado-recibido,
                   valor_entregado=sum(D(r['entregado'])*D(r['precio_final']) for r in lineas),
                   efectivo_esperado=esperado, efectivo_contado=D(c['contado']),
                   diferencia_caja=esperado-D(c['contado']), transferencia_declarada=banco_d,
                   transferencia_confirmada=banco_c, diferencia_transferencia=banco_d-banco_c,
                   credito_autorizado=sum(D(f['credito_autorizado']) for f in fac
                                          if f['documento'] in {r['documento'] for r in lineas}))
    for campo, valor in valores.items():
        igual(valor, D(salida[campo]), f'{ruta} {campo}')

corte = date(2026, 10, 29)
for salida in leer('salida-documentos'):
    doc = salida['documento']
    f = next(r for r in fac if r['documento'] == doc)
    pagos = [r for r in cob if r['documento'] == doc]
    # Enlace documento->pago no confirma aplicacion: solo declarado = confirmado reduce el saldo.
    aplicada = sum(D(r['confirmado']) for r in pagos if D(r['declarado']) == D(r['confirmado']))
    pendiente = [r for r in pagos if D(r['declarado']) != D(r['confirmado'])]
    saldo = 'DESCONOCIDO' if pendiente else D(f['saldo_anterior']) - aplicada
    igual(str(saldo), salida['saldo_tras_pago_confirmado'], f'{doc} saldo')
    for r in pendiente:
        if not r['id'] in salida['motivo'] and not r['soporte'] in salida['motivo']:
            raise AssertionError(f"{doc}: el motivo no nombra {r['id']} ({r['soporte']})")
        if 'aplicacion' not in salida['motivo']:
            raise AssertionError(f'{doc}: el motivo no declara la aplicacion como pendiente')
    if f['metodo'] == 'PPD' and pagos:
        fecha = limite(datetime.fromisoformat(pagos[0]['fecha_pago']).date())
        igual(fecha.isoformat(), salida['limite_rep'], f'{doc} vencimiento')
        estado = 'VENCIDO' if corte > fecha else 'VENCE_HOY' if corte == fecha else 'EN_PLAZO'
        igual(estado, salida['estado_plazo'], f'{doc} plazo')
    else:
        igual('', salida['limite_rep'], f'{doc} sin fecha REP')
    if salida['rep'] == 'LIBERABLE_REP':
        igual(sum(D(r['confirmado']) for r in pagos), D(salida['importe_rep_propuesto']), f'{doc} propuesta')
    igual('PENDIENTE_REVISION_CONTADOR', salida['fiscal'], f'{doc} sin timbrado')

# Casos que evitan perder información al agregar rutas o imponer un bloqueo global.
s = {r['documento']: r for r in leer('salida-documentos')}
igual('LIBERABLE_REP', s['D2']['rep'], 'firma faltante no elimina pago')
igual('LIBERABLE_FACTURA', s['D3']['factura'], 'credito sin pago permite expediente factura')
igual('SIN_PAGO_REP', s['D3']['rep'], 'credito no equivale a cobro')
igual('LIBERABLE_FACTURA', s['D4']['factura'], 'faltante de custodia no retiene la factura entregada')
igual('RETENER_REP', s['D5']['rep'], 'transferencia contradictoria requiere aclaracion')
igual('DESCONOCIDO', s['D5']['saldo_tras_pago_confirmado'], 'd5 sin aplicacion confirmada no tiene saldo')
igual('LIBERABLE_REP', s['D6']['rep'], 'otra incidencia de R2 no bloquea C6')
igual(date(2027, 1, 5), limite(date(2026, 12, 31)), 'cambio de año')
ex = leer('salida-excepciones')
igual(5, len(ex), 'incidencias sin compensar')
for r in ex:
    igual(D(r['esperado']) - D(r['observado']), D(r['diferencia']), r['id'])
    if not r['responsable'] or not r['accion']:
        raise AssertionError(f"{r['id']}: falta responsable o accion")
igual({'E4', 'E5'}, {r['id'] for r in ex if r['documento'] == 'D5'}, 'd5 deja de lado de cobranza y de banco')
print('OK: 2 rutas, 6 documentos, 5 incidencias; saldos, medios de cobro y plazo comprobados.')
