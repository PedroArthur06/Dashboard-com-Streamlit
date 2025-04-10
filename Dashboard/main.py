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

@st.cache_data
def carregar_acoes():
    base_tickers = pd.read_csv("IBOV.csv", sep=";")
    tickers = list(base_tickers["Código"])
    tickers = [item + ".SA" for item in tickers]
    return tickers

acoes = carregar_acoes()
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

texto_perf= ""

if len (lista_acoes) == 0:
    lista_acoes = list(dados.columns)

for acao in lista_acoes:
    performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
    performance_ativo = float(performance_ativo)
    texto_perf = texto_perf + f" \n{acao}: {performance_ativo:.1%} \n"


st.write(f""" 
### Performace dos ativos
Essa foi a performace de cada ativo no período selecionado:
         
{texto_perf}
""")
