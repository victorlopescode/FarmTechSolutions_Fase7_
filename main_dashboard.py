import streamlit as st

from fase1_base_dados.calculo_area import mostrar_fase1
from fase2_banco_dados.conexao_db import mostrar_status_banco
from fase3_iot_esp32.simulacao_sensores import mostrar_iot
from fase4_dashboard_ml.Dashboard import mostrar_dashboard_fase4
from fase5_cloud_aws.aws_alerts import send_test_alert
from fase6_vision.yolo_inferencia import mostrar_visao_computacional

st.set_page_config(
    page_title="FarmTech Solutions - Fase 7",
    page_icon="🌾",
    layout="wide"
)

st.sidebar.title("Navegação")
pagina = st.sidebar.radio(
    "Escolha a Fase/Serviço:",
    [
        "Visão Geral",
        "Fase 1 - Base de Dados & Insumos",
        "Fase 2 - Banco de Dados",
        "Fase 3 - IoT & Sensores",
        "Fase 4 - Dashboard & ML",
        "Fase 5 - Cloud & Alertas",
        "Fase 6 - Visão Computacional"
    ]
)

if pagina == "Visão Geral":
    st.title("🌾 FarmTech Solutions - Sistema Integrado (Fase 7)")
    st.markdown(
        """
        Este painel integra todas as fases do projeto **FarmTech Solutions**:

        - **Fase 1** – Cálculo de área de plantio e insumos
        - **Fase 2** – Banco de dados relacional (simulado)
        - **Fase 3** – IoT com ESP32 e sensores (simulado)
        - **Fase 4** – Dashboard com Machine Learning (Scikit-Learn)
        - **Fase 5** – Cloud Computing na AWS com serviço de alertas (SNS - simulado)
        - **Fase 6** – Visão computacional (YOLO/CNN simulados)
        """
    )

elif pagina == "Fase 1 - Base de Dados & Insumos":
    mostrar_fase1()

elif pagina == "Fase 2 - Banco de Dados":
    mostrar_status_banco()

elif pagina == "Fase 3 - IoT & Sensores":
    mostrar_iot()

elif pagina == "Fase 4 - Dashboard & ML":
    mostrar_dashboard_fase4()

elif pagina == "Fase 5 - Cloud & Alertas":
    st.title("☁️ Fase 5 – Cloud & Alertas (AWS SNS)")
    st.markdown(
        """
        Aqui simulamos o envio de alertas usando AWS SNS.

        Em produção, esta função seria integrada com o `boto3` e um tópico SNS real.
        """
    )
    if st.button("Disparar alerta de teste"):
        send_test_alert()
        st.success("Alerta de teste 'enviado' (simulação local, ver console de logs).")

elif pagina == "Fase 6 - Visão Computacional":
    mostrar_visao_computacional()

