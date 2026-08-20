# MASTER HUB — ESPECIFICAÇÃO FUNCIONAL E DE EXPERIÊNCIA V12

**Versão do documento:** 1.0  
**Data de consolidação:** 19/08/2026  
**Objetivo:** servir como fonte de verdade para o desenvolvimento da V12 do Master Hub a partir da V11.  
**Escopo principal da rodada:** Faturamento, Crédito, Limite Extra e Faixas.  
**Fora do escopo de reformulação nesta rodada:** Cliente 360 e Visão Executiva.

---

## 0. COMO USAR ESTE DOCUMENTO

Este documento deve ser utilizado junto com o pacote/código da **V11**. A V12 não deve ser construída do zero ignorando a versão atual: a orientação é **preservar o que já funciona bem na V11 e aplicar integralmente as alterações descritas aqui**.

### Hierarquia em caso de conflito

1. Esta especificação funcional V12.
2. Decisões explícitas registradas na conversa de validação da V11.
3. Comportamentos e regras existentes na V11 que não foram alterados por esta especificação.
4. Decisões técnicas de implementação que preservem o objetivo funcional e a experiência descrita aqui.

### Legenda de decisão

- **[OBRIGATÓRIO]** requisito explicitamente definido para a V12.
- **[DECISÃO V12]** decisão de projeto tomada para fechar uma lacuna e tornar a implementação objetiva.
- **[PRESERVAR V11]** elemento atual considerado adequado e que não deve ser removido sem necessidade técnica.
- **[FASE 2]** item deliberadamente postergado.

### Princípio central da V12

A V12 deve deixar de ser apenas um conjunto de telas com dados e evoluir para uma ferramenta gerencial de leitura rápida e aprofundamento progressivo.

A estrutura mental da aplicação será:

> **Filtrar → compreender o cenário → identificar exceções/oportunidades → aprofundar no detalhe → tomar decisão.**

Por isso, os principais módulos devem seguir um padrão consistente:

1. filtros;
2. cards executivos;
3. visualizações ou análises intermediárias;
4. tabela principal;
5. drawer lateral direito para aprofundamento contextual.

---

# 1. ESCOPO DA V12

## 1.1 Módulos que serão reformulados nesta rodada

**[OBRIGATÓRIO]**

- Faturamento
- Crédito
- Limite Extra
- Faixas

## 1.2 Módulos que permanecem acessíveis, mas sem reformulação

**[FASE 2]**

- Cliente 360
- Visão Executiva

Os dois módulos devem **continuar visíveis e clicáveis no menu lateral**, preservando o funcionamento atual da V11. O objetivo é não perdê-los de vista e trabalhar uma reformulação dedicada posteriormente.

Não realizar nesta V12 uma tentativa superficial de redesenhar Cliente 360 ou Visão Executiva. Esses módulos merecem uma rodada própria de arquitetura, conteúdo e experiência.

---

# 2. ARQUITETURA GLOBAL E NAVEGAÇÃO

## 2.1 Menu lateral esquerdo

**[PRESERVAR V11]**

O menu lateral esquerdo retrátil/expansível da V11 foi aprovado.

Requisitos:

- manter o comportamento de recolher e expandir;
- manter a organização por módulos;
- não transformar o menu em navegação superior;
- manter Cliente 360 e Visão Executiva acessíveis;
- preservar a sensação de ganho de área útil quando recolhido.

## 2.2 Padrão de navegação interna dos módulos

**[DECISÃO V12]**

Cada módulo pode possuir subpáginas/abas, porém a navegação deve ter comportamento consistente. O usuário deve saber em qual módulo e página está sem precisar interpretar o conteúdo.

Recomendação de hierarquia visual:

- título do módulo;
- nome da página/subpágina;
- pequena descrição funcional quando necessário;
- filtros;
- conteúdo.

Evitar excesso de breadcrumbs, títulos redundantes e barras que consumam altura sem gerar contexto.

---

# 3. PADRÃO GLOBAL DE PÁGINA

## 3.1 Ordem estrutural

**[OBRIGATÓRIO]**

Nas páginas analíticas de Faturamento, Crédito, Limite Extra e Faixas, adotar a seguinte ordem sempre que aplicável:

1. Cabeçalho da página
2. Área de filtros
3. Linha de cards executivos
4. Gráficos/resumos analíticos
5. Tabela principal
6. Drawer de detalhe ao clicar em entidade

A previsibilidade estrutural deve reduzir a curva de aprendizagem da ferramenta.

---

# 4. FILTROS — PADRÃO EXPANSÍVEL

## 4.1 Conceito

**[OBRIGATÓRIO]**

Os filtros atuais ocupam espaço demais quando todos estão visíveis e, ao mesmo tempo, faltam filtros avançados em algumas páginas. A V12 deve resolver os dois problemas com **filtros em dois níveis**:

### Nível 1 — filtros principais

Ficam sempre visíveis.

### Nível 2 — filtros adicionais

Ficam recolhidos por padrão e são exibidos ao clicar em:

- **Mais filtros**
- quando aberto, o mesmo controle muda para **Menos filtros**

O bloco expandido deve crescer verticalmente de forma organizada, sem abrir modal.

## 4.2 Comportamentos obrigatórios

**[OBRIGATÓRIO]**

- mostrar claramente filtros ativos;
- permitir limpar filtros;
- preservar os filtros ao alternar páginas dentro do mesmo módulo sempre que a dimensão for compatível;
- não esconder silenciosamente um filtro ativo quando o bloco “Mais filtros” estiver recolhido — utilizar um indicador de quantidade, chip ou marcador visual;
- evitar controles excessivamente altos;
- manter a área de filtros mais estreita/compacta do que na V11.

## 4.3 Filtros globais recomendados

**[DECISÃO V12]**

Nem todo filtro precisa aparecer em toda página. Disponibilizar apenas dimensões existentes e aplicáveis àquele contexto.

Possíveis filtros:

- Período
- Cliente
- Guia atual
- Guia da venda, quando diferente de guia atual
- Loja
- Segmento
- Categoria
- Faixa
- Curva ABC
- Status comercial
- RP
- Carteira
- Situação de inadimplência
- Faixa de saturação de crédito
- Possui limite extra: sim/não
- Faixa de faturamento

## 4.4 Comparação de períodos

**[OBRIGATÓRIO]**

Nenhum card ou gráfico poderá usar termos vagos como:

- “janela anterior”
- “período anterior” sem explicar qual período
- “delta” sem dizer o que está sendo comparado

**[DECISÃO V12]**

Sempre que houver comparação, mostrar de forma explícita no componente ou tooltip:

> **Período atual:** DD/MM/AAAA a DD/MM/AAAA  
> **Comparação:** DD/MM/AAAA a DD/MM/AAAA

Quando tecnicamente viável, incluir seletor:

- Período imediatamente anterior de mesma duração
- Mesmo período do ano anterior
- Sem comparação

Se a V11 possuir regra diferente que seja crítica ao negócio, preservá-la, mas **explicá-la explicitamente na interface**.

---

# 5. CARDS EXECUTIVOS

## 5.1 Função dos cards

**[OBRIGATÓRIO]**

Os cards não devem existir apenas como decoração. Eles devem responder em poucos segundos:

- qual é o tamanho do cenário filtrado;
- o que está mudando;
- onde há risco;
- onde há concentração;
- qual indicador merece aprofundamento.

## 5.2 Regras

- títulos curtos;
- valores com formatação pt-BR;
- comparação claramente definida;
- tooltip para fórmula ou conceito não óbvio;
- evitar mais de 6 cards na mesma linha visual em desktop;
- priorizar indicadores realmente relacionados à página.

---

# 6. TABELAS — PADRÃO GLOBAL

