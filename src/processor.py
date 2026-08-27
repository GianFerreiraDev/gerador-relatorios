"""
Módulo responsável por transformar os dados brutos carregados pelo
data_loader em agregações úteis para os gráficos e o relatório final (PDF).

Fase 1: agrega `valor` por mês (ano_mês), retornando o total de cada mês.
Fase 2: vai adicionar cálculo de variação % entre os dois últimos meses.
Fase 3: vai adicionar agregação por categoria, retornando total por categoria.
Fase 4: vai adicionar suporte a CSV, além de Excel.
"""
import pandas as pd

from src.config import COLUNA_DATA, COLUNA_VALOR

# Nome da coluna auxiliar que representa o "bucket" mensal (formato "YYYY-MM")
COLUNA_ANO_MES = "ano_mes"

# Nome da coluna final que guarda o valor agregado de cada mês
COLUNA_TOTAL = "total"


def agregar_por_mes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa os valores por mês (ano-mês) e retorna o total de cada mês,
    ordena do mais antigo para o mais recente.
    
    Args:
        df: DataFrame retornando por `data_loader.carregar_dados`.
        Precisa ter, no mínimo, as colunas `data` (datetime) e `valor`.

    Returns:
        df: DataFrame com duas colunas:
            - `ano_mes` (str no formato "YYYY-MM")
            - `total` (float com a soma dos valores daquele mês)
    
    Exemplo de retorno:
            ano_mes    total
        0   2026-01    1250.00
        1   2026-02    1830.50
        2   2026-03    2410.75
    """
    # Cópia pra não mutar o DataFrame original (boa prática com pandas)
    dados = df.copy()

    # Cria coluna auxiliar no formato "YYY-MM" (ano-mês) usando o acessor .dt do pandas.
    # .dt.strftime é o jeito idiomático de formatar datetime pra string.
    dados[COLUNA_ANO_MES] = dados[COLUNA_DATA].dt.strftime("%Y-%m")

    # Agrupa por mês e soma o valor. as_index=False mantém `ano_mes` como coluna
    # em vez de virar índice do DataFrame resultante (mais prático pro resto).
    agregado = (
        dados
        .groupby(COLUNA_ANO_MES, as_index=False)[COLUNA_VALOR]
        .sum()
    )

    # Renomeia a coluna de valor "total" - fica mais semântico    # ("valor" faz sentido na linha crua, "total" faz sentido na linha agrupada)
    agregado = agregado.rename(columns={COLUNA_VALOR: COLUNA_TOTAL})

    # Ordena por mês ascendente (string "YYYY-MM" ordena certinho como cronologia)
    agregado = agregado.sort_values(COLUNA_ANO_MES).reset_index(drop=True)

    return agregado
