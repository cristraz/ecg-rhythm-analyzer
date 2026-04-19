# Modificaciones al Código Base

Este documento describe las modificaciones realizadas a los repositorios públicos utilizados como base para el proyecto ECG Rhythm Analyzer.

## Repositorios base
- [PTB-XL Benchmarking](https://github.com/helme/ecg_ptbxl_benchmarking)
- [ECG-Digitiser](https://github.com/felixkrones/ECG-Digitiser)

---

## Preparación de Datos

### Código reutilizado
- Funciones de carga de registros de `utils.py` del repositorio PTB-XL Benchmarking (wfdb.rdsamp())
- Script de descarga automática del dataset desde PhysioNet

### Modificaciones realizadas
- Se eliminó la carga de las 12 derivaciones, dejando únicamente la derivación DII (columna índice 1)
- Se adaptó la función de carga de etiquetas para producir clasificación binaria (Normal vs. Arritmia)

### Código escrito desde cero
- Script de etiquetado binario: reagrupa las 5 superclases de PTB-XL en 2 clases (NORM → 0, MI/STTC/CD/HYP → 1)
- Filtro de confianza: elimina registros con likelihood < 75%
- Exportación de señales en formato .npy organizadas por split (train/val/test)

---

## Generación de Imágenes Sintéticas

### Código reutilizado
- Generador de imágenes de ECG del repositorio ECG-Digitiser (gen_ecg_images_from_data_batch.py)

### Modificaciones realizadas
- Se cambió el layout de 3 filas × 4 columnas (12 derivaciones) a una sola tira horizontal (derivación DII)
- Se eliminaron los metadatos textuales de la imagen (nombres de derivaciones, datos del paciente, fecha)
- Se configuró la cuadrícula para simular papel térmico: cuadros grandes en rosa/rojo claro, subdivisiones más tenues, trazado en negro
- Se fijó el tamaño de salida a 224×224 píxeles

### Código escrito desde cero
- Pipeline de augmentation fotográfico: rotación aleatoria 0-3°, variación de brillo/contraste ±15%, ruido gaussiano leve
- Script de organización de carpetas en estructura ImageFolder de PyTorch (train/val/test con subcarpetas normal/arritmia)

---

## Entrenamiento del Modelo CNN

### Código reutilizado
- Estructura general del pipeline de entrenamiento del repositorio PTB-XL Benchmarking (scp_experiment.py)

### Modificaciones realizadas
- Se reemplazó la arquitectura CNN 1D por EfficientNet-B0 (CNN 2D) para procesar imágenes en lugar de señales numéricas
- Se reemplazó la última capa del modelo: model.classifier[1] = nn.Linear(1280, 1) para clasificación binaria
- Se adaptaron las métricas de evaluación para clasificación binaria (accuracy, sensibilidad, especificidad, AUC-ROC)

### Código escrito desde cero
- Data loader con ImageFolder y normalización ImageNet
- Data augmentation en entrenamiento (RandomRotation, ColorJitter, RandomAffine, GaussianBlur)
- Weighted loss para manejo de desbalance de clases
- Early stopping con patience=5
- Transfer learning en dos fases: Fase 1 con capas congeladas (lr=1e-3), Fase 2 con fine-tuning (lr=1e-5)
- ReduceLROnPlateau scheduler
- Exportación del modelo a formato ONNX

---

## App y Despliegue

### Código reutilizado
- Ninguno. La app fue desarrollada desde cero.

### Código escrito desde cero
- `app.py`: interfaz web completa con Streamlit que incluye carga de imagen, preprocesamiento con normalización ImageNet, inferencia con ONNX Runtime, visualización de resultados con código de color (verde/rojo), manejo de errores, instrucciones de uso y disclaimer médico
- `requirements.txt`: lista de dependencias del proyecto

### Decisiones técnicas
- Se usó ONNX Runtime en lugar de PyTorch para la inferencia porque es más liviano y no requiere instalar PyTorch en producción
- El preprocesamiento replica exactamente los parámetros usados durante el entrenamiento (normalización ImageNet, resize a 224×224) para garantizar consistencia
- La app detecta automáticamente si el modelo real está disponible y usa modelo dummy si no lo encuentra

---

## Conclusión
*Por completar al finalizar el proyecto.*

