# Cuadre de rutas

Cruza carga, entrega, retorno recibido, efectivo, transferencias, crédito y evidencia de cada parada. Entrega expedientes de factura o recibo electrónico de pago (REP) que pueden pasar al contador y diferencias con responsable de resolverlas.

Autor: **Heroldo Escobedo**. Versión 1.1: 2026-10-29. Página: https://heroldo.org/skills/cuadre-de-rutas/ · a la venta en [Agensi](https://agensi.io/skills/cuadre-de-rutas).

## Uso en 3 pasos (sin instalar nada)

1. **Pega las reglas.** Copia el contenido de `SKILL.md` y adjunta `references/contrato.md` (los campos que hacen falta) y `references/fuentes.md` (el plazo del REP y su fuente oficial). Los tres viajan juntos dentro de `cuadre-de-rutas.zip`, en la carpeta `cuadre-de-rutas/`. Si ya tienes la skill conectada, este paso no hace falta.
2. **Adjunta lo que ya tengas** —tabla pegada en el chat, Excel, CSV o el exporte de tu sistema, con los nombres de columna que ya use— y escribe delante: **empresa, corte con zona** (por ejemplo «Corte 2026-10-31T18:00:00-06:00») y **política de evidencias** (foto/firma/hora, si la pides). No hay plantilla que preparar; si falta un campo imprescindible, la skill lo pide y no lo inventa.
3. **Pide las tres tablas:** «Cuadra las rutas al corte indicado y dame las tres tablas». Recibes rutas, documentos (factura y REP con su fecha límite) y excepciones con responsable, más los pendientes con la atribución, listos para copiar.

Sin terminal, sin scripts obligatorios, sin API ni configuración técnica. La comprobación de cuentas en `ejemplos/test_caso.py` es opcional y nada depende de ella. No adjuntes contraseñas, certificados privados ni llaves.

En los pasos de arriba `SKILL.md`, `references/` y `ejemplos/` están escritos como quedan dentro del ZIP (la carpeta `cuadre-de-rutas/`); en el repositorio están dentro de `skills/cuadre-de-rutas/`.

## Prueba sin tus datos

Adjunta el archivo `ejemplos/entrada-completa.md` completo —trae el corte, la política de evidencias, los vencimientos de crédito, la condición simulada y los seis conjuntos de datos en un solo bloque— y escribe literalmente:

> Cuadra las rutas de Andén Norte al corte 2026-10-29T12:00:00-06:00 de este bloque y dame las tres tablas.

Compara con `ejemplos/salida-esperada.md`, que es la salida ya armada para copiar; las cuentas a mano están en `ejemplos/CASO.md`. El bloque de entrada no trae resultados esperados, para que la prueba no se contamine.

## Instalar la skill (opcional)

Si prefieres tenerla siempre disponible, sube **`cuadre-de-rutas.zip`** (ya preparado: `SKILL.md`, `references/`, `ejemplos/`, `README.md` y `LICENSE` dentro de la carpeta `cuadre-de-rutas/`) desde la opción de cargar skills de tu cuenta; en Claude: Configuración → Capacidades → Skills. Si lo armas tú mismo, comprime la carpeta `skills/cuadre-de-rutas/` y mete además en esa misma carpeta el `LICENSE` y este `README.md`, para que la atribución viaje con la skill. La disponibilidad del conector de Agensi y de la carga de ZIP depende de tu plan.

## Qué trae el paquete

```
cuadre-de-rutas/
  README.md                    esta página
  LICENSE                      Licencia de uso de Heroldo 1.0
  cuadre-de-rutas.zip          la skill ya comprimida, para subirla sin armar nada
  skills/cuadre-de-rutas/
    SKILL.md                   las reglas y el formato de salida
    references/               contrato.md (campos) y fuentes.md (SAT, con fecha de consulta)
    ejemplos/                 entrada-completa.md, CASO.md, salida-esperada.md,
                              los 6 CSV de entrada, los 3 de salida y test_caso.py (opcional)
  revision/                    informes internos de las casas revisoras: NO se entregan al comprador
```

Al vender o entregar el paquete se excluye `revision/`: son notas de revisión entre casas, con nombres ajenos al ejemplo. Dentro de `cuadre-de-rutas.zip` la carpeta `cuadre-de-rutas/` va plana —`SKILL.md`, `references/`, `ejemplos/`, `LICENSE` y este `README.md`—, de modo que los enlaces de `SKILL.md` funcionan sin instalar nada y el ejemplo viaja con la skill.

---

## Licencia

**Propiedad intelectual de Heroldo Escobedo**, con el código a la vista ([Licencia de uso de Heroldo 1.0](LICENSE)):

- **Uso personal: gratis.** Léelo, pruébalo y adáptalo para aprender o en tus propios datos.
- **Uso en una empresa o con fines de lucro: solo con compra.** Cómpralo en [Agensi](https://agensi.io/skills/cuadre-de-rutas)
  o escribe a heroldo@lolo-enterprises.com. La compra cubre a tu empresa.
- **Siempre se cita la fuente:** «Basado en una skill de Heroldo Escobedo — heroldo.org».
- No se revende ni se vuelve a publicar.

> **In English:** Source-available, not open source. Free for personal use. Business use requires purchase on
> [Agensi](https://agensi.io/skills/cuadre-de-rutas). Attribution to Heroldo Escobedo — heroldo.org is always required.
