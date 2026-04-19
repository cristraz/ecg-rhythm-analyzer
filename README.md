# 🫀 ECG Rhythm Analyzer

Proyecto académico de machine learning para clasificación binaria de ritmo cardíaco (Normal vs. Arritmia) a partir de imágenes de electrocardiogramas en derivación DII.

## Descripción

Este sistema analiza fotografías de tiras de ritmo cardíaco y las clasifica automáticamente como ritmo normal o arritmia usando una red neuronal convolucional (CNN) entrenada con imágenes sintéticas del dataset PTB-XL.

## Tecnologías utilizadas

- Python 3.x
- Streamlit (interfaz web)
- PyTorch + EfficientNet-B0 (modelo CNN)
- ONNX Runtime (inferencia)
- OpenCV / Pillow (procesamiento de imágenes)
- PTB-XL Database (dataset de ECGs)

## Integrantes

Stephanie Cuevas
Gabriela Domínguez
Gloria Rodríguez
Cristina Stanziola

## Cómo ejecutar localmente

1. Clona el repositorio:
```
git clone https://github.com/cristraz/ecg-rhythm-analyzer.git
cd ecg-rhythm-analyzer
```

2. Instala las dependencias:
```
python -m pip install -r requirements.txt
```

3. Ejecuta la app:
```
python -m streamlit run app.py
```

4. Abre tu navegador en `http://localhost:8501`

## Repositorios base utilizados

- [PTB-XL Benchmarking](https://github.com/helme/ecg_ptbxl_benchmarking) — pipeline de entrenamiento y carga de datos
- [ECG-Digitiser](https://github.com/felixkrones/ECG-Digitiser) — generación de imágenes sintéticas de ECG

## Resultados

*Por completar al finalizar el entrenamiento del modelo.*

## App desplegada

https://ecg-rhythm-analyzer-f2jktkxqkkccdneihpr4b2.streamlit.app/

## Licencia

MIT License — ver archivo LICENSE para más detalles.

## Atribución académica

Proyecto desarrollado para el curso de Instrumentación Biomédica Avanzada 2026-1, Universidad Latina de Panamá, 2026.
Dataset: Wagner, P., et al. (2020). PTB-XL, a large publicly available electrocardiography dataset. Scientific Data, 7(1), 154.
