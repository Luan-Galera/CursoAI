# Linha 04 — Fábrica Modelo

Site estático de demonstração da aula **IA Generativa aplicada a DevOps e CI/CD**.
Três arquivos — HTML, CSS e JavaScript — publicados automaticamente no GitHub Pages a cada
`git push` na branch `main`.

🔗 **Site publicado:** https://SEU-USUARIO.github.io/demo-cicd-industria/

---

## O pipeline

| Job | O que faz |
|---|---|
| **build** | Copia os arquivos para `dist/` e carimba na página o commit, a branch, o número da execução e a data |
| **test** | Confere o que saiu do build: arquivos presentes, marcadores substituídos, `lang`, `<title>`, viewport, referências de CSS/JS e `alt` nas imagens |
| **deploy** | Publica a pasta `dist/` no GitHub Pages — só se o build e os testes passaram |

Nada de Node, nada de Python: as três etapas são comandos de terminal dentro do próprio
arquivo `.github/workflows/ci-cd.yml`.

O bloco **"Última publicação"** no fim da página mostra o commit que gerou aquela versão.
É a prova visual de que o pipeline rodou. Abrindo o `index.html` direto no navegador,
ele mostra "execução local".

---

## Estrutura

```
.
├── index.html                    # a página
├── style.css                     # estilos
├── script.js                     # contadores + selo de publicação
└── .github/workflows/
    ├── ci-cd.yml                 # o pipeline completo (build → test → deploy)
    └── deploy-simples.yml.txt    # versão mínima, só deploy
```

---

## Rodando local

Abra o `index.html` no navegador. Só isso.

Se preferir um servidor local (recomendado, evita restrições do protocolo `file://`):

```bash
npx serve .
# ou, se tiver Python instalado:
python -m http.server 8000
```

---

## Ativando o GitHub Pages

1. **Settings → Pages**
2. Em **Source**, selecione **GitHub Actions**
3. `git push` na `main` e acompanhe a aba **Actions**

---

## Tecnologias

HTML5 · CSS3 · JavaScript (ES6) · GitHub Actions · GitHub Pages

---

## Autor

Material didático — SENAI Jaú/SP · Programa de Programação em IA Generativa.
