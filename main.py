import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache_data
def carregarDados(empresa):
    # Carregar os dados históricos da ação
    dados = yf.Ticker(empresa)
    cotacao_acao = dados.history(period="1d", start="2010-01-01", end="2023-10-01")
    cotacao_acao = cotacao_acao[["Close"]]
    return  cotacao_acao

dados=carregarDados("ITUB4.SA")

st.write(""" 
# App preço de ações
O gráfico abaixa representa a evolução do preço das ações do Itaú(ITUB4.SA) e do Bradesco(BBDC3.SA) ao longo dos anos.
""")

st.line_chart(dados, use_container_width=True)
