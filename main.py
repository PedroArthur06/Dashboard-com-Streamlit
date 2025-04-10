import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache_data
def carregarDados(empresas):
    texto_tickers = " ".join(empresas)
    dados = yf.Tickers(texto_tickers)
    cotacao_acao = dados.history(period="1d", start="2010-01-01", end="2023-10-01")
    print(cotacao_acao)
    cotacao_acao = cotacao_acao["Close"]
    return  cotacao_acao

acoes= ["ITUB4.SA", "BBDC3.SA","PETR3.SA", "VALE3.SA", "ITSA4.SA"]
dados=carregarDados(acoes)

st.write(""" 
# App preço de ações
O gráfico abaixa representa a evolução do preço das ações do Itaú(ITUB4.SA) e do Bradesco(BBDC3.SA) ao longo dos anos.
""")

st.line_chart(dados, use_container_width=True)
