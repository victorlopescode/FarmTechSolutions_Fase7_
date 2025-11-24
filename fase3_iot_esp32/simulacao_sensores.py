import streamlit as st
import random
import time

def mostrar_iot():
    st.title("🔌 Fase 3 — IoT & Sensores (Simulação)")

    st.markdown(
        """
        Esta tela simula leituras vindas do **ESP32** em tempo real.
        """
    )

    # Controle de atualização automática
    auto = st.checkbox("Atualizar automaticamente (a cada 2 segundos)", value=False)

    # Gerar leituras
    umidade = random.randint(20, 90)
    ph = round(random.uniform(5.5, 7.0), 2)
    nutrientes = random.randint(40, 80)

    col1, col2, col3 = st.columns(3)
    col1.metric("Umidade (%)", umidade)
    col2.metric("pH", ph)
    col3.metric("Nutrientes (unidade)", nutrientes)

    # Mensagem de condição do solo
    if umidade < 30:
        st.warning("Umidade crítica — irrigação recomendada!")
    elif umidade > 80:
        st.info("Solo muito úmido — risco de alagamento.")
    else:
        st.success("Umidade em faixa aceitável.")

    # Se ativado, recarrega página a cada 2 segundos
    if auto:
        time.sleep(2)
        st.rerun()

