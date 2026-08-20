# Master Hub v12 — Especificação funcional aplicada

Versão funcional construída a partir da v11 integrada, usando a especificação `ESPECIFICACAO_FUNCIONAL_MASTER_HUB_V12.md` como fonte de verdade.

## Escopo reformulado na v12
- Faturamento: Visão Geral, Guias, Clientes, Lojas e Segmentos.
- Crédito: Visão Geral, Clientes e Guias.
- Limite Extra: Visão Geral, Movimentações, Clientes e Guias.
- Faixas: Visão Geral e Clientes, com Evolução incorporada.

## Preservado para Fase 2
- Visão Executiva.
- Cliente 360.

## Base fictícia reaproveitada da v11
- 96 clientes
- 24 Guias
- 8 RPs
- 30 lojas
- 10 segmentos
- 3.828 faturamentos
- 522 movimentações de Limite Extra
- 2.304 snapshots de Crédito
- 2.304 posições mensais de Faixa

## Regras compartilhadas
A v12 centraliza funções de faturamento, distinct count de faturamentos, posição de Crédito, Limite Extra atual, Risco Total, Inadimplência, Status Comercial e Faixas para evitar divergência entre módulos.

Crédito continua sendo um cenário demonstrativo baseado nas regras vigentes da v11 e não constitui política automática de aprovação.

## QA final

Veja `QA_V12.md`. As suítes finais foram executadas em Chromium e validaram Faturamento, Crédito, Limite Extra, Faixas, Fase 2 preservada, invariantes cruzados, exportação e responsividade.
