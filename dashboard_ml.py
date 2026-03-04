
import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Dashboard BI + ML", page_icon="logo-icone.ico", layout="wide")

st.markdown(
"""
<style>
.stApp{
background-color:#0a1f44;
color:white;
}
</style>
""", unsafe_allow_html=True)

st.image("logo-icone.ico", width=200)

st.title("Dashboard BI com Machine Learning")

df = pd.read_csv("dados_vendas.csv")

faturamento = df["valor"].sum()
qtd = df["quantidade"].sum()

col1,col2 = st.columns(2)

col1.metric("Faturamento Total", f"R$ {faturamento}")
col2.metric("Quantidade Vendida", qtd)

st.subheader("Vendas por Produto")
st.bar_chart(df.groupby("produto")["valor"].sum())

st.subheader("Previsão de Vendas")

mes = st.slider("Mês",1,12,6)
quantidade = st.slider("Quantidade esperada",1,10,3)

try:
    with open("modelo_vendas.pkl","rb") as f:
        modelo = pickle.load(f)

    previsao = modelo.predict([[mes,quantidade]])

    st.success(f"Previsão de faturamento: R$ {round(previsao[0],2)}")

except:
    st.warning("Treine o modelo primeiro executando: python treinar_modelo.py")
