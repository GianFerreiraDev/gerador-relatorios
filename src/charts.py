"""
Módulo responsável por gerar e salvar os gráficos (PNG) usados no PDF.

Fase 1: gráfico de linha com a evolução mensal (todos os meses disponíveis).
Fase 2: vai adicionar gráfico de barras comparando só os dois últimos meses.
"""

from pathlib import Path
import pandas as pd
import matplotlib

# Backend "Agg" permite gerar PNG sem precisar de display gráfico aberto.
# Essencial pra rodar em servidor, CI ou container sem interface gráfica.
matplotlib.use("Agg")

import matplotlib.pyplot as plt # noqa: E402 (import depois do use("Agg") é proposital)

from src.processor import COLUNA_ANO_MES, COLUNA_TOTAL


def _garantir_pasta_saida(caminho_arquivo: Path) -> None:
    """Cria a pasta de saída (e as pai) caso não exista."""
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)


def gerar_grafico_linha(
        df_mensal: pd.DataFrame,
        caminho_saida: Path,
        titulo: str = "Evolução mensal",
) -> Path:
    """
    Gera um gráfico de linha com a evolução dos totais mensais e salva em PNG.

    Args:
        df_mensal: DataFrame retornado por `processor.agregar_por_mes`
        Deve ter as colunas `ano_mes` (str "YYYY-MM") e `total` (float).
        caminho_saida: caminho completo do arquivo PNG a ser gerado.
        titulo: título do gráfico (opcional).
    
    Returns:
        Path: o mesmo `caminho_saida` (pra facilitar encadeamento no main.py).
    """
    _garantir_pasta_saida(caminho_saida)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        df_mensal[COLUNA_ANO_MES],
        df_mensal[COLUNA_TOTAL],
        marker="o", # bolinha em cada ponto - facilita leitura dos meses
        linewidth=2,
        color="#2563eb", # azul acessível, consistente com a paleta do projeto
    )

    ax.set_title(titulo, fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Mês")
    ax.set_ylabel("Total")

    # Rotaciona os labels do eixo X pra não sobrepor quando tiver muitos meses.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    # Grid sutil só no eixo Y — guia o olho sem poluir.
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.set_axisbelow(True)  # grid fica atrás da linha, não na frente

    # Remove as bordas superior e direita (visual mais limpo, padrão moderno).
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(caminho_saida, dpi=150, bbox_inches="tight")
    plt.close(fig)  # libera memória; sem isso, cada chamada acumula figura

    return caminho_saida
