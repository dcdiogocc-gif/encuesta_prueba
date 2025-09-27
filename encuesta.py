import streamlit as st

# Título de la aplicación
st.title("Encuesta Interactiva")

# Preguntas de la encuesta
st.header("Por favor, responde las siguientes preguntas:")
nombre = st.text_input("¿Cuál es tu nombre?")
edad = st.number_input("¿Cuántos años tienes?", min_value=0, max_value=120, step=1)
ciudad = st.text_input("¿Cuál es tu ciudad de residencia?")
tecnologia = st.radio("¿Te gusta la tecnología?", ["Sí", "No"])

# Mostrar las respuestas al final
if st.button("Enviar respuestas"):
    st.subheader("Tus respuestas:")
    st.write(f"Nombre: {nombre}")
    st.write(f"Edad: {edad}")
    st.write(f"Ciudad de residencia: {ciudad}")
    st.write(f"¿Te gusta la tecnología?: {tecnologia}")
    st.success("¡Gracias por participar en la encuesta!")
