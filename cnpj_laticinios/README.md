# Lean Radar de Oportunidades — Laticínios

Versão preparada para publicação estática no GitHub Pages.

## Estrutura

- `index.html` — ferramenta
- `data/base.xlsx` — base pública carregada automaticamente
- `.nojekyll` — evita processamento do projeto pelo Jekyll

## Publicação no GitHub Pages

1. Envie todo o conteúdo desta pasta para a raiz do repositório.
2. No GitHub, abra **Settings → Pages**.
3. Em **Build and deployment**, escolha **Deploy from a branch**.
4. Selecione a branch `main` e a pasta `/ (root)`.
5. Salve e aguarde a URL do GitHub Pages.

## Atualizar a base

Substitua somente `data/base.xlsx` por um novo XLSX com a mesma estrutura de colunas e faça o commit. O Radar usa o identificador fixo `radar-laticinios`, então listas, status, observações e próximas ações salvos no mesmo navegador continuam vinculados por CNPJ.

## Importante

- O XLSX publicado no GitHub Pages é **somente leitura para a ferramenta**.
- Alterações comerciais feitas no Radar ficam no navegador do usuário e podem ser exportadas.
- A ferramenta **não grava de volta** no arquivo do GitHub.
- Como o navegador precisa baixar `data/base.xlsx`, o arquivo deve ser considerado público quando o repositório/site for público.