## 6.1 Resumo x detalhado

**[OBRIGATÓRIO quando houver muitas colunas]**

Utilizar controle:

- **Resumida**
- **Detalhada**

O objetivo é impedir que a análise principal vire uma planilha horizontal excessivamente densa.

## 6.2 Interação

**[DECISÃO V12]**

- cabeçalho fixo durante rolagem;
- ordenação por colunas relevantes;
- primeira coluna de identificação fixável/sticky quando houver rolagem horizontal;
- nomes de Cliente, Guia, Loja e Segmento devem parecer clicáveis;
- ao clicar no nome, abrir drawer lateral direito;
- filtros/ordenação não devem ser perdidos ao abrir/fechar drawer;
- evitar abrir nova página para detalhes que podem ser consultados no drawer.

## 6.3 Formatação

- Moeda: `R$ 123.456,78`
- Percentual: preferencialmente 1 casa decimal quando não houver necessidade de maior precisão
- Datas: `dd/mm/aaaa`
- Contagens: número inteiro
- Dias: ex. `34 dias`

---

# 7. LINGUAGEM, COPY E EXPLICABILIDADE

## 7.1 Capitalização

**[OBRIGATÓRIO]**

Evitar palavras inteiras em caixa alta.

Padrão preferido:

- “Ativo”
- “Atenção”
- “Inativo”
- “Faturamento”
- “Representatividade”

Siglas e classificações cuja natureza exige letra maiúscula podem permanecer, por exemplo: A, B, C, RP, ABC.

## 7.2 Indicadores calculados

**[OBRIGATÓRIO]**

Todo indicador cujo significado não seja evidente deve possuir pelo menos uma das seguintes soluções:

- subtítulo;
- tooltip;
- ícone de informação;
- microcopy explicativa;
- rótulo mais descritivo.

Nunca deixar “Δ”, “variação”, “janela anterior”, “recente”, “risco” ou similares sem definição acessível ao usuário.

---

# 8. PADRÃO VISUAL PARA CURVA ABC

## 8.1 Aplicação

**[OBRIGATÓRIO]**

As tabelas de:

- Guias
- Clientes
- Lojas
- Segmentos

no módulo Faturamento devem conter:

- Faturamento
- Representatividade
- Acumulado
- Curva ABC

## 8.2 Representação visual

**[OBRIGATÓRIO]**

A classificação ABC deve ser legível por texto, cor e ícone, não somente por cor.

**[DECISÃO V12]**

Sugestão visual:

- **★ A** — verde, maior destaque
- **◆ B** — cor secundária moderada
- **● C** — tom neutro/cinza

A classe A deve possuir o destaque mais evidente, conforme solicitado.

**Importante:** não alterar os thresholds/regras matemáticas atuais da curva ABC da V11 sem necessidade. Se a regra atual estiver configurada, preservá-la. Caso a V11 não torne a regra explícita, documentá-la no código/configuração e disponibilizar tooltip na interface.

---

# 9. PADRÃO VISUAL PARA STATUS COMERCIAL

**[OBRIGATÓRIO]**

- **✓ Ativo** — verde
- **! Atenção** — amarelo/âmbar
- **× Inativo** — vermelho

Utilizar texto + ícone + cor.

Não utilizar somente bolinha colorida sem significado textual.

---

# 10. DRAWER LATERAL DIREITO — PADRÃO GLOBAL

## 10.1 Objetivo

**[OBRIGATÓRIO]**

O drawer deve **complementar a análise da tela atual**, e não simplesmente repetir a linha selecionada.

Ao clicar em uma entidade, o usuário deve receber contexto suficiente para responder perguntas adicionais sem sair da página.

## 10.2 Estrutura recomendada

**[DECISÃO V12]**

Organizar o drawer em blocos, conforme aplicável:

1. Identificação e status
2. Resumo executivo
3. Evolução/histórico
4. Crédito e risco
5. Comportamento de compra
6. Rankings relacionados
7. Movimentações/eventos

Nem todas as entidades usam todos os blocos.

## 10.3 UX do drawer

- largura suficiente para tabelas compactas e pequenos gráficos;
- fechamento claro;
- rolagem interna;
- cabeçalho fixo com nome da entidade;
- não perder contexto da página de origem;
- quando houver muitos dados, usar seções/tabs internas discretas, mas evitar transformar o drawer em um segundo sistema de navegação.

---

# 11. MÓDULO FATURAMENTO

## 11.1 Objetivo do módulo

O módulo Faturamento possui dois objetivos centrais:

1. analisar faturamento;
2. analisar concentração/Curva ABC por diferentes dimensões.

As dimensões obrigatórias da V12 são:

- Guia
- Cliente
- Loja
- Segmento

## 11.2 Estrutura de páginas

**[OBRIGATÓRIO]**

O módulo passa a possuir cinco páginas claramente separadas:

1. Visão geral
2. Guias
3. Clientes
4. Lojas
5. Segmentos

Na V11, Loja e Segmento aparecem de forma excessivamente agrupada. Na V12, devem ser análises independentes.

---

## 11.3 FATURAMENTO — VISÃO GERAL

### 11.3.1 Filtros

**[OBRIGATÓRIO]**

Filtros compactos e expansíveis conforme padrão global.

Principais sugeridos:

- Período
- Cliente
- Guia atual

Adicionais, quando aplicáveis:

- Guia da venda
- Loja
- Segmento
- Categoria
- Faixa
- Curva ABC
- Status comercial

### 11.3.2 Cards

**[PRESERVAR V11 + APRIMORAR]**

Os cards atuais foram considerados adequados em conceito. Devem ser mantidos, porém qualquer variação/comparação precisa explicar o período de referência.

**[DECISÃO V12]**

Conjunto recomendado:

- Faturamento total do período
- Nº de faturamentos/pedidos distintos
- Ticket médio por faturamento
- Nº de clientes com faturamento no período
- Variação vs período comparativo
- Concentração da Curva A ou participação do Top 10, conforme cálculo já disponível

Se a V11 possuir card relevante adicional, preservar desde que não gere redundância.

### 11.3.3 Comparação temporal

**[OBRIGATÓRIO]**

A atual indicação “evolução atual vs janela anterior” deve ser reescrita para informar exatamente quais datas são comparadas.

Exemplo de copy:

> **Evolução do faturamento**  
> 01/07/2026–31/07/2026 vs 01/06/2026–30/06/2026

### 11.3.4 Concentração dinâmica

**[OBRIGATÓRIO]**

A análise de concentração da Visão Geral deve possuir seletor para alternar entre:

- Clientes
- Guias
- Lojas
- Segmentos

O usuário deve conseguir utilizar o mesmo espaço visual para comparar rapidamente onde o faturamento está concentrado.

O seletor deve atualizar título, gráfico/resumo e números associados.

---

## 11.4 FATURAMENTO — GUIAS

### 11.4.1 Filtros

Filtros expansíveis conforme padrão global.

### 11.4.2 Cards sugeridos

**[DECISÃO V12]**

- Faturamento total
- Nº de guias com venda no período
- Nº de clientes atendidos
- Nº de faturamentos
- Ticket médio por faturamento
- Participação dos guias Curva A

### 11.4.3 Tabela obrigatória

**[OBRIGATÓRIO]**

Colunas:

1. Guia
2. Faturamento
3. Representatividade
4. Acumulado
5. Curva
6. Nº de clientes atendidos
7. Nº de faturamentos distintos
8. Nº de lojas atendidas

Substituir o termo “Participação” por **Representatividade**.

### 11.4.4 Drawer do Guia

**[OBRIGATÓRIO]**

O drawer do Guia deve se comportar como uma visão gerencial da carteira.

#### Bloco A — resumo

