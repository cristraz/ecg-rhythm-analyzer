import streamlit as st
from PIL import Image
import numpy as np
import random

# Configuración de la página
st.set_page_config(
    page_title="ECG Rhythm Analyzer",
    page_icon="🫀",
    layout="centered"
)

# Título y descripción
st.title("🫀 ECG Rhythm Analyzer")
st.write("Sube una imagen de una tira de ritmo cardíaco en derivación DII para clasificarla como Normal o Arritmia.")

# Función de preprocesamiento
def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    img_array = np.array(image).astype(np.float32) / 255.0
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    img_array = (img_array - mean) / std
    img_array = np.transpose(img_array, (2, 0, 1))
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Función de inferencia dummy (temporal hasta tener el modelo real)
def predict_dummy(img_array):
    probability = random.uniform(0.0, 1.0)
    return probability

# Carga de imagen
uploaded_file = st.file_uploader("Sube una imagen de ECG", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        # Mostrar imagen
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagen cargada", use_container_width=True)

        # Preprocesar y predecir
        img_array = preprocess_image(image)
        probability = predict_dummy(img_array)

        # Mostrar resultado
        st.subheader("Resultado:")
        if probability >= 0.5:
            st.error(f"🔴 ARRITMIA detectada — Confianza: {probability:.1%}")
        else:
            st.success(f"🟢 Ritmo NORMAL — Confianza: {1 - probability:.1%}")

        st.progress(float(probability))

        # Instrucciones de uso
        with st.expander("¿Qué tipo de imagen funciona mejor?"):
            st.write("""
            - Foto de tira de ritmo en derivación DII
            - Buena iluminación, sin sombras fuertes
            - Imagen centrada y sin recortes
            - Fondo claro (papel térmico rosado o blanco)
            """)

    except Exception as e:
        st.error("No se pudo procesar la imagen. Verifica que el archivo es una imagen válida.")

# Disclaimer médico
st.divider()
st.caption("⚠️ Este es un prototipo académico. No ha sido validado clínicamente. No utilizar para diagnóstico médico.")
