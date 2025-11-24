import streamlit as st
import random
from fase5_cloud_aws.aws_alerts import send_alert


def analisar_imagem_fake():
    """
    Simula o resultado de um modelo de visão computacional.
    Retorna (classe, risco) onde risco = 1 se crítico.
    """
    classes = [
        ("Planta saudável", 0),
        ("Praga detectada", 1),
        ("Doença foliar", 1),
        ("Planta com deficiência nutricional", 1),
    ]
    return random.choice(classes)


def mostrar_visao_computacional():
    st.title("👁️ Fase 6 — Visão Computacional (Simulada)")

    st.markdown(
        """
        Esta seção simula a Fase 6, em que um modelo de visão computacional
        (por exemplo, YOLO ou uma CNN) analisa imagens da plantação para
        detectar **pragas, doenças ou problemas de crescimento**.
        """
    )

    uploaded = st.file_uploader("Envie uma imagem da plantação", type=["jpg", "jpeg", "png"])
    if uploaded is not None:
        st.image(uploaded, caption="Imagem enviada", use_container_width=True)

        if st.button("Analisar imagem (simulação)"):
            classe, risco = analisar_imagem_fake()

            if risco == 1:
                st.error(f"Resultado: {classe}")
                if st.checkbox("Enviar alerta AWS (simulado)"):
                    send_alert(f"[Visão Computacional] {classe} detectada na lavoura.")
                    st.success("Alerta 'enviado' (simulação, ver console).")
            else:
                st.success(f"Resultado: {classe}")
