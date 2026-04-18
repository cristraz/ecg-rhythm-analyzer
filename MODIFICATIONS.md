## Gloria — Imágenes Sintéticas

### Archivos modificados de ecg-image-kit
- gen_ecg_images_from_data_batch.py: se modificaron los parámetros de layout y resolución

### Parámetros cambiados
| Parámetro | Valor original | Valor nuevo |
|---|---|---|
| --num_leads | 12 | 1 |
| --num_columns | 3 | 1 |
| --resolution | default | 224 |
| --remove_lead_names | desactivado | activado |

### Código eliminado
- Layout multi-derivación (3 filas × 4 columnas)
- Metadatos de texto (nombre de derivaciones, fecha, datos del paciente)

### Código escrito desde cero
- Conversión de señales .npy a formato WFDB
- Pipeline de augmentation: rotación aleatoria, variación de brillo y contraste, ruido gaussiano
- Organización de imágenes en carpetas train/val/test con subcarpetas normal/arritmia
