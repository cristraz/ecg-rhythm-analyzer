## Stephanie — Datos y Señales (feature/data-preparation)

### Código reutilizado
Se reutilizaron las funciones del repositorio ecg_ptbxl_benchmarking para 
leer los archivos de señales usando la librería wfdb-python. Específicamente 
la función wfdb.rdsamp() para cargar los registros del dataset PTB-XL.

### Código modificado
Se modificó la carga original de las 12 derivaciones del ECG para extraer 
únicamente la derivación DII (columna índice 1), que es la derivación 
estándar para monitoreo de ritmo cardíaco.

### Código escrito desde cero
Se escribió completamente desde cero el script de etiquetado binario, que 
convierte las 5 superclases diagnósticas (NORM, MI, STTC, CD, HYP) en 2 
clases: Normal (0) y Arritmia (1). Este script incluye un filtro de 
confianza del 75% para descartar casos ambiguos, dejando 19,053 registros 
útiles de los 21,799 originales.

### Archivos entregados
- train_signals.npy (15,258 señales)
- val_signals.npy (1,890 señales)
- test_signals.npy (1,905 señales)
- labels.csv (record_id, fold, label, split)
