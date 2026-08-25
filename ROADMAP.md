# ROADMAP.md — Gerador de Relatórios

Marque `[x]` conforme for concluindo. Cada fase deve ficar funcional antes de
passar pra próxima.

## Fase 1 — MVP
- [ ] `data_loader.py`: ler Excel de exemplo, validar colunas `data` e `valor`
- [ ] `processor.py`: agrupar `valor` por mês (`ano_mes`)
- [ ] `charts.py`: gerar gráfico de linha com a evolução mensal
- [ ] `pdf_report.py`: montar PDF simples com resumo + gráfico de linha
- [ ] `main.py`: rodar o fluxo completo ponta a ponta

## Fase 2 — Comparação dos últimos 2 meses
- [ ] Calcular variação % entre o último mês e o penúltimo
- [ ] `charts.py`: gerar gráfico de barras só com os 2 últimos meses
- [ ] Incluir a variação % e o gráfico de barras no PDF

## Fase 3 — Categoria (opcional)
- [ ] Suporte à coluna `categoria` (quando presente no arquivo)
- [ ] Gráfico de breakdown por categoria no último mês

## Fase 4 — Generalização da entrada
- [ ] Suporte a CSV como alternativa ao Excel
- [ ] Mapeamento de nomes de coluna configurável em `config.py`

## Fase 5 — Stretch: entrada via PDF
- [ ] Avaliar `pdfplumber` para extração de tabela
- [ ] Documentar limitações (depende do layout do PDF de origem)

## Fase 6 — CLI
- [ ] `argparse`: escolher arquivo de entrada e mês de referência via linha de comando

## Fase 7 — Polimento
- [ ] README com prints do PDF gerado e instruções de uso
- [ ] Testes básicos com `pytest` (`processor.py` é prioridade — lógica pura, fácil de testar)
- [ ] Dados de exemplo fictícios em `data/input/` para quem for rodar o projeto

## Notas de sessão
(Use esta seção para anotar decisões tomadas durante o desenvolvimento com o
Claude Code, bugs encontrados, ou mudanças de escopo.)