- Faturamento no período filtrado
- Faturamento médio mensal no período, quando aplicável
- Nº de clientes
- Nº de lojas
- Nº de faturamentos
- Curva ABC do guia

#### Bloco B — faturamento histórico

- gráfico temporal de faturamento do guia;
- respeitar o período selecionado ou disponibilizar histórico contextual suficiente;
- indicar claramente granularidade e datas.

#### Bloco C — crédito da carteira do guia

Exibir indicadores agregados dos clientes pertencentes à carteira do guia, quando os dados existirem:

- Limite total da carteira
- Limite normal
- Limite extra
- Limite utilizado/consumido
- Limite disponível
- Valor em aberto
- Risco total
- Inadimplência total
- Quantidade de clientes inadimplentes

#### Bloco D — Top 10 clientes do Guia

Tabela/ranking com os dez principais clientes do guia, contendo preferencialmente:

- Cliente
- Faturamento
- Representatividade dentro da carteira do guia
- Curva
- Status comercial
- Limite total
- Risco/valor em aberto
- Inadimplência

O objetivo é responder rapidamente “quem sustenta a carteira deste guia?” e “onde está o risco?”.

---

## 11.5 FATURAMENTO — CLIENTES

### 11.5.1 Filtros

**[OBRIGATÓRIO]**

Filtros expansíveis.

### 11.5.2 Cards

Na V11 faltava um bloco de cards específico na página de Clientes.

**[DECISÃO V12]**

Cards recomendados:

- Faturamento total dos clientes filtrados
- Nº de clientes com faturamento
- Ticket médio por cliente
- Nº de faturamentos
- Participação dos clientes Curva A
- Clientes em Atenção/Inativos, quando status comercial estiver disponível

### 11.5.3 Modos de tabela

**[OBRIGATÓRIO]**

Controle:

- Resumida
- Detalhada

#### Tabela resumida

Colunas prioritárias:

1. Cliente
2. Faturamento
3. Representatividade
4. Acumulado
5. Curva
6. Categoria
7. Nº de lojas em que comprou
8. Nº de faturamentos

#### Tabela detalhada

Além das colunas da visão resumida, incluir:

9. Guia atual
10. Status comercial
11. Faixa
12. Data da primeira compra
13. Data da última compra
14. Dias sem compra
15. Intervalo médio entre compras
16. Inadimplência

**[DECISÃO V12]**

Quando os dados estiverem disponíveis, podem entrar também:

- Nº de guias relacionados no período, se fizer sentido operacionalmente;
- ticket médio do cliente;
- frequência média de compra.

Evitar inserir colunas extras se apenas repetirem informação sem utilidade decisória.

### 11.5.4 Definições comportamentais

**[OBRIGATÓRIO]**

- **Data da última compra:** data mais recente de faturamento/compra válida do cliente.
- **Dias sem compra:** diferença entre a data de referência da análise e a última compra.
- **Intervalo médio entre compras:** média de dias entre compras/faturamentos distintos do cliente dentro do histórico disponível/regra atual.

Se a V11 utilizar uma janela específica, manter a regra e explicá-la em tooltip.

### 11.5.5 Drawer do Cliente

**[OBRIGATÓRIO]**

O drawer deve ficar significativamente mais completo do que na V11.

#### Bloco A — resumo comercial

- Cliente
- Faturamento no período
- Variação com período comparativo — **explicitando datas**
- Curva
- Faixa
- Categoria
- Status comercial
- Guia atual

#### Bloco B — comportamento de compra

- Primeira compra
- Última compra
- Dias sem compra
- Intervalo médio entre compras
- Nº de faturamentos
- Nº de lojas
- Histórico de faturamento, preferencialmente com pequeno gráfico

#### Bloco C — crédito e risco

Exibir:

- Limite normal
- Limite extra
- Limite total
- Limite utilizado/consumido
- Limite disponível
- Valor em aberto
- “Recente”/vencido recente conforme regra do módulo Crédito
- Risco total
- Inadimplência

Os termos devem usar as mesmas regras e fórmulas do módulo Crédito para evitar números divergentes.

#### Bloco D — leitura gerencial

**[DECISÃO V12]**

Sempre que possível, mostrar relações úteis, por exemplo:

- Limite total ÷ faturamento médio mensal
- Valor em aberto ÷ faturamento médio mensal
- Indicador de saturação

O objetivo não é criar uma nota automática de crédito nesta V12, mas fornecer contexto para o usuário julgar se a exposição faz sentido.

---

## 11.6 FATURAMENTO — LOJAS

### 11.6.1 Página independente

**[OBRIGATÓRIO]**

Loja deve possuir página própria e não ficar agregada à análise de Segmento.

### 11.6.2 Cards sugeridos

**[DECISÃO V12]**

- Faturamento total
- Nº de lojas
- Nº de clientes
- Nº de guias
- Nº de faturamentos
- Participação das lojas Curva A

### 11.6.3 Tabela obrigatória

1. Loja
2. Segmento
3. Faturamento
4. Representatividade
5. Acumulado
6. Curva
7. Nº de clientes
8. Nº de guias
9. Nº de faturamentos

### 11.6.4 Drawer da Loja

**[OBRIGATÓRIO]**

Não priorizar crédito, pois crédito não é uma dimensão natural de Loja.

#### Resumo

- Faturamento
- Representatividade
- Curva
- Segmento
- Nº de clientes
- Nº de guias
- Nº de faturamentos

#### Evolução

- faturamento histórico da loja;
- tendência do período.

#### Top 10 clientes da Loja

- Cliente
- Faturamento
- Representatividade na loja
- Curva/status, quando aplicável

#### Top 10 guias da Loja

- Guia
- Faturamento
- Representatividade na loja
- Nº de clientes atendidos na loja, se disponível

O drawer deve ajudar a responder “quem vende nesta loja?” e “quem compra nesta loja?”.

---

## 11.7 FATURAMENTO — SEGMENTOS

### 11.7.1 Página nova e independente

**[OBRIGATÓRIO]**

Criar página específica de Segmentos.

### 11.7.2 Cards sugeridos

**[DECISÃO V12]**

- Faturamento total
- Nº de segmentos
- Nº de lojas
- Nº de clientes
- Nº de guias
- Participação dos segmentos Curva A

### 11.7.3 Tabela obrigatória

1. Segmento
2. Faturamento
3. Representatividade
4. Acumulado
5. Curva
6. Nº de clientes
7. Nº de guias
8. Nº de faturamentos
9. Nº de lojas pertencentes ao segmento

### 11.7.4 Drawer do Segmento

#### Resumo

- Faturamento
- Representatividade
- Curva
- Nº de lojas
- Nº de clientes
- Nº de guias
- Nº de faturamentos

#### Evolução

- faturamento histórico do segmento.

#### Principais lojas do Segmento

Top lojas por faturamento.

#### Principais clientes do Segmento

Top clientes por faturamento dentro do segmento.

#### Principais guias do Segmento

Top guias por faturamento dentro do segmento.

O drawer deve explicar “quem compõe esse segmento” sem exigir navegação para três páginas diferentes.

---

# 12. MÓDULO CRÉDITO

## 12.1 Objetivo do módulo

A análise de crédito da V12 não pode responder apenas:

> “quanto de limite esse cliente possui?”

Ela precisa ajudar a responder:

> “esse limite é coerente com o comportamento de compra e com o risco atual desse cliente ou dessa carteira?”

Esse é o principal salto conceitual do módulo.

## 12.2 Relação entre Crédito e Limite Extra

**[DECISÃO V12]**

Nesta rodada, **Crédito e Limite Extra permanecem módulos separados**, porque cumprem funções analíticas diferentes:

