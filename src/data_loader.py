"""
Módulo responsável por carregar o arquivo de entrada (Excel/CSV) e validar
que ele respeita o contrato de dados definido em src/config.py.

Por enquanto (Fase 1 do ROADMAP) só lê Excel. Suporte a CSV entra na fase 4.
"""

from pathlib import Path
import pandas as pd

from src.config import (
    CAMINHO_INPUT,
    ARQUIVO_INPUT_PADRAO,
    COLUNA_DATA,
    COLUNA_VALOR,
    COLUNA_CATEGORIA,
)


def _resolver_caminho(caminho_arquivo: str | None) -> Path:
    """
    Resolve o caminho final do arquivo de entrada.
    
    - Se `caminho_arquivo` for None, usa o arquivo padrão dentro de CAMINHO_INPUT.
    - Se for um caminho relativo, interpreta como relativo à raiz do projeto.
    
    Returns:
        Path: caminho absoluto do arquivo.
    
    Raises:
        FileNotFoundError: se o arquivo não existir no caminho resolvido.
    """

    if caminho_arquivo is None:
        caminho = CAMINHO_INPUT / ARQUIVO_INPUT_PADRAO
    else:
        caminho = Path(caminho_arquivo)
        # Se for relativo, ancora na raiz do projeto (não no cwd do terminal)
        if not caminho.is_absolute():
            from src.config import RAIZ_PROJETO
            caminho = RAIZ_PROJETO / caminho

    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo de entrada não encontrado: {caminho}\n"
            f"Verifique se o arquivo existe e se o caminho está correto."
        )

    return caminho


def _validar_colunas(df: pd.DataFrame) -> None:
    """
    Garante que o DataFrame tem as colunas obrigatórias do contrato.
    
    A coluna `categoria` é opcional - sua ausência não levanta erro.
    
    Raises:
        ValueError: listando as colunas obrigatórias que estão faltando.
    """
    colunas_obrigatorias = [COLUNA_DATA, COLUNA_VALOR]
    faltando = [c for c in colunas_obrigatorias if c not in df.columns]

    if faltando:
        raise ValueError(
            f"Colunas obrigatórias ausentes no arquivo: {faltando}\n"
            f"Colunas encontradas: {list(df.columns)}\n"
            f"Esperado no mínimo: {colunas_obrigatorias}\n"
            f"Se os nomes forem diferentes, ajuste as constantes src/config.py."
        )


def carregar_dados(caminho_arquivo: str | None = None) -> pd.DataFrame:
    """
    Carrega o arquivo de entrada e devolve um DataFrame validado.
    - Lê Excel (.xlsx) usando openpyxl como engine.
    - Valida que as colunas obrigatórias (`data`, `valor`) existem.
    - Converte a coluna `data` para datetime (falha alto se vier dado inválido).

    Args:
        caminho_arquivo: caminho do arquivo. Se None, usa o padrão de config.

    Returns:
        pd.DataFrame: dados carregados, com a coluna `data` já em datetime.

    Raises:
        FileNotFoundError: se o arquivo não existir.
        ValueError: se falta coluna obrigatória ou a data for inválida.
    """
    caminho = _resolver_caminho(caminho_arquivo)

    # engine="openpyxl" é explicito pra deixar claro que dependemos dele.
    # Se um dia o arquivo vier .xls antigo, vai falhar alto aqui (bom sinal).
    df = pd.read_excel(caminho, engine="openpyxl")

    _validar_colunas(df)

    # Converte a coluna de data. errors="raises" joga exceção se tiver data
    # inválida (ex: "abc" ou string mal formatada), em vez de virar Nat silencioso.
    df[COLUNA_DATA] = pd.to_datetime(df[COLUNA_DATA], errors="raises")

    return df
