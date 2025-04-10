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

acoes= ["ITUB4.SA", "BBDC3.SA","PETR3.SA", "VALE3.SA", "ITSA4.SA", "ABEV3.SA", "MGLU3.SA"]
dados=carregarDados(acoes)

st.write(""" 
# App preço de ações
O gráfico abaixa representa a evolução do preço das ações ao longo dos anos.
""")

# Filtragem das ações
lista_acoes= st.multiselect("Escolha as ações para visualizar",dados.columns)
if lista_acoes:
    dados= dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns = {acao_unica: "Close"})


st.line_chart(dados)