- **Crédito:** fotografia da exposição, disponibilidade, saturação, risco e adequação do limite ao comportamento de compra.
- **Limite Extra:** histórico de concessões/movimentações e análise do efeito dessas alterações.

Porém, os módulos devem compartilhar contexto e dados. Não podem parecer sistemas isolados.

Exemplo:

- Crédito mostra Limite normal + Limite extra = Limite total.
- Limite Extra mostra também a situação atual do crédito do cliente.

## 12.3 Conceitos informados na validação

**[OBRIGATÓRIO]**

- **Limite normal:** limite-base cedido ao cliente.
- **Limite extra:** limite adicional separado do limite normal.
- **Limite total:** Limite normal + Limite extra.
- **Valor em aberto:** exposição atual conforme regra já utilizada na V11.
- **Recente:** conceito associado ao valor vencido/considerado nos últimos 60 dias na análise atual.
- **Risco total:** preservar a fórmula vigente da V11, mas documentá-la e explicá-la.
- **Crédito disponível:** preservar a regra vigente, incluindo o tratamento do “recente”, mas tornar a fórmula compreensível.
- **Saturação:** preservar regra vigente e fornecer definição.
- **Inadimplência:** precisa ser visível e tratada como informação central de risco.

**Atenção de implementação:** a conversa definiu o significado operacional de vários campos, mas não fechou matematicamente todas as fórmulas. Portanto, **não inventar fórmulas novas** se elas já existirem na V11. Extrair as regras do código/base atual, manter consistência e acrescentar explicabilidade.

## 12.4 Páginas da V12

**[DECISÃO V12]**

Estrutura mínima:

1. Visão geral
2. Clientes
3. Guias

Caso a V11 possua outra subpágina indispensável ao funcionamento, preservá-la, desde que não gere redundância.

---

## 12.5 CRÉDITO — VISÃO GERAL

### 12.5.1 Filtros

**[OBRIGATÓRIO]**

Atualmente os filtros são limitados a Período, Cliente, Guia atual, RP e Carteira. Manter esses e adicionar filtros avançados no bloco “Mais filtros”.

Principais:

- Período
- Cliente
- Guia atual
- RP
- Carteira

Adicionais recomendados:

- Loja
- Segmento
- Categoria
- Faixa
- Curva ABC
- Status comercial
- Possui inadimplência
- Faixa de saturação
- Possui limite extra
- Faixa de limite total
- Faixa de risco total

### 12.5.2 Cards

**[OBRIGATÓRIO]** uma linha de cards principais.

**[DECISÃO V12]** conjunto recomendado:

1. Limite total da carteira filtrada
2. Limite disponível
3. Valor em aberto
4. Risco total
5. Inadimplência total
6. Saturação média/mediana ou nº de clientes em alta saturação

Quando o espaço permitir e houver utilidade, apresentar Limite extra em subtexto do card de Limite total, evitando excesso de cards.

### 12.5.3 Distribuição de saturação

**[PRESERVAR V11]**

A distribuição de saturação foi considerada útil e deve permanecer.

Melhorias:

- tooltip explicando as faixas;
- clique em uma faixa pode filtrar a tabela, se tecnicamente simples;
- mostrar quantidade e/ou exposição financeira por faixa quando possível.

### 12.5.4 Maiores riscos

**[OBRIGATÓRIO]**

A seção “Maiores riscos” deve possuir seletor:

- Clientes
- Guias

Ao alternar, o ranking deve atualizar para refletir a entidade escolhida.

### 12.5.5 Tabela resumida de clientes

**[PRESERVAR V11]**

A tabela resumida de clientes na Visão Geral pode permanecer, pois foi considerada útil.

Ela deve funcionar como lista de exceções/consulta rápida, sem tentar substituir a página Clientes.

---

## 12.6 CONTEXTO DE FATURAMENTO DENTRO DO CRÉDITO

**[OBRIGATÓRIO]**

A V12 precisa aproximar exposição de crédito e comportamento de compra.

Para Cliente e Guia, disponibilizar quando possível:

- Faturamento últimos 3 meses
- Faturamento últimos 6 meses
- Faturamento últimos 12 meses
- Média mensal de faturamento no horizonte selecionado
- Relação Limite total / Faturamento médio mensal
- Relação Valor em aberto / Faturamento médio mensal

### 12.6.1 Interpretação

Essas relações não devem automaticamente classificar o cliente como bom ou ruim sem regra de negócio validada. O objetivo é dar escala e contexto.

Exemplo:

Um cliente com limite de R$ 52 mil e R$ 38 mil em aberto é difícil de avaliar isoladamente. Se ele compra R$ 10 mil/mês, a leitura é uma; se compra R$ 100 mil/mês, é outra.

A interface deve tornar essa diferença palpável.

---

## 12.7 CRÉDITO — CLIENTES

### 12.7.1 Filtros e cards

**[OBRIGATÓRIO]**

Aplicar padrão de filtros expansíveis e cards.

Cards sugeridos:

- Nº de clientes analisados
- Limite total
- Limite disponível
- Risco total
- Inadimplência
- Nº de clientes em alta saturação/inadimplentes

### 12.7.2 Tabela resumida

**[DECISÃO V12]**

Colunas prioritárias:

1. Cliente
2. Guia atual
3. Limite normal
4. Limite extra
5. Limite total
6. Valor em aberto
7. Limite disponível
8. Saturação
9. Risco total
10. Inadimplência

### 12.7.3 Tabela detalhada

Adicionar:

11. Faturamento 3 meses
12. Faturamento 6 meses
13. Faturamento 12 meses
14. Faturamento médio mensal
15. Limite total / média mensal
16. Valor em aberto / média mensal
17. Valor recente — últimos 60 dias conforme regra vigente
18. Faixa
19. Categoria
20. Status comercial

Não usar rótulos crípticos para relações. Exemplo preferido:

- “Limite / compra média”
- “Em aberto / compra média”

com tooltip contendo a fórmula.

### 12.7.4 Drawer do Cliente no Crédito

Deve conter:

#### Resumo de crédito

- Limite normal
- Limite extra
- Limite total
- Limite utilizado/consumido
- Limite disponível
- Valor em aberto
- Recente
- Risco total
- Saturação
- Inadimplência

#### Contexto de compra

- Faturamento 3m
- Faturamento 6m
- Faturamento 12m
- Média mensal
- Histórico visual de faturamento

#### Relações

- Limite / média mensal
- Em aberto / média mensal

#### Contexto comercial

- Faixa
- Categoria
- Status comercial
- Guia atual
- Última compra
- Dias sem compra, quando disponível

---

## 12.8 CRÉDITO — GUIAS

### 12.8.1 Filtros e cards

**[OBRIGATÓRIO]**

Mesma lógica de filtros expansíveis e cards executivos.

Cards sugeridos:

- Nº de guias
- Limite total das carteiras
- Valor em aberto
- Risco total
- Inadimplência
- Nº de clientes inadimplentes

### 12.8.2 Tabela de Guias

**[DECISÃO V12]**

Exibir, no mínimo:

- Guia
- Nº de clientes
- Faturamento 3m
- Faturamento 6m
- Faturamento 12m
- Limite total da carteira
- Valor em aberto
- Risco total
- Inadimplência
- Saturação agregada/referencial, conforme regra disponível

### 12.8.3 Drawer do Guia no Crédito

**[OBRIGATÓRIO]**

O drawer precisa mostrar os principais clientes daquele guia e contexto de limite/risco.

#### Resumo da carteira

- Nº de clientes
- Faturamento histórico
- Faturamento 3m/6m/12m
- Limite total
- Limite disponível
- Valor em aberto
- Risco atual
- Inadimplência

#### Principais clientes do Guia

Tabela com:

