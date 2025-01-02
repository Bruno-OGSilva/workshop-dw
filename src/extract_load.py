# import
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# import var de ambiente

commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata

def buscar_dados_commodities(simbolo, periodo='5d', intervalo="1d"):
    ticker = yf.Ticker('CL=F')
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo  # Adiciona a coluna do símbolo
    return dados

def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)  # Concatena todos os dados em um único DataFrame

# pegar a cotacao dos ativos


# concatenar os meus ativos  (1..2...3) -> (1)


# salvar no banco de dados

if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    print(dados_concatenados)
    #salvar_no_postgres(dados_concatenados, schema='public')