# Salida ESPERADA del caso ficticio de Andén Norte

Resultado de correr la skill sobre `entrada-completa.md`. Es el texto que la empresa copia y pega: las tres tablas con los encabezados del `../SKILL.md` §5, sin introducción, y después «Pendientes y alcance». Contrástala con `CASO.md`, que trae las cuentas a mano.

## Rutas

| ruta | unidad | carga | entregado | retorno_declarado | retorno_recibido | diferencia_fisica | moneda | valor_entregado | efectivo_esperado | efectivo_contado | diferencia_caja | transferencia_declarada | transferencia_confirmada | diferencia_transferencia | credito_autorizado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | caja | 19 | 18 | 1 | 1 | 0 | MXN | 1800.00 | 1000.00 | 950.00 | 50.00 | 400.00 | 400.00 | 0.00 | 400.00 |
| R2 | caja | 6 | 5 | 1 | 0 | 1 | MXN | 500.00 | 100.00 | 100.00 | 0.00 | 150.00 | 100.00 | 50.00 | 200.00 |

## Documentos

| documento | factura | rep | importe_rep_propuesto | saldo_tras_pago_confirmado | limite_rep | estado_plazo | fiscal | motivo | responsable | siguiente_accion |
|---|---|---|---|---|---|---|---|---|---|---|
| D1 | YA_EMITIDA | NO_PROPONER_REP | 0.00 | 0.00 |  | NO_APLICA | PENDIENTE_REVISION_CONTADOR | PUE ya emitida; faltante de caja es custodia (E1) | Facturacion | Ninguna fiscal; seguir E1 |
| D2 | YA_EMITIDA | LIBERABLE_REP | 400.00 | 0.00 | 2026-11-05 | EN_PLAZO | PENDIENTE_REVISION_CONTADOR | Pago C2 acreditado 400; firma faltante (E2) | Contador | Revisar y timbrar REP 400 antes del 2026-11-05 |
| D3 | LIBERABLE_FACTURA | SIN_PAGO_REP | 0.00 | 400.00 |  | NO_APLICA | PENDIENTE_REVISION_CONTADOR | Entrega completa a credito CRED-3 | Facturacion | Revisar y emitir factura 400 a credito |
| D4 | LIBERABLE_FACTURA | SIN_PAGO_REP | 0.00 | 200.00 |  | NO_APLICA | PENDIENTE_REVISION_CONTADOR | Entrega de 2 cajas firmada a credito CRED-4; caja DEV2 sin recepcion (E3) | Facturacion | Revisar y emitir factura 200 a credito; seguir E3 |
| D5 | YA_EMITIDA | RETENER_REP | 0.00 | DESCONOCIDO | 2026-11-05 | EN_PLAZO | PENDIENTE_REVISION_CONTADOR | ABONO-5 acredita 100 en banco; aplicacion a D5 pendiente; saldo antes de aplicacion 200; si se confirma aplicacion de 100 el saldo resulta 100; declarado 150 contra abono 100 (E4); 50 sin pago ni credito (E5) | Tesoreria | Confirmar aplicacion de ABONO-5; si aplica REP 100 antes del 2026-11-05 |
| D6 | YA_EMITIDA | LIBERABLE_REP | 100.00 | 0.00 | 2026-11-05 | EN_PLAZO | PENDIENTE_REVISION_CONTADOR | Pago C6 acreditado 100 | Contador | Revisar y timbrar REP 100 antes del 2026-11-05 |

## Excepciones

| id | ruta | documento | tipo | esperado | observado | diferencia | unidad | responsable | accion | plazo_seguimiento |
|---|---|---|---|---|---|---|---|---|---|---|
| E1 | R1 | D1 | caja | 1000.00 | 950.00 | 50.00 | MXN | Caja R1 | Recontar con repartidor R1 y rastrear entrega de efectivo | POR_ACORDAR |
| E2 | R1 | D2 | firma | 1 | 0 | 1 | evidencia | Repartidor R1 | Recuperar firma de P2 sin retrasar REP de C2 | POR_ACORDAR |
| E3 | R2 | D4 | retorno | 1 | 0 | 1 | caja | Almacen | Verificar con repartidor R2 la caja DEV2 y registrar recepcion real | POR_ACORDAR |
| E4 | R2 | D5 | transferencia | 150.00 | 100.00 | 50.00 | MXN | Tesoreria | Confirmar aplicacion de ABONO-5 y cobrar o aclarar 50.00 | POR_ACORDAR |
| E5 | R2 | D5 | cobranza | 200.00 | 150.00 | 50.00 | MXN | Cobranza | Cobrar o autorizar credito por 50.00 que no se declaro cobrado | POR_ACORDAR |

## Pendientes y alcance

- No comprobado: XML, UUID reales, datos fiscales de emisor y receptor, e impuestos. Los UUID `SIM-*` y las referencias FOTO/FIRMA son pedagógicos: aquí no acreditan evidencia fiscal. Corte: **2026-10-29T12:00:00-06:00**.
- Cubre: rutas R1 y R2, documentos D1 a D6, cobros C1, C2, C5 y C6, retornos DEV1 y DEV2, caja de ambas rutas y evidencias declaradas en el escenario.
- No autoriza nada fiscal: no se emite, no se timbra, no se cancela y no se modifica saldo alguno en sistemas. LIBERABLE = expediente operativo listo para la revisión del contador. Plazo REP según RMF 2026, regla 2.7.1.32 (DOF 2025-12-28), verificado el 2026-10-29.
- D5 queda con saldo DESCONOCIDO mientras Tesorería no confirme a qué documento aplica ABONO-5; E4 (50 declarados sin abono) y E5 (50 sin pago ni crédito) siguen abiertas, con plazo de seguimiento POR_ACORDAR.
- Basado en una skill de Heroldo Escobedo — heroldo.org
