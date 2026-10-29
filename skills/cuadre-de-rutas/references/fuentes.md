# Fuentes y alcance

Consulta realizada el **2026-10-29**. Las fuentes fiscales son oficiales; las reglas de cuadre y los responsables son criterios operativos, no obligaciones fiscales nuevas. Antes de aplicar a un periodo distinto o emitir, comprobar modificaciones publicadas y conservar la versión consultada.

## SAT: guía de llenado de pagos

- Autor: Servicio de Administración Tributaria.
- Título: *Guía de llenado del comprobante al que se le incorpore el complemento para recepción de pagos*. Aplica para CFDI 4.0 y complemento de pagos 2.0.
- URL oficial: http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Guia_llenado_pagos.pdf
- Entrada del SAT: https://wwwmat.sat.gob.mx/consultas/92764/comprobante-de-recepcion-de-pagos
- Fecha inicial: 2021-12-31. Historial del archivo descargado: revisión 4, **2026-01-16**, ajuste de formato (página 111/111); incluye revisiones de 2023-03-08, 2024-03-22 y 2025-12-29.
- Medición: descarga HTTP del dominio oficial, respuesta 200, **1 962 569 bytes**; SHA-256 `d76bcaddc343fd23f6a03a0d735815f848655a01953c1884e6ca71f8c58c4700`. HTTPS agotó tiempo; no se presenta esa vía como comprobada. No se incorpora copia del PDF al paquete.
- Localizadores: apartado I, campos FechaPago, FormaDePagoP, MonedaP, Monto, IdDocumento, EquivalenciaDR, NumParcialidad, ImpSaldoAnt, ImpPagado, ImpSaldoInsoluto y nodos de impuestos; apéndice 2, pregunta 4, página 63/111: plazo del quinto día natural del mes siguiente al pago.
- Aplicación: identificar pago/documento, comprobar saldos e impuestos y distinguir pago recibido de crédito pendiente. No usar la hora de entrega como fecha automática de pago.

Comprobación opcional, solo para auditar la fuente (no hace falta para usar la skill):

```bash
curl --fail --max-time 45 'http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Guia_llenado_pagos.pdf' -o /tmp/cuadre-guia-sat.pdf
sha256sum /tmp/cuadre-guia-sat.pdf
pdftotext -layout /tmp/cuadre-guia-sat.pdf /tmp/cuadre-guia-sat.txt
```

Si el archivo cambia, revisar su historial y las reglas utilizadas; una huella distinta no implica incumplimiento.

## RMF 2026: plazo y expedición

- Autor: SAT / Secretaría de Hacienda y Crédito Público, publicación en DOF **2025-12-28**.
- URL oficial: https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf
- Localizador: regla **2.7.1.32**, páginas impresas 112–113 (índices PDF 111–112), “Expedición de CFDI por pagos realizados”.
- Aplicación: comprobante por operación y pagos posteriores; posibilidad de un REP por pago o uno por pagos de un mes al mismo receptor; fecha máxima: **quinto día natural del mes inmediato siguiente al pago recibido**. No son cinco días hábiles ni cinco días desde la entrega.
- Página oficial de apoyo con el texto de la regla: https://wwwmat.sat.gob.mx/articulo/22029/regla-2.7.1.35 (el título visible es 2.7.1.32 aunque la dirección conserve otro número).
- No se pretende compilar todas las modificaciones fiscales ni resolver regímenes especiales. Si el caso requiere una excepción, no inventarla: documentar la duda y enviarla al contador con el vencimiento visible.

## Atribución operativa

Adaptaciones de **Heroldo Escobedo**, *Logistics Crew Skills*, versión publicada en 2026-10-26 bajo CC BY 4.0 (consulta local 2026-10-29). Repositorio fuente: https://github.com/heroldoe-create/logistics-crew-skills ; licencia original https://creativecommons.org/licenses/by/4.0/ .

Se consultaron estas fichas del repositorio fuente (carpeta skills/):

- `log-wms-n5-merchandise-checker/SKILL.md`: cruce entre documento y físico; aquí se adapta al cierre de reparto sin su muestreo ni tolerancias.
- `log-inv-n4-erp-wms-reconciler/SKILL.md`: reconstrucción de trazabilidad y correcciones respaldadas; aquí no se ejecutan ajustes ni reintentos en sistemas.
- `log-wms-n4-reverse-logistics-tech/SKILL.md`: devolución recibida con evidencia y discrepancia de motivo; aquí no se dispone ni destruye mercancía.

Estas adaptaciones incorporan el cruce de cobros y el expediente REP y salen con la licencia del paquete. Las fichas originales conservan CC BY 4.0. El paquete es autónomo: no exige instalar el crew. No se adoptan nombres de sistemas, umbrales económicos ni políticas internas de las fichas.
