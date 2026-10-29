# Contrato mínimo de entrada y salida

CSV en UTF-8, coma, punto decimal, fechas ISO y zona explícita. Folios como texto; importes en decimal exacto. Agrupar solo después de verificar unicidad y relaciones. Cada fila conserva archivo y número para citarla en la salida. Si hay varias partidas o pagos por documento, usar tablas separadas; no multiplicar cobros al unir con partidas.

## Entradas

| Conjunto | Campos y controles |
|---|---|
| Carga/entrega | ruta, parada, documento, línea, producto, lote si aplica, unidad, carga, entregado, precio, descuentos/impuestos documentados; remisión de salida y acuse |
| Retornos | ID único, ruta/documento/línea, cantidad declarada, cantidad recibida, motivo, fecha, folio receptor y responsable; disposición aparte |
| Evidencias | ID, ruta/parada/documento, foto, firma, receptor y hora con zona; estado de acceso y verificación, política comercial aplicable |
| Cobros | ID único, ruta/documento, fecha real, efectivo o transferencia, moneda, declarado, confirmado, recibo o abono, rol que verifica |
| Aplicaciones | ID de pago → UUID/documento, importe aplicado, moneda/equivalencia y saldo; controlar suma aplicada contra cobro e historial |
| Caja | ruta, fondo inicial, efectivo contado, gastos/retiros autorizados y recibo; custodio y corte |
| Cartera y fiscal | documento, borrador/emitido, UUID y vigencia/hora de consulta, receptor/emisor, PUE/PPD, moneda, total, saldo anterior, ajuste autorizado y aplicado, parcialidad, REP previos, saldo abierto y autorización de crédito; impuestos y equivalencias desde XML/contador |

La evidencia mínima no implica subir fotos de personas al repositorio. En uso real restringir la salida a folios y ubicaciones autorizadas, sin cuentas completas, credenciales ni imágenes personales. En ejemplos solo datos ficticios.

## Simplificaciones declaradas del ejemplo

`operacion.csv` tiene una partida por documento; precio es importe comercial final unitario. `retornos.csv` conserva lo declarado y lo recibido. `cobros.csv` tiene una aplicación por pago; confirmado significa cobro al cliente acreditado por tesorería/recibo, no entrega posterior de caja. La aplicación al documento se da por confirmada solo si declarado = confirmado; si difieren, es RETENER_REP (C5) y el `saldo_tras_pago_confirmado` de ese documento sale **DESCONOCIDO**, no el resultado de restar el abono: primero confirma Tesorería a qué documento se aplica y solo entonces el abono reduce el saldo. El abono sin aplicar conserva su fecha real de pago y su vencimiento de REP. `facturas.csv` aporta el saldo anterior vigente **después** del ajuste autorizado: D2 era 500, ajuste 100, saldo 400. Crédito es el remanente autorizado al cierre, no el importe original antes del pago. Ningún monto es cálculo de impuestos.

Los UUID `SIM-*` y referencias de foto/firma son identificadores pedagógicos sin validez fiscal, representados como verificados dentro del escenario. No hay fotos reales ni XML. Por eso LIBERABLE_REP/FACTURA del ejemplo significa expediente operativo para el contador; la validación fiscal y el timbrado quedan pendientes en **todos** los casos. Ninguno se presenta como comprobante emitible con estos CSV.

## Salida

- `salida-rutas.csv`: cantidades por unidad y dinero por moneda; diferencias con signo esperado menos observado.
- `salida-documentos.csv`: decisión independiente de factura y REP, importe/saldo, vencimiento y estado; evidencia de origen y responsable en el caso narrado.
- `salida-excepciones.csv`: diferencias sin compensar, acción, responsable de resolver y plazo de seguimiento (POR_ACORDAR si no existe compromiso).

En un caso real añade emisor/receptor, UUID verificado, trazabilidad de cada aplicación e impuestos al expediente fiscal. Cualquier dato faltante impide afirmar LISTO_PARA_TIMBRAR. Al corte del ejemplo 2026-10-29, un pago de 2026-10-28 vence 2026-11-05; no se usa la fecha de salida de ruta para calcularlo.
