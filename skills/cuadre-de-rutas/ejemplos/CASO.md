# Caso FICTICIO de Andén Norte

Todos los folios, clientes, importes, referencias y roles son inventados. No hay fotos, firmas reales, cuentas, XML ni UUID válidos. Este ejemplo comprueba la conciliación operativa, no autoriza emisión fiscal.

Corte: **2026-10-29T12:00:00-06:00**. Las dos rutas salieron el 2026-10-28 a las 08:00 -06:00. Una partida y una parada por documento; todas las cantidades son cajas y todos los importes MXN. Política comercial ficticia: foto, firma y hora para aceptar entrega; sin tolerancia de cantidades ni dinero. Referencias FOTO/FIRMA presentes representan evidencia revisada dentro de la simulación, no archivos que el agente haya visto. Se autoriza crédito de 400 en D3 y 200 en D4, con vencimiento comercial 2026-11-12. No hay fondos, gastos, retiros ni otros movimientos. Tesorería confirma los recibos/abonos según `cobros.csv`; no hay REP previos. Las facturas emitidas se suponen vigentes solo para la simulación.

## Entrada y cuentas manuales

Leer `operacion.csv`, `retornos.csv`, `evidencias.csv`, `cobros.csv`, `caja.csv` y `facturas.csv`. Primera fila de datos = fila 2 del archivo. Todo eso, junto y listo para pegar en un chat, está en `entrada-completa.md`; la salida que debe salir, en `salida-esperada.md`.

| Documento | Cuenta física y comercial | Cuenta de dinero/cartera |
|---|---|---|
| D1 | 10 cargadas = 10 entregadas; 10 × 100 = 1000 | C1 acredita 1000 de efectivo del cliente; caja recibe 950: faltan 50 de custodia, no de pago del cliente |
| D2 | 5 = 4 entregadas + 1 recibida por DEV1/REC-1; valor entregado 400 | Factura 500 menos ajuste NC-2 de 100 ya aplicado = saldo anterior 400; C2/ABONO-2 paga 400; insoluto 0 |
| D3 | 4 = 4 entregadas; valor 400; evidencia completa | Sin cobro; CRED-3 autoriza 400 de cartera |
| D4 | 3 cargadas - 2 entregadas - 0 recibidas = 1 sin aclarar | Valor entregado 200 a crédito CRED-4; DEV2 declara 1 caja pero carece de recepción (custodia, E3); no inventar devolución ni merma |
| D5 | 2 = 2 entregadas; valor 200 | Declara transferencia 150; ABONO-5 acredita 100: diferencia 50. Solo si Tesorería confirma que ABONO-5 se aplica a D5: 200 - 100 = 100; sin esa confirmación el saldo es DESCONOCIDO y no es 50; 50 que nadie declaró cobrados ni tienen crédito: E5 a Cobranza |
| D6 | 1 = 1 entregada; valor 100 | C6 acredita efectivo 100 y caja recibe 100; saldo 100 - 100 = 0 |

Totales esperados en `salida-rutas.csv`:

- R1: carga 19 = entregas 18 + retorno recibido 1. Entregado 1800 = efectivo cliente 1000 + transferencia 400 + cartera 400. Caja 1000 - 950 = 50; falta además firma D2. La suma de efectivo contado 950 + banco 400 + cartera 400 = 1750 muestra esos mismos 50; no sumarlos otra vez como otra pérdida.
- R2: carga 6 - entregas 5 - retorno recibido 0 = **1 caja pendiente**. Entregado 500 = efectivo 100 + banco acreditado 100 + crédito 200 + **saldo sin resolver 100** de D5. Ese saldo 100 son dos diferencias distintas: 50 declarados por la ruta sin abono (E4, Tesorería) y 50 que nadie declaró cobrados ni tienen crédito autorizado (E5, Cobranza). No son el mismo dinero: no se compensan entre sí ni se suman otra vez. El banco tiene 100 acreditados (ABONO-5) y es otro dato: mientras no se confirme a qué documento se aplican, el importe de D5 sin conciliación documental es 200 y baja a 100 si se aplican ahí. No cuentes el acreditado y el sin aplicar como dos pérdidas, ni los sumes al faltante de transferencia de E4. El retorno declarado 1 no cierra el físico.

## Decisiones esperadas

Ver `salida-documentos.csv` y la salida armadas en markdown en `salida-esperada.md`. Ninguna fila está LISTA_PARA_TIMBRAR: faltan XML, UUID reales, datos fiscales del receptor/emisor e impuestos aplicables por validar con el contador. LIBERABLE identifica solo expediente operativo listo para su revisión.

- D1: ya emitida PUE; no duplicar factura ni proponer REP. E1 a Caja R1 por custodia (cobros fila 2 / caja fila 2). Si en uso real apareciera contradicción de fecha/método, remitir al contador.
- D2: ya emitida; **REP 400 liberable para revisión** por C2 (cobros fila 3, facturas fila 3). Firma ausente en evidencias fila 3 → E2 al Repartidor R1. Mantener la incidencia comercial independiente del pago acreditado. Saldo 400 - 400 = 0, no restar NC-2 nuevamente.
- D3: **factura liberable a crédito** por 400 (operación/evidencias/facturas fila 4); sin pago, no proponer REP. Facturación recibe el expediente.
- D4: **factura liberable a crédito** por 200 (2 cajas entregadas con evidencia; operación fila 5 / evidencias fila 5 / facturas fila 5). La caja de DEV2 sin recepción es custodia del repartidor, no cambia lo que el cliente recibió: E3 a Almacén para comprobar con Repartidor R2. Sin pago, no REP.
- D5: ya emitida; **retener propuesta REP de 150** por inconsistencia con abono de 100 (cobros fila 4). E4 a Tesorería. E5 a Cobranza por los 50 sin pago ni crédito. El abono de 100 conserva su fecha real y su vencimiento de REP mientras se aclara: si Tesorería confirma que se aplica a D5 y separa los otros 50, preparar REP de 100 con saldo resultante 100 (200 - 100), sin esperar la cobranza restante; sin esa confirmación el saldo queda DESCONOCIDO y no se da por reducido. No antedatar ni ignorar su vencimiento mientras se aclara.
- D6: ya emitida; **REP 100 liberable para revisión** (cobros fila 5 / caja fila 3 / facturas fila 7), aunque la misma R2 tenga E3/E4/E5.

Todos los pagos son del 28-octubre: límite REP = **2026-11-05**, EN_PLAZO al corte. Para D1 no se propone REP por PUE; para D3/D4 no hay fecha límite REP sin pago. Ejemplo adicional de calendario: pago 2026-12-31 → 2027-01-05. Corte en el día 5 → VENCE_HOY; después → VENCIDO y escalar sin antedatar. Fuente: `../references/fuentes.md`.

`salida-excepciones.csv` contiene cinco incidencias con responsables **de resolver, no culpables**. Seguimiento POR_ACORDAR porque nadie ha comprometido fecha; el plazo fiscal sigue visible en la salida documental. Las evidencias fiscales faltantes son una limitación general declarada, no cuatro incidencias comerciales adicionales.

Comprobación opcional de las cuentas (no hace falta para usar la skill), desde la carpeta del paquete: `python3 ejemplos/test_caso.py`. Usa aritmética decimal y los mismos CSV, sin acceder a servicios externos.
