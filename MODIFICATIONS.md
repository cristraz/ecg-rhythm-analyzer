# MODIFICATIONS.md — Semana 2
## Colaboradora: Gloria (Estudiante B)

---

## 1. Archivos modificados

El generador base utilizado fue el `ecg-image-kit`. Se tomó como referencia su pipeline de generación de imágenes ECG y se realizaron las siguientes modificaciones para adaptarlo a los requerimientos del proyecto.

---

## 2. Cambios en el layout

| Parámetro | Valor original | Valor nuevo |
|---|---|---|
| Formato de derivaciones | 3 filas × 4 columnas (12 derivaciones) | 1 sola derivación (DII única) |
| Tamaño de salida | Variable | 224 × 224 píxeles |
| Orientación | Multi-derivación | Tira horizontal única |

Se eliminó completamente el layout de 3 filas × 4 columnas y se reemplazó por una sola derivación DII que ocupa todo el ancho de la imagen, simulando la tira de ritmo que sale de un monitor de signos vitales.

---

## 3. Código eliminado

- Layout multi-derivación (3 filas × 4 columnas)
- Texto con nombre del paciente
- Texto con fecha y hora del registro
- Etiquetas de nombres de derivaciones (DII, V1, V2, etc.)
- Datos técnicos del dispositivo

La imagen final contiene únicamente la cuadrícula y el trazado de la señal, sin ningún texto ni metadato visible.

---

## 4. Cambios en la cuadrícula

| Parámetro | Valor original | Valor nuevo |
|---|---|---|
| Color fondo | Blanco puro `#FFFFFF` | Blanco hueso `#FFF8F8` |
| Color cuadrícula grande (5mm) | Gris | Rosa/rojo claro `#E07070` |
| Color cuadrícula pequeña (1mm) | Gris claro | Rosa tenue `#F4AAAA` |
| Grosor línea grande | Variable | 0.7px, alpha 0.7 |
| Grosor línea pequeña | Variable | 0.3px, alpha 0.6 |
| Color trazado señal | Variable | Negro `#000000`, 0.8px |

---

## 5. Código escrito desde cero

### Pipeline de augmentation fotográfico
Se implementó desde cero una función de augmentation que simula imperfecciones de fotografías reales tomadas con celular:

- **Rotación aleatoria**: entre -3 y +3 grados
- **Variación de brillo**: factor aleatorio entre 0.85 y 1.15 (±15%)
- **Variación de contraste**: factor aleatorio entre 0.85 y 1.15 (±15%)
- **Ruido gaussiano**: media 0, desviación estándar 4
- **Desenfoque gaussiano**: radio 0.5, aplicado con 30% de probabilidad

El augmentation se aplica únicamente al set de entrenamiento (train), no a val ni test.

### Organización de carpetas
Se escribió desde cero el pipeline de organización automática de imágenes en la estructura que PyTorch ImageFolder requiere:
images/
train/
normal/
arritmia/
val/
normal/
arritmia/
test/
normal/
arritmia/

### Pipeline de generación masiva
Se implementó desde cero el procesamiento de las ~19,000 señales con reporte de progreso en tiempo real (imágenes procesadas, tiempo transcurrido y tiempo estimado restante).

---

## 6. Resultados finales

| Split | Normal | Arritmia | Total |
|---|---|---|---|
| Train | 6,896 | 8,364 | 15,260 |
| Val | 853 | 1,039 | 1,892 |
| Test | 864 | 1,043 | 1,907 |
| **Total** | **8,613** | **10,446** | **19,059** |

---

## 7. Dependencias utilizadas

- `matplotlib` — generación de imágenes
- `Pillow (PIL)` — augmentation fotográfico y guardado
- `numpy` — manejo de señales
- `pandas` — lectura de etiquetas
- `opencv-python-headless` — procesamiento de imágenes
