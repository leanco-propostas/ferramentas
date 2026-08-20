# Master Hub v12 — Relatório de QA e Aceite

## Base fictícia integrada

- Clientes: **96**
- Guias: **24**
- Rps: **8**
- Lojas: **30**
- Segmentos: **10**
- Faturamentos: **3.828**
- Classificacoes: **768**
- Movimentos Limite Extra: **522**
- Snapshots Credito: **2.304**
- Posicoes Faixa: **2.304**

## Resultado geral

- Sintaxe JavaScript: PASS (`node --check`).
- Inicialização em Chromium: PASS.
- Erros JavaScript nas suítes finais: **0**.
- Overflow global 1366×768: **0 px**.
- Overflow global 768×1024: **0 px**.
- Overflow global 390×844: **0 px**.
- Exportação CSV: PASS.
- Exportação Excel compatível (.xls): PASS.

## Critérios globais da especificação

- [x] Menu lateral retrátil preservado.
- [x] Cliente 360 e Visão Executiva acessíveis e preservados para Fase 2.
- [x] Faturamento com 5 páginas independentes.
- [x] Lojas e Segmentos separados.
- [x] 14 páginas reformuladas com filtros expansíveis e cards executivos.
- [x] Comparações exibem datas/metodologia.
- [x] Indicadores calculados possuem rótulos/ajuda contextual.
- [x] ABC com Representatividade + Acumulado + Curva e ★ A em destaque.
- [x] Status comercial usa texto + ícone + cor.
- [x] Entidades clicáveis abrem Drawer contextual.
- [x] Métricas de Crédito/Extra compartilhadas fecham entre módulos.
- [x] Estados sem dado usam `—` onde aplicável.

## Faturamento

- [x] Visão Geral: comparação explícita e concentração Clientes/Guias/Lojas/Segmentos.
- [x] Guias: colunas obrigatórias, histórico, Crédito agregado da carteira e Top 10 Clientes no Drawer.
- [x] Clientes: Resumida/Detalhada; primeira/última compra, dias, intervalo e inadimplência; Crédito completo no Drawer.
- [x] Lojas: página independente e Drawer com Top 10 Clientes/Guias.
- [x] Segmentos: página independente e Drawer com Lojas/Clientes/Guias.

## Crédito

- [x] Crédito e Limite Extra permanecem separados.
- [x] Limite Total = Limite Normal + Limite Extra.
- [x] Risco Total = Aberto + Recente no cenário vigente da V11.
- [x] Filtros avançados.
- [x] Distribuição de saturação clicável.
- [x] Maiores riscos alterna Clientes/Guias.
- [x] Faturamento 3m/6m/12m e média mensal.
- [x] Limite/compra média e Em aberto/compra média exibidos como razão `×`.
- [x] Drawer do Guia com principais Clientes e contexto de risco.

## Limite Extra

- [x] Visão Geral preserva a essência e evita tabela completa de Clientes duplicada.
- [x] Efeito após aumento em destaque com metodologia explícita.
- [x] Dois meses-calendário completos antes/depois, total e média.
- [x] Variação absoluta e percentual apenas quando a janela pós-evento está completa.
- [x] **68 eventos** da base de teste possuem janela pós-aumento incompleta e **0** deles recebe delta/média pós como se a janela estivesse completa.
- [x] Outras movimentações dentro da janela são sinalizadas.
- [x] Movimentações com filtros/cards.
- [x] Drawer de Cliente lista todas as movimentações do período; caso testado: 4 esperadas / 4 exibidas.
- [x] Drawer de Guia mostra Clientes e origem da variação.

## Faixas

- [x] Apenas Visão Geral + Clientes.
- [x] Evolução incorporada a Clientes.
- [x] Visão Geral sem tabela completa duplicada.
- [x] Faixa inicial/final explicitadas.
- [x] Migração por Nº de Clientes ou Faturamento.
- [x] Tabela única Resumida/Detalhada.
- [x] Drawer com trajetória mensal, faturamento e Crédito/Risco.

## Observações de escopo

- Visão Executiva e Cliente 360 foram deliberadamente preservados sem reformulação profunda, conforme Fase 2 da especificação.
- Crédito continua sendo um cenário demonstrativo baseado nas regras vigentes da V11; a v12 melhora explicabilidade e integração, mas não cria score ou motor automático de aprovação.