- Cliente
- Faturamento
- Limite total
- Limite extra
- Valor em aberto
- Risco
- Inadimplência
- Saturação

O objetivo é permitir que o gestor avalie se o risco está concentrado em poucos clientes ou distribuído pela carteira.

---

# 13. MÓDULO LIMITE EXTRA

## 13.1 Objetivo

O módulo Limite Extra deve analisar:

1. quanto e para quem o limite extra foi concedido;
2. como o limite extra se movimentou ao longo do tempo;
3. qual foi o comportamento do faturamento antes e depois das concessões;
4. qual é a situação atual de risco dos clientes beneficiados.

## 13.2 Páginas da V12

**[OBRIGATÓRIO]**

1. Visão geral
2. Movimentações
3. Clientes
4. Guias

---

## 13.3 LIMITE EXTRA — VISÃO GERAL

### 13.3.1 Estrutura geral

**[PRESERVAR V11]**

A Visão Geral foi considerada boa em conceito.

Aplicar melhorias sem descaracterizá-la.

### 13.3.2 Filtros

**[OBRIGATÓRIO]**

Filtros expansíveis conforme padrão global.

### 13.3.3 Cards

**[OBRIGATÓRIO]**

Manter/ajustar os principais cards e assegurar que exista uma linha executiva.

**[DECISÃO V12]** conjunto recomendado:

- Limite extra atual total
- Variação líquida de limite extra no período
- Nº de clientes com limite extra
- Nº de movimentações no período
- Valor total concedido/aumentado no período
- Risco atual dos clientes com limite extra ou inadimplência associada

Se houver distinção entre aumento e redução, expor em subtexto ou tooltip.

### 13.3.4 Remover redundância da tabela de clientes

**[OBRIGATÓRIO]**

A tabela completa de clientes da Visão Geral não precisa repetir o conteúdo da página Clientes.

Remover ou substituir por um resumo/ranking compacto, preservando a página Clientes como local principal da análise tabular.

### 13.3.5 Efeito após aumento

**[PRESERVAR E APRIMORAR]**

Esta análise foi considerada uma das partes mais interessantes do módulo e deve ganhar destaque e explicabilidade.

O objetivo é comparar faturamento antes e depois de uma concessão/aumento de limite extra.

#### Problema atual

Rótulos como “Faturamento 2 meses antes” e “Faturamento 2 meses depois” não explicam:

- quais meses;
- se é soma ou média;
- qual é a data de corte;
- se os meses são completos;
- como múltiplas movimentações interferem na leitura.

#### Metodologia V12

**[DECISÃO V12]**

Para cada evento elegível de aumento de limite extra:

- **Data do evento:** data em que o aumento foi registrado/concedido.
- **Janela antes:** dois meses-calendário completos imediatamente anteriores ao mês/data do evento, ou a regra equivalente já usada pela V11 se ela for tecnicamente diferente e consistente.
- **Janela depois:** dois meses-calendário completos posteriores ao evento.
- Mostrar as **datas/meses exatos** usados.
- Mostrar **faturamento total** da janela antes.
- Mostrar **média mensal antes**.
- Mostrar **faturamento total** da janela depois.
- Mostrar **média mensal depois**.
- Mostrar **variação absoluta**.
- Mostrar **variação percentual**.

Se não houver dois meses completos posteriores disponíveis, sinalizar:

> “Janela pós-aumento ainda incompleta”

Evitar apresentar conclusão definitiva.

Se houver nova alteração de limite dentro da própria janela antes/depois, sinalizar a ocorrência para evitar leitura causal simplista.

#### Copy metodológica

Adicionar um tooltip ou texto curto:

> “Compara o faturamento do cliente nos dois meses completos anteriores ao aumento do limite extra com os dois meses completos posteriores. A variação indica associação temporal, não prova isoladamente que o aumento de limite causou o crescimento.”

Essa ressalva aumenta a qualidade analítica da ferramenta.

### 13.3.6 Drawer do efeito após aumento

**[OBRIGATÓRIO]**

Ao clicar no cliente/evento, mostrar:

- Cliente
- Guia
- Data do aumento
- Limite extra anterior
- Valor do aumento
- Limite extra após movimento
- Limite normal atual
- Limite total atual
- Faturamento da janela antes
- Média mensal antes
- Faturamento da janela depois
- Média mensal depois
- Delta absoluto
- Delta percentual — explicitamente definido
- Utilização/saturação atual
- Valor em aberto
- Risco atual
- Inadimplência
- Outras movimentações na janela, se existirem

O drawer deve contar a história da decisão e do resultado observado, e não apenas repetir o percentual.

---

## 13.4 LIMITE EXTRA — MOVIMENTAÇÕES

### 13.4.1 Tabela

**[PRESERVAR V11]**

A tabela atual foi considerada adequada e não precisa ser redesenhada nesta rodada.

### 13.4.2 Filtros

**[OBRIGATÓRIO]**

Adicionar padrão “Mais filtros / Menos filtros”.

Filtros avançados recomendados:

- Cliente
- Guia
- Tipo de movimentação
- Faixa de valor movimentado
- Situação de inadimplência
- Categoria
- Faixa
- Loja
- Segmento

### 13.4.3 Cards

**[OBRIGATÓRIO]**

Adicionar linha de cards.

**[DECISÃO V12]**:

- Nº de movimentações
- Valor total de aumentos
- Valor total de reduções, quando existir
- Variação líquida
- Nº de clientes movimentados
- Valor médio por movimentação

---

## 13.5 LIMITE EXTRA — CLIENTES

### 13.5.1 Estrutura

**[PRESERVAR V11 + APRIMORAR]**

A tabela atual pode ser mantida, complementada por filtros e cards.

### 13.5.2 Filtros e cards

Aplicar padrão global.

Cards recomendados:

- Nº de clientes com limite extra
- Limite extra atual
- Variação no período
- Nº de clientes com aumento
- Nº de clientes com redução
- Inadimplência/risco dos clientes com limite extra

### 13.5.3 Drawer do Cliente

**[OBRIGATÓRIO]**

Quando um cliente possui múltiplas movimentações — por exemplo, quatro — o drawer deve mostrar **todas as movimentações desse cliente**.

#### Resumo atual

- Limite normal
- Limite extra atual
- Limite total
- Limite disponível
- Valor em aberto
- Risco
- Inadimplência
- Faturamento
- Faixa
- Categoria
- Guia atual

#### Histórico de movimentações

Tabela/timeline em ordem cronológica contendo, no mínimo:

- Data
- Tipo de movimentação
- Valor anterior
- Variação do movimento
- Valor após movimento
- Responsável/justificativa, apenas se a base possuir essas informações

**[SUGESTÃO APROVADA PARA BACKLOG/TÉCNICA]**

Se a aplicação/base já possuir ou vier a possuir dados de governança, registrar quem aprovou, quando e justificativa. Não inventar esses dados na V12 se não existirem.

#### Delta/variação

**[OBRIGATÓRIO]**

Qualquer “Δ” ou percentual apresentado no drawer deve informar claramente a comparação.

Exemplo:

> “Variação do faturamento: +18,4% — média dos 2 meses após vs média dos 2 meses antes do aumento de 15/05/2026.”

---

## 13.6 LIMITE EXTRA — GUIAS

### 13.6.1 Filtros e cards

**[OBRIGATÓRIO]**

- filtros expansíveis;
- linha de cards executivos.

Cards sugeridos:

- Nº de guias
- Nº de clientes com limite extra
- Limite extra atual das carteiras
- Variação líquida no período
- Risco atual
- Inadimplência

### 13.6.2 Tabela

**[DECISÃO V12]**

Preservar informações úteis atuais e garantir, no mínimo:

