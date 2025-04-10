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

st.sidebar.header("Filtros")

# Filtragem das ações
lista_acoes= st.sidebar.multiselect("Escolha as ações para visualizar",dados.columns)
if lista_acoes:
    dados= dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns = {acao_unica: "Close"})

# Filtro de datas
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_datas = st.sidebar.slider("Selecione o período", min_value= data_inicial, max_value= data_final, value= (data_inicial, data_final))

dados = dados.loc[intervalo_datas[0]: intervalo_datas[1]]

# Filtro de preço


st.line_chart(dados)
