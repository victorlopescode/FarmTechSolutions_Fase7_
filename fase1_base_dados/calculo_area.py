import streamlit as st
import pandas as pd
from .manejo_insumos import calcular_insumos


def mostrar_fase1():
    st.title("🌱 Fase 1 — Cálculo de Área e Insumos")

    st.markdown(
        """
        Nesta fase calculamos a **área de plantio** e estimamos
        os **insumos necessários** para a cultura selecionada.
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        largura = st.number_input("Largura do terreno (m)", min_value=1.0, value=20.0)
    with col2:
        comprimento = st.number_input("Comprimento do terreno (m)", min_value=1.0, value=50.0)

    cultura = st.selectbox("Cultura", ["Soja", "Milho", "Trigo", "Outro"])

    area = largura * comprimento
    st.metric("Área total (m²)", f"{area:.2f}")

    insumos = calcular_insumos(area_m2=area, cultura=cultura)

    df_insumos = pd.DataFrame(
        [
            ["Sementes", insumos["sementes_kg"], "kg"],
            ["Fertilizante", insumos["fertilizante_kg"], "kg"],
            ["Água", insumos["agua_litros"], "L"],
        ],
        columns=["Item", "Quantidade", "Unidade"],
    )

    st.subheader("Planejamento de Insumos (estimado)")
    st.dataframe(df_insumos, use_container_width=True)
