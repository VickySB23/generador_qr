import streamlit as st
import requests

st.set_page_config(page_title="Generador de QR", page_icon="📱")

st.title("📱 Generador de Códigos QR")
st.write("Ingresá un enlace y generá tu código QR al instante. Seguro, rápido y sin dejar rastros en el servidor.")

url_input = st.text_input("Enlace (URL):", placeholder="https://www.ejemplo.com")

if st.button("Generar QR", type="primary"):
    if url_input:
        with st.spinner("Generando..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/v1/generate-qr/",
                    json={"url": url_input}
                )

                if response.status_code == 200:
                    st.success("¡QR generado con éxito!")
                    image_bytes = response.content
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.image(image_bytes, caption="Tu código QR", use_container_width=True)
                        st.download_button(
                            label="Descargar QR",
                            data=image_bytes,
                            file_name="mi_codigo_qr.png",
                            mime="image/png",
                            use_container_width=True
                        )
                elif response.status_code == 422:
                    st.error("⚠️ Por favor, ingresá una URL válida (debe incluir http:// o https://).")
                else:
                    st.error("❌ Ocurrió un error en el servidor.")
            
            except requests.exceptions.ConnectionError:
                st.error("🔌 Error de conexión: Asegurate de que la API de FastAPI esté corriendo de fondo.")
    else:
        st.warning("Por favor, escribí un enlace primero.")