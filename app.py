import streamlit as st
from PIL import Image
import numpy as np
import random
import os

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
    img_array = np.expand_dims(img_array, axis=0).astype(np.float32)
    return img_array

# Función para cargar el modelo ONNX
def load_model():
    try:
        import onnxruntime as ort
        model_path = os.path.join("model", "ecg_model.onnx")
        session = ort.InferenceSession(model_path)
        return session
    except Exception:
        return None

# Función de inferencia
def predict(img_array, session):
    if session is None:
        # Modelo dummy mientras no llegue el real
        return random.uniform(0.0, 1.0)
    input_name = session.get_inputs()[0].name
    result = session.run(None, {input_name: img_array})
    probability = float(1 / (1 + np.exp(-result[0][0][0])))
    return probability

# Cargar modelo al iniciar
session = load_model()

if session is not None:
    st.info("✅ Modelo real cargado correctamente.")
else:
    st.warning("⚙️ Usando modelo de prueba — el modelo real se integrará en Semana 3.")

# Carga de imagen
uploaded_file = st.file_uploader("Sube una imagen de ECG", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        # Mostrar imagen
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagen cargada", use_container_width=True)

        # Preprocesar y predecir
        img_array = preprocess_image(image)
        probability = predict(img_array, session)

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