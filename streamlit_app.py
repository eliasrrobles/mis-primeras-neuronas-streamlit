import streamlit as st

st.image("img/neurona.png")
st.title("Mis primeras neuronas")
st.write("Página de prueba para el ejercicio ¡Hola neurona!.")

st.divider()
tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab3:
    col1, col2, col3 = st.columns(3)

    t3_w0 = col1.slider("Peso w0", value=0.0, min_value=-10.0, max_value=10.0, format="%.2f")
    t3_w1 = col2.slider("Peso w1", value=0.0, min_value=-10.0, max_value=10.0, format="%.2f")
    t3_w2 = col3.slider("Peso w2", value=0.0, min_value=-10.0, max_value=10.0, format="%.2f")

    t3_x0 = col1.number_input("Entrada x0", value=0.0, format="%.2f")
    t3_x1 = col2.number_input("Entrada x1", value=0.0, format="%.2f")
    t3_x2 = col3.number_input("Entrada x2", value=0.0, format="%.2f")

    t3_b = st.number_input("Sesgo b", value=0.0, format="%.2f")

    t3_result = t3_w0 * t3_x0 + t3_w1 * t3_x1 + t3_w2 * t3_x2 + t3_b
    if st.button("Calcular salida (tres entradas y sesgo)"):
        st.write(f"Salida: {t3_result:.2f}")

st.write("© Elías Robles Ruiz - CPIFP Alan Turing")