"""
Condigurações centrais do projeto.

Centraliza caminhos de pastas e nomes de coluna do arquivo de entrada.
Se a planilha real estiver nomes de coluna diferentes do contrato padrão,
basta ajustar as contantes `COLUNA_*` aqui, o resto do codigo não muda.
"""

from pathlib import Path

# -----------------------------------------------------------------------------
# Caminhos de pastas
# -----------------------------------------------------------------------------# Pasta raiz do projeto (assume que este arquivo está em src/, então sobe um nível.)
# Path(__file__).resolve().parent.parent aponta para a raiz independente de
# onde o script for executado.
RAIZ_PROJETO = Path(__file__).resolve().parent.parent

# Pasta com as planilhas de entrada (Excel/CSV de exemplo)
CAMINHO_INPUT = RAIZ_PROJETO / "data" /"input"

# Pasta onde os PDFs gerados serão salvos
CAMINHO_OUTPUT_REPORTS = RAIZ_PROJETO / "output" / "reports"

# Pasta onde os gráficos (PNG) gerados serão salvos temporariamente
CAMINHO_OUTPUT_CHARTS = RAIZ_PROJETO / "output" / "charts"

# -----------------------------------------------------------------------------
# Arquivo de entrada padrão
# -----------------------------------------------------------------------------

# Nome de arquivo Excel que será usado quando main.py rodar sem argumentos.
# Fase 6 (CLI) vai permitir trocar isso via linha de comando.
ARQUIVO_INPUT_PADRAO = "exemplo.xlsx"

# -----------------------------------------------------------------------------
# Contrato de dados - nomes de colunas no arquivo de entrada
# -----------------------------------------------------------------------------

# Coluna obrigatória com a data do registro (será convertida para datetime)
COLUNA_DATA = "data"

# Coluna Obrigatória com o valor numérico (float) do registro
COLUNA_VALOR = "valor"

# Coluna opcional com a categoria do registro (fase 3 do roadmap)
COLUNA_CATEGORIA = "categoria"