- Guia
- Nº de clientes
- Faturamento da carteira
- Limite extra atual
- Variação de limite extra no período
- Nº de movimentações
- Risco atual
- Inadimplência

### 13.6.3 Drawer do Guia

**[OBRIGATÓRIO]**

Exibir:

- clientes atuais do guia;
- faturamento histórico da carteira;
- risco atual;
- limite extra atual;
- variação total de limite extra dentro do período filtrado;
- nº de movimentações;
- inadimplência.

#### Lista de clientes do Guia

Para cada cliente, mostrar preferencialmente:

- Cliente
- Faturamento
- Limite normal
- Limite extra atual
- Variação do limite extra no período
- Risco
- Inadimplência

Assim, o usuário consegue entender **quem gerou a variação de limite da carteira**.

---

# 14. MÓDULO FAIXAS

## 14.1 Objetivo

O módulo Faixas precisa deixar de repetir a mesma tabela em três lugares e passar a explicar efetivamente a trajetória dos clientes entre faixas.

Perguntas que a V12 deve responder:

- Em qual faixa o cliente começou o período?
- Em qual faixa terminou?
- Ele subiu, caiu ou permaneceu?
- Como foi a trajetória mês a mês?
- Quanto de faturamento está associado a clientes que evoluíram ou regrediram?
- O cliente possui risco/inadimplência relevante para contextualizar essa evolução?

## 14.2 Simplificação de arquitetura

**[OBRIGATÓRIO]**

A V11 repete a tabela de clientes em:

- Visão Geral
- Evolução
- Clientes

Na V12, eliminar essa redundância.

### Páginas V12

1. Visão geral
2. Clientes

A antiga página/seção de **Evolução** deve ser incorporada à página **Clientes**.

Se “Migração” existir como bloco analítico, ele pode permanecer como seção dentro da página Clientes ou Visão Geral, mas não deve provocar repetição integral da tabela.

---

## 14.3 FAIXAS — VISÃO GERAL

### 14.3.1 Filtros

Filtros expansíveis.

### 14.3.2 Cards

**[DECISÃO V12]**

- Nº de clientes analisados
- Nº de clientes que subiram de faixa
- Nº de clientes que caíram de faixa
- Nº de clientes que mantiveram faixa
- Faturamento total dos clientes analisados
- Faturamento dos clientes que subiram de faixa ou participação desse grupo

### 14.3.3 Resumos analíticos

A Visão Geral deve priorizar distribuição e migração, e não repetir a tabela completa.

Sugestões:

- distribuição de clientes por faixa inicial;
- distribuição por faixa final;
- fluxo/matriz de migração entre faixas;
- faturamento associado a subidas, quedas e permanências.

### 14.3.4 Definição de Faixa inicial x Faixa final

**[OBRIGATÓRIO]**

Deixar visível e didático:

> **Faixa inicial:** faixa do cliente na primeira referência do período filtrado.  
> **Faixa final:** faixa do cliente na última referência do período filtrado.

Quando a granularidade for mensal:

> “Período analisado: jan/2026 a jun/2026. Faixa inicial = jan/2026; faixa final = jun/2026.”

Não obrigar o usuário a inferir essa regra.

---

## 14.4 FAIXAS — CLIENTES

### 14.4.1 Estrutura da página

**[OBRIGATÓRIO]**

1. Filtros expansíveis
2. Cards
3. Gráfico de evolução — manter o conceito aprovado da V11
4. Análise de migração
5. Tabela única de clientes

### 14.4.2 Cards

Podem repetir os principais indicadores da Visão Geral quando necessário ao contexto, mas priorizar indicadores diretamente relacionados à tabela/gráfico filtrado.

### 14.4.3 Gráfico de evolução

**[PRESERVAR V11]**

O gráfico atual foi considerado útil e deve ser mantido/aprimorado.

Melhorias:

- legenda clara;
- período explícito;
- tooltip por ponto/período;
- permitir leitura da quantidade de clientes e/ou faturamento por faixa, quando o seletor fizer sentido.

### 14.4.4 Análise de migração

**[DECISÃO V12]**

Adicionar mais contexto ao bloco de migração.

Idealmente, permitir alternar métrica entre:

- Nº de clientes
- Faturamento

Assim, uma migração de poucos clientes muito relevantes não fica escondida por uma simples contagem.

Quando houver suporte de dados, permitir também contexto de:

- inadimplência dos clientes que migraram;
- faturamento total do cliente/grupo.

### 14.4.5 Tabela de Clientes

**[DECISÃO V12]**

#### Resumida

1. Cliente
2. Faixa inicial
3. Faixa final
4. Movimento — Subiu / Manteve / Caiu
5. Faturamento no período
6. Categoria
7. Status comercial
8. Inadimplência

#### Detalhada

Adicionar:

9. Guia atual
10. Limite total
11. Limite extra
12. Risco total
13. Média mensal de faturamento
14. Primeira referência do período
15. Última referência do período

Evitar redundância com o drawer; a tabela deve permitir comparação entre clientes, enquanto o drawer conta a história individual.

### 14.4.6 Drawer do Cliente em Faixas

**[OBRIGATÓRIO]**

#### Resumo

- Cliente
- Faturamento
- Variação — com período explicitado
- Faixa inicial
- Faixa final
- Faixa atual, se diferente do conceito de faixa final
- Categoria
- Status comercial
- Limite total
- Inadimplência
- Risco, quando aplicável

#### Evolução mensal de faixa

Mostrar trajetória mês a mês.

Exemplo:

| Mês | Faixa | Faturamento |
|---|---:|---:|
| Jan/26 | 3 | R$ ... |
| Fev/26 | 3 | R$ ... |
| Mar/26 | 2 | R$ ... |
| Abr/26 | 2 | R$ ... |
| Mai/26 | 1 | R$ ... |
| Jun/26 | 1 | R$ ... |

A nomenclatura real das faixas deve respeitar a base da V11.

#### Crédito e risco

Quando disponível:

- Limite normal
- Limite extra
- Limite total
- Limite disponível
- Valor em aberto
- Risco
- Inadimplência

#### Faturamento ao longo da trajetória

Idealmente exibir pequeno gráfico ou série mês a mês para permitir cruzar mudança de faixa e comportamento do faturamento.

---

# 15. CLIENTE 360 — FASE 2

**[FASE 2]**

O conceito do Cliente 360 foi considerado interessante, porém a tela precisa de uma reformulação mais profunda.

Decisão para V12:

- manter o módulo no menu;
- manter clicável;
- preservar o funcionamento existente;
- não investir tempo de V12 em ajustes cosméticos ou incrementais;
- criar projeto dedicado posteriormente.

A futura reformulação deverá reconsiderar arquitetura da informação, objetivo do módulo, hierarquia dos dados e integração das visões Comercial, Faturamento, Crédito, Faixas e Limite Extra.

---

# 16. VISÃO EXECUTIVA — FASE 2

**[FASE 2]**

Mesma decisão do Cliente 360.

Para a V12:

- manter no menu;
- manter clicável;
- preservar versão atual;
- não reformular agora.

A Visão Executiva deverá ser trabalhada em rodada posterior para evitar que seja apenas uma colagem de cards dos demais módulos.

---

# 17. CRUZAMENTO ENTRE MÓDULOS

## 17.1 Princípio

**[OBRIGATÓRIO]**

Uma mesma entidade não deve exibir números conflitantes em módulos diferentes.

Exemplos:

- Limite total no Faturamento > Cliente precisa ser o mesmo do Crédito.
- Inadimplência no módulo Faixas precisa usar a mesma fonte/regra do Crédito.
- Limite extra exibido no Crédito deve coincidir com o saldo atual do Limite Extra.

## 17.2 Contextualização cruzada

**[DECISÃO V12]**

