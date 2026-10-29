# Entrada COMPLETA del caso ficticio de Andén Norte (para pegar o adjuntar)

Pega este bloque entero en el chat, o adjúntalo como archivo, junto con las reglas de `../SKILL.md`, el contrato de `../references/contrato.md` y las fuentes de `../references/fuentes.md`. No trae resultados esperados: esos están aparte, en `CASO.md` y `salida-esperada.md`, para que puedas contrastar sin mirar primero.

---

Empresa: **Andén Norte** (ficticia). Corte: **2026-10-29T12:00:00-06:00**. Las dos rutas (R1, R2) salieron el **2026-10-28 a las 08:00 -06:00**. Una partida y una parada por documento; todas las cantidades son cajas y todos los importes MXN.

Política comercial ficticia de evidencias: se exige **foto, firma y hora** para aceptar una entrega; sin tolerancia de cantidades ni de dinero. No es requisito fiscal del SAT.

Crédito autorizado: 400 en D3 y 200 en D4, con **vencimiento comercial 2026-11-12**. No hay fondos iniciales, gastos, retiros ni otros movimientos. Tesorería confirma los recibos/abonos según la tabla de cobros; no hay REP previos.

Condición simulada: los UUID `SIM-*` y las referencias FOTO/FIRMA son identificadores pedagógicos sin validez fiscal, representados como verificados dentro del escenario. No hay fotos reales, firmas reales, cuentas bancarias ni XML. Ninguna fila puede salir LISTO_PARA_TIMBRAR.

Se pide: **cuadra las rutas R1 y R2 al corte 2026-10-29T12:00:00-06:00 y entrega las tres tablas** (rutas, documentos, excepciones) con las reglas de la skill.

## Los seis conjuntos de datos

### Carga y entrega (operacion.csv)

```csv
ruta,documento,parada,producto,unidad,carga,entregado,precio_final,remision
R1,D1,P1,CAJA-A,caja,10,10,100.00,SAL-1
R1,D2,P2,CAJA-B,caja,5,4,100.00,SAL-2
R1,D3,P3,CAJA-C,caja,4,4,100.00,SAL-3
R2,D4,P4,CAJA-D,caja,3,2,100.00,SAL-4
R2,D5,P5,CAJA-E,caja,2,2,100.00,SAL-5
R2,D6,P6,CAJA-F,caja,1,1,100.00,SAL-6
```

### Retornos (retornos.csv)

```csv
id,ruta,documento,declarado,recibido,folio_recepcion,motivo,responsable
DEV1,R1,D2,1,1,REC-1,rechazo comercial,Almacen
DEV2,R2,D4,1,0,,rechazo comercial,Repartidor R2
```

### Evidencias (evidencias.csv)

```csv
documento,foto,firma,hora,receptor,estado_escenario
D1,FOTO-1,FIRMA-1,2026-10-28T10:00:00-06:00,Cliente ficticio 1,verificado ficticio
D2,FOTO-2,,2026-10-28T11:00:00-06:00,Cliente ficticio 2,falta firma
D3,FOTO-3,FIRMA-3,2026-10-28T12:00:00-06:00,Cliente ficticio 3,verificado ficticio
D4,FOTO-4,FIRMA-4,2026-10-28T10:30:00-06:00,Cliente ficticio 4,verificado ficticio
D5,FOTO-5,FIRMA-5,2026-10-28T11:30:00-06:00,Cliente ficticio 5,verificado ficticio
D6,FOTO-6,FIRMA-6,2026-10-28T12:30:00-06:00,Cliente ficticio 6,verificado ficticio
```

### Cobros (cobros.csv)

```csv
id,ruta,documento,fecha_pago,medio,moneda,declarado,confirmado,soporte,parcialidad
C1,R1,D1,2026-10-28T10:05:00-06:00,efectivo,MXN,1000.00,1000.00,RECIBO-1,1
C2,R1,D2,2026-10-28T11:05:00-06:00,transferencia,MXN,400.00,400.00,ABONO-2,1
C5,R2,D5,2026-10-28T11:35:00-06:00,transferencia,MXN,150.00,100.00,ABONO-5,1
C6,R2,D6,2026-10-28T12:35:00-06:00,efectivo,MXN,100.00,100.00,RECIBO-6,1
```

### Caja (caja.csv)

```csv
ruta,moneda,fondo,gastos_autorizados,retiros_acreditados,contado,recibo_caja,responsable
R1,MXN,0.00,0.00,0.00,950.00,CAJA-1,Caja R1
R2,MXN,0.00,0.00,0.00,100.00,CAJA-2,Caja R2
```

### Facturas y cartera (facturas.csv)

```csv
documento,estado,uuid_simulado,metodo,moneda,total_documento,ajuste_aplicado,saldo_anterior,credito_autorizado,autorizacion,rep_previos
D1,emitida,SIM-D1,PUE,MXN,1000.00,0.00,1000.00,0.00,,ninguno
D2,emitida,SIM-D2,PPD,MXN,500.00,100.00,400.00,0.00,NC-2,ninguno
D3,borrador,,PPD,MXN,400.00,0.00,400.00,400.00,CRED-3,ninguno
D4,borrador,,PPD,MXN,200.00,0.00,200.00,200.00,CRED-4,ninguno
D5,emitida,SIM-D5,PPD,MXN,200.00,0.00,200.00,0.00,,ninguno
D6,emitida,SIM-D6,PPD,MXN,100.00,0.00,100.00,0.00,,ninguno
```
