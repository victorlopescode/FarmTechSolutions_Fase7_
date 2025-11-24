import streamlit as st
import pandas as pd


def mostrar_status_banco():
    st.title("🗄️ Fase 2 — Banco de Dados Relacional")

    st.markdown(
        """
        Aqui simulamos uma visão das **leituras de sensores** armazenadas no banco de dados.
        Em um cenário real, estes dados viriam de um SGBD (Oracle, PostgreSQL, etc.) via SQL.
        """
    )

    dados = {
        "DATA_HORA": ["2025-11-23 10:00", "2025-11-23 09:55", "2025-11-23 09:50"],
        "UMIDADE": [40, 35, 42],
        "NUTRIENTES": [60, 55, 58],
        "PH": [6.5, 6.2, 6.3],
    }
    df = pd.DataFrame(dados)

    st.subheader("Últimas leituras registradas (simulação)")
    st.dataframe(df, use_container_width=True)
