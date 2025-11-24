import os
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


@st.cache_resource
def treinar_modelo_sintetico():
    """
    Gera um dataset sintético de umidade/temperatura e treina
    um RandomForest para decidir se deve irrigar (1) ou não (0).
    Regra usada para gerar o rótulo:
    - irrigar = 1 se umidade < 40 e temperatura > 22
    """
    rng = np.random.RandomState(42)
    n = 10000
    umidade = rng.randint(10, 95, size=n)
    temperatura = rng.randint(10, 40, size=n)
    irrigar = ((umidade < 40) & (temperatura > 22)).astype(int)

    df = pd.DataFrame(
        {"umidade": umidade, "temperatura": temperatura, "irrigar": irrigar}
    )

    X = df[["umidade", "temperatura"]]
    y = df["irrigar"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    acuracia = modelo.score(X_test, y_test)

    return modelo, df, acuracia


def mostrar_dashboard_fase4():
    st.title("🤖 Fase 4 — Dashboard & Machine Learning (Irrigação)")

    st.markdown(
        """
        Esta seção utiliza um modelo de Machine Learning (**RandomForest**) treinado em
        dados sintéticos para sugerir **se é necessário irrigar ou não** com base em
        umidade do solo e temperatura ambiente.
        """
    )

    modelo, df, acuracia = treinar_modelo_sintetico()

    with st.expander("Ver amostra dos dados de treinamento"):
        st.dataframe(df.head(), use_container_width=True)
        st.write(f"Acurácia em teste (dados sintéticos): **{acuracia:.2f}**")

    col1, col2 = st.columns(2)
    with col1:
        umidade = st.slider("Umidade do solo (%)", 0, 100, 50)
    with col2:
        temperatura = st.slider("Temperatura ambiente (°C)", 0, 50, 25)

    entrada = [[umidade, temperatura]]
    pred = modelo.predict(entrada)[0]
    prob = modelo.predict_proba(entrada)[0][pred]

    if pred == 1:
        st.success(
            f"Recomendação do modelo: **IRRIGAR** (confiança ~ {prob * 100:.1f}%)"
        )
    else:
        st.info(
            f"Recomendação do modelo: **NÃO IRRIGAR** (confiança ~ {prob * 100:.1f}%)"
        )