Mesmo sem unificar módulos, usar dados cruzados onde aumentam a qualidade da decisão:

- Faturamento dentro de Crédito
- Crédito dentro de Faturamento > Cliente
- Crédito e inadimplência dentro de Faixas
- Crédito atual dentro de Limite Extra
- Limite extra dentro de Crédito

Isso cria uma ferramenta integrada sem destruir a clareza de cada módulo.

---

# 18. REGRAS DE NÃO REDUNDÂNCIA

**[OBRIGATÓRIO]**

Evitar repetir a mesma tabela completa em páginas diferentes.

Critério:

- Visão Geral = cenário e exceções
- Página de entidade = comparação e exploração
- Drawer = profundidade individual

Se a mesma informação aparece em três lugares, cada ocorrência precisa cumprir função diferente. Caso contrário, remover a redundância.

Exemplo já decidido:

- Faixas não repetirá a tabela de clientes em Visão Geral, Evolução e Clientes.

---

# 19. REGRAS DE EXPLICABILIDADE E CONFIANÇA

## 19.1 Termos que obrigatoriamente precisam de definição

Quando aparecerem:

- Representatividade
- Acumulado
- Curva
- Saturação
- Risco total
- Recente
- Crédito disponível
- Inadimplência
- Delta/Variação
- Faixa inicial
- Faixa final
- Faturamento antes/depois

## 19.2 Tooltip padrão

**[DECISÃO V12]**

O tooltip deve responder, quando aplicável:

1. O que significa?
2. Como é calculado?
3. Qual período utiliza?

Exemplo:

> **Representatividade** — percentual do faturamento desta linha sobre o faturamento total resultante dos filtros atuais.

> **Acumulado** — soma progressiva da representatividade após ordenar a dimensão por faturamento decrescente.

---

# 20. REGRAS CONCEITUAIS PARA REPRESENTATIVIDADE, ACUMULADO E ABC

**[OBRIGATÓRIO]**

Em Guias, Clientes, Lojas e Segmentos:

### Representatividade

Percentual da entidade sobre o faturamento total do conjunto filtrado.

### Acumulado

Soma progressiva das representatividades após ordenação por faturamento decrescente.

### Curva ABC

Classificação com base na regra/threshold já vigente no sistema.

**Não redefinir thresholds sem validação.**

---

# 21. ESTADOS, CORES E ACESSIBILIDADE

## 21.1 Não depender somente de cor

**[OBRIGATÓRIO]**

Qualquer status relevante precisa de texto e/ou ícone, porque cor isolada prejudica acessibilidade e compreensão.

Aplicações:

- Curva ABC
- Status comercial
- Inadimplência
- Saturação
- Migração de faixa

## 21.2 Migração de faixa

**[DECISÃO V12]**

Representação sugerida:

- ↑ Subiu
- → Manteve
- ↓ Caiu

Usar cor apenas como reforço.

---

# 22. COMPORTAMENTO RESPONSIVO E DENSIDADE

**[DECISÃO V12]**

A ferramenta é analítica e deve ser otimizada principalmente para desktop/notebook, mas não pode quebrar em telas menores.

Princípios:

- desktop first;
- tabelas podem ter rolagem horizontal controlada;
- drawers devem adaptar largura;
- cards quebram para múltiplas linhas conforme a viewport;
- filtros adicionais não podem sobrepor conteúdo;
- preservar legibilidade em 1366×768 e resoluções superiores.

---

# 23. COMPONENTES REUTILIZÁVEIS

**[DECISÃO V12 — IMPORTANTE PARA DESENVOLVIMENTO]**

A V12 deve reduzir duplicação de código utilizando componentes reutilizáveis para:

- Sidebar
- Cabeçalho de módulo
- FilterBar
- AdvancedFilters
- MetricCard
- ComparisonBadge
- ABCBadge
- CommercialStatusBadge
- RiskBadge/DelinquencyBadge
- ViewModeToggle — Resumida/Detalhada
- EntityTable
- EntityDrawer
- RankingList/Top10
- TrendChart
- InfoTooltip
- EmptyState
- LoadingState

A consistência visual deve vir do compartilhamento real de componentes, e não de cópia manual de CSS por página.

---

# 24. ESTADOS DE VAZIO, ERRO E DADOS INCOMPLETOS

**[DECISÃO V12]**

Criar estados claros para:

- nenhum resultado com os filtros atuais;
- período insuficiente para comparação;
- janela pós-aumento incompleta;
- cliente sem histórico de compra suficiente para intervalo médio;
- entidade sem dado de crédito;
- valor não aplicável.

Evitar mostrar `0` quando a realidade é “sem dado”. Usar `—` e tooltip quando apropriado.

---

# 25. REGRAS DE DADOS E CÁLCULOS

## 25.1 Fonte única

**[OBRIGATÓRIO]**

As métricas repetidas em módulos distintos devem ser calculadas por uma única função/regra compartilhada.

Exemplos:

- faturamento;
- nº de faturamentos;
- inadimplência;
- limite total;
- risco total;
- faixa;
- status comercial.

## 25.2 Distinct count de faturamentos

O “Nº de faturamentos” deve usar o identificador transacional já adotado pela base/V11 e contar documentos/pedidos/faturamentos distintos, evitando contagem de linhas de itens como se fossem operações separadas.

## 25.3 Cliente/guia/loja/segmento sem movimento

Definir claramente se as páginas mostram apenas entidades com movimento no período ou também entidades sem movimento. **[DECISÃO V12]**: por padrão, análises de faturamento devem priorizar entidades com faturamento no período; análises de crédito podem incluir clientes sem faturamento recente se ainda possuem exposição de crédito.

---

# 26. CRITÉRIOS DE ACEITE — PADRÕES GLOBAIS

A V12 não deve ser considerada concluída se qualquer item abaixo falhar:

- [ ] Menu lateral retrátil preservado.
- [ ] Cliente 360 e Visão Executiva continuam acessíveis.
- [ ] Faturamento possui 5 páginas: Visão Geral, Guias, Clientes, Lojas, Segmentos.
- [ ] Loja e Segmento estão separados.
- [ ] Todas as páginas principais dos quatro módulos possuem filtros expansíveis.
- [ ] Páginas analíticas possuem cards coerentes com seu objetivo.
- [ ] Comparações de período mostram datas/metodologia.
- [ ] Não há “delta” sem explicação.
- [ ] Curva ABC utiliza Representatividade + Acumulado + Curva.
- [ ] Curva A possui destaque visual forte.
- [ ] Status comercial possui ícone + cor + texto.
- [ ] Textos não aparecem desnecessariamente em caixa alta.
- [ ] Entidades clicáveis abrem drawer lateral direito.
- [ ] Drawers adicionam contexto em vez de repetir a linha.
- [ ] Inadimplência aparece em contextos de Cliente e Crédito onde solicitado.
- [ ] Crédito incorpora faturamento 3m/6m/12m e relações com limite/exposição.
- [ ] Limite Extra explica claramente o efeito antes/depois.
- [ ] Drawer de Cliente em Limite Extra mostra todas as movimentações.
- [ ] Drawer de Guia em Limite Extra mostra clientes e variação de limite no período.
- [ ] Faixas elimina a repetição da tabela em três páginas.
- [ ] Evolução é incorporada à página Clientes de Faixas.
- [ ] Drawer de Faixas mostra evolução mensal do cliente.
- [ ] Métricas compartilhadas usam regras consistentes entre módulos.

---

# 27. CRITÉRIOS DE ACEITE — FATURAMENTO

## Visão Geral

- [ ] Filtros expansíveis.
- [ ] Cards com comparação explicada.
- [ ] Evolução identifica datas atual x comparação.
- [ ] Concentração alternável por Cliente, Guia, Loja e Segmento.

