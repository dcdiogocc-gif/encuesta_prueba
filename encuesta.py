import streamlit as st
import sqlite3

# Configuración de la base de datos
conn = sqlite3.connect("encuesta.db")
c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS respuestas (
        nombre TEXT,
        edad INTEGER,
        ciudad TEXT,
        tecnologia TEXT
    )
""")
conn.commit()

# Título de la aplicación
st.title("Encuesta Interactiva")

# Preguntas de la encuesta
st.header("Por favor, responde las siguientes preguntas:")
nombre = st.text_input("¿Cuál es tu nombre?")
edad = st.number_input("¿Cuántos años tienes?", min_value=0, max_value=120, step=1)
ciudad = st.text_input("¿Cuál es tu ciudad de residencia?")
tecnologia = st.radio("¿Te gusta la tecnología?", ["Sí", "No"])

# Guardar respuestas en la base de datos
if st.button("Enviar respuestas"):
    c.execute("INSERT INTO respuestas (nombre, edad, ciudad, tecnologia) VALUES (?, ?, ?, ?)", 
              (nombre, edad, ciudad, tecnologia))
    conn.commit()
    st.success("¡Gracias por participar en la encuesta! Tus respuestas han sido guardadas.")

# Mostrar las respuestas almacenadas
if st.button("Ver respuestas"):
    st.subheader("Respuestas almacenadas:")
    c.execute("SELECT * FROM respuestas")
    datos = c.fetchall()
    for fila in datos:
        st.write(fila)

