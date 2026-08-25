# PROJECT_CONTEXT.md — Gerador de Relatórios

## Objetivo
Projeto de portfólio (GitHub) que processa dados de uma planilha, gera gráficos
comparativos de evolução mensal e exporta um relatório em PDF.

## Stack
- **pandas** + **openpyxl** — leitura de Excel/CSV, agregação por mês
- **matplotlib** — geração dos gráficos (linha + barras)
- **fpdf2** (fork mantido do `fpdf` original — **não** usar o `fpdf` antigo, está abandonado)

## Contrato de dados de entrada
O arquivo de entrada (Excel principal, CSV como fallback) precisa ter, no mínimo:

| Coluna     | Obrigatória | Exemplo         |
|------------|-------------|-----------------|
| `data`     | Sim         | 2026-07-15      |
| `valor`    | Sim         | 1250.00         |
| `categoria`| Não         | "Vendas"        |

Se os nomes das colunas do arquivo real forem diferentes, o mapeamento fica
centralizado em `src/config.py` (ex: `COLUNA_DATA = "Data Lançamento"`).

## Decisões de escopo já tomadas
- **Genérico**: o sistema deve funcionar com qualquer planilha que siga o
  contrato de dados acima, não é amarrado a um domínio específico.
- **Entrada principal: Excel.** CSV entra como fallback simples (pandas lê os
  dois de forma parecida).
- **Entrada via PDF é stretch goal** (fase 4) — extração de tabela de PDF é
  instável e depende de layout; não faz parte do MVP.
- **Comparativo principal: evolução ao longo de vários meses** (série
  temporal), com destaque comparando os dois últimos meses (variação %).
  Comparação por categoria é opcional (fase 3), não faz parte do MVP.

## Estrutura de pastas
```
report-generator/
├── data/input/          # planilhas de exemplo (dados fictícios)
├── src/
│   ├── config.py        # caminhos e nomes de coluna
│   ├── data_loader.py   # lê Excel/CSV, valida colunas
│   ├── processor.py     # agrupa por mês, calcula variação %
│   ├── charts.py        # gera gráfico de linha (evolução) e de barras (últimos 2 meses)
│   └── pdf_report.py    # monta o PDF final
├── output/
│   ├── charts/
│   └── reports/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── PROJECT_CONTEXT.md
└── ROADMAP.md
```

## O que cada módulo faz
- `data_loader.py`: lê o Excel/CSV, valida se as colunas obrigatórias existem,
  converte `data` para datetime.
- `processor.py`: extrai `ano_mes` de cada linha, agrupa e soma `valor` por
  mês, calcula variação % entre o último e o penúltimo mês.
- `charts.py`: gera e salva `.png` — gráfico de linha com todos os meses
  disponíveis, e gráfico de barras comparando só os 2 últimos meses.
- `pdf_report.py`: monta o PDF com resumo textual (total do mês atual,
  variação % vs mês anterior), os gráficos e uma tabela mês a mês.

## Status atual
Projeto ainda não iniciado — apenas escopo e arquivos de contexto criados.
Próximo passo: MVP (fase 1 do ROADMAP.md).