## Guias

- [ ] Tabela contém Guia, Faturamento, Representatividade, Acumulado, Curva, Nº clientes, Nº faturamentos, Nº lojas.
- [ ] Drawer contém histórico de faturamento.
- [ ] Drawer contém crédito agregado da carteira.
- [ ] Drawer contém Top 10 clientes.

## Clientes

- [ ] Cards adicionados.
- [ ] Toggle Resumida/Detalhada.
- [ ] Tabela detalhada contém primeira compra, última compra, dias sem compra, intervalo médio e inadimplência.
- [ ] Drawer contém bloco completo de crédito.

## Lojas

- [ ] Página independente.
- [ ] Tabela com colunas definidas.
- [ ] Drawer contém Top 10 clientes e Top 10 guias.

## Segmentos

- [ ] Página independente.
- [ ] Tabela com colunas definidas.
- [ ] Drawer contém principais lojas, clientes e guias.

---

# 28. CRITÉRIOS DE ACEITE — CRÉDITO

- [ ] Crédito e Limite Extra permanecem módulos separados nesta rodada.
- [ ] Limite total integra limite normal + extra.
- [ ] Filtros avançados adicionados.
- [ ] Cards executivos adicionados/padronizados.
- [ ] Distribuição de saturação preservada.
- [ ] Maiores riscos alterna Clientes/Guias.
- [ ] Cliente possui faturamento 3m/6m/12m e média mensal.
- [ ] Relações Limite/média e Em aberto/média disponíveis.
- [ ] Drawer do Guia mostra principais clientes e limites/riscos.
- [ ] Fórmulas de risco, recente, saturação e crédito disponível são explicáveis.

---

# 29. CRITÉRIOS DE ACEITE — LIMITE EXTRA

- [ ] Visão Geral preserva essência atual.
- [ ] Tabela completa de clientes não é duplicada desnecessariamente na Visão Geral.
- [ ] “Efeito após aumento” permanece e recebe maior destaque.
- [ ] Janelas antes/depois são explicitadas.
- [ ] Soma, média, delta absoluto e delta percentual são mostrados.
- [ ] Período pós-aumento incompleto é sinalizado.
- [ ] Movimentações recebe filtros avançados e cards.
- [ ] Drawer de Cliente lista todas as movimentações.
- [ ] Delta possui definição explícita.
- [ ] Guias recebe filtros, cards e drawer completo.
- [ ] Drawer de Guia mostra clientes e variação do limite no período.

---

# 30. CRITÉRIOS DE ACEITE — FAIXAS

- [ ] Arquitetura reduzida para Visão Geral + Clientes.
- [ ] Evolução incorporada a Clientes.
- [ ] Tabela completa não é repetida na Visão Geral.
- [ ] Faixa inicial e final são explicadas com datas/períodos.
- [ ] Cards mostram subida, queda e manutenção.
- [ ] Gráfico de evolução preservado.
- [ ] Migração pode ser lida por clientes e faturamento.
- [ ] Tabela única de clientes possui modo resumido/detalhado.
- [ ] Drawer mostra faixa mês a mês.
- [ ] Drawer inclui faturamento e contexto de crédito/inadimplência.

---

# 31. BACKLOG EXPLICITAMENTE POSTERGADO

Itens que não devem desviar o desenvolvimento da V12:

1. Reformulação completa do Cliente 360.
2. Reformulação completa da Visão Executiva.
3. Motor automático de recomendação/aprovação de crédito.
4. Score de crédito proprietário, caso não exista regra validada.
5. Workflow completo de aprovação com usuário/aprovador/justificativa, se esses dados não existirem hoje.
6. Redesenho estrutural de módulos que não foram discutidos nesta rodada.

---

# 32. ORIENTAÇÃO PARA A IMPLEMENTAÇÃO DA V12

Ao receber este documento junto com o ZIP/pacote da V11, o desenvolvedor/agente deve:

1. auditar rapidamente a estrutura da V11 para localizar componentes, dados e regras existentes;
2. mapear as páginas atuais para a arquitetura definida nesta especificação;
3. preservar regras de negócio não modificadas;
4. criar/refatorar componentes globais reutilizáveis antes de duplicar telas;
5. implementar primeiro a camada global — filtros, cards, badges, tabelas, drawers e tooltips;
6. implementar Faturamento;
7. implementar Crédito;
8. implementar Limite Extra;
9. implementar Faixas;
10. revisar consistência cruzada de dados;
11. executar auditoria de UX/UI e regressão;
12. entregar a V12 completa e funcional, não apenas mockups estáticos.

---

# 33. PRINCÍPIOS DE PRODUTO QUE NÃO DEVEM SER PERDIDOS

A V12 deve transmitir cinco características:

### 1. Clareza

O usuário não deve precisar perguntar “o que esse número quer dizer?”.

### 2. Profundidade progressiva

A primeira tela deve ser simples; o detalhe aparece quando o usuário deseja investigar.

### 3. Comparabilidade

Tabelas e rankings precisam facilitar comparação entre clientes, guias, lojas e segmentos.

### 4. Contexto

Crédito sem faturamento é incompleto. Faixa sem trajetória é incompleta. Limite extra sem antes/depois é incompleto.

### 5. Ação

A ferramenta precisa ajudar o usuário a perceber rapidamente:

- concentração;
- oportunidade;
- deterioração;
- risco;
- mudança de comportamento;
- necessidade de aprofundamento.

---

# 34. RESUMO EXECUTIVO DA V12

A V12 consolida uma evolução de arquitetura da ferramenta.

O Master Hub deverá adotar um padrão consistente de **filtros expansíveis + cards executivos + análise visual + tabela + drawer contextual**.

No **Faturamento**, a estrutura passa a separar Visão Geral, Guias, Clientes, Lojas e Segmentos, com Curva ABC completa — Faturamento, Representatividade, Acumulado e Curva — em todas as dimensões. Clientes ganham visão resumida/detalhada e informações de comportamento de compra. Os drawers deixam de ser simples resumos e passam a reunir histórico, rankings e crédito quando aplicável.

No **Crédito**, o foco evolui da exposição absoluta para a adequação do limite ao comportamento de compra. Faturamento de 3, 6 e 12 meses, média mensal e relações entre limite/exposição e compra tornam o risco mais palpável. O módulo mantém saturação e maiores riscos, passando a alternar a leitura entre Clientes e Guias.

No **Limite Extra**, a estrutura permanece separada do Crédito, mas conectada a ele. A análise “Efeito após aumento” é preservada e fortalecida com metodologia explícita, janelas exatas, médias, deltas e contexto de risco. Movimentações e Guias recebem filtros e cards, e o drawer do cliente passa a exibir todo o histórico de movimentações.

No **Faixas**, elimina-se a repetição de tabelas. A antiga Evolução é incorporada à página Clientes. Faixa inicial e final passam a ter significado explícito e o drawer mostra a trajetória mês a mês, cruzando faixa, faturamento e crédito/risco.

**Cliente 360 e Visão Executiva permanecem clicáveis, porém ficam deliberadamente fora da reformulação da V12 e entram na Fase 2.**

---

# 35. PRÓXIMO PASSO IMEDIATO

Anexar ao próximo chat/agente:

1. o pacote/ZIP completo da V11;
2. este arquivo `ESPECIFICACAO_FUNCIONAL_MASTER_HUB_V12.md`;
3. uma instrução direta para implementar integralmente a V12 com base nesta especificação, preservando o que não foi alterado e tomando decisões técnicas somente quando não houver conflito com os requisitos.

A implementação deve ser concluída como uma nova versão funcional da ferramenta e posteriormente submetida a uma rodada de validação técnica e de produto.
