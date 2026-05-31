# Atividade 02

---

# 🧰 Tecnologias Utilizadas

## 🌐 Frontend

- HTML5
- Tailwind CSS

## 🐍 Backend / Dados

- Python 3
- Pandas

## 🗄️ Banco de Dados

- SQL

---

# 📁 Estrutura do Projeto

```bash
Atividade02/
│
├── consultas.sql
├── index.html
├── producao_textil.csv
├── README.md
├── relatorio_maquinas.csv
├── relatorio_turnos.csv
└── relatorio.py
```

---

# ⚙️ Requisitos

## 🐍 Python

Instalar Python 3:
https://www.python.org/

## 📦 Instalar dependência

```bash
pip install pandas
```

---

# 🚀 Como Executar o Projeto

## 🌐 1. Landing Page

Abra o arquivo:

```bash
index.html
```

no navegador.

---

## 🐍 2. Análise de Produção (Python)

Execute no terminal:

```bash
python relatorio.py
```

### O sistema irá:

- Ler o arquivo `producao_textil.csv`
- Gerar relatório de produção por máquina
- Gerar relatório de produção por turno
- Exibir resultados no terminal
- Exportar relatórios em CSV

---

## 🗄️ 3. Banco de Dados (SQL)

Execute o arquivo:

```bash
consultas.sql
```

em um banco compatível:

- MySQL
- PostgreSQL
- SQL Server

### O script contém:

- Criação da tabela `estoque_producao`
- Inserção de dados de exemplo
- Análise de valor total em estoque
- Produtos abaixo do estoque mínimo
- Análise por categoria
- Análise por linha de produção
- Produtos com status crítico

---

# 📊 Estrutura dos Dados

## 📌 Produção Têxtil (`producao_textil.csv`)

```csv
id_maquina,turno,pecas_produzidas,data
Tear_01,Manhã,1200,2026-05-25
Tear_02,Tarde,980,2026-05-25
```

---

# 📈 Funcionalidades do Sistema

## 🌐 Frontend (Portal SENAI)

- Layout responsivo
- Interface moderna com Tailwind CSS
- Identidade visual SENAI (vermelho, branco e preto)
- Portal de cursos de tecnologia

---

## 🐍 Python (Análise de Dados)

- Leitura de CSV industrial
- Agrupamento por máquina
- Agrupamento por turno
- Cálculo de produção total
- Exportação automática de relatórios

---

## 🗄️ SQL (Estoque Industrial)

- Criação de tabela única (`estoque_producao`)
- Controle de estoque industrial
- Identificação de produtos críticos
- Análise por categoria
- Análise por linha de produção
- Cálculo de valor total em estoque

---

# 📤 Saídas do Sistema

## 🖥️ Terminal

Exibe relatórios de produção em tempo real.

## 📁 Arquivos gerados

- `relatorio_maquinas.csv`
- `relatorio_turnos.csv`

---

# 📊 Exemplo de Saída (Python)

```
========== RELATÓRIO POR MÁQUINA ==========

id_maquina
Tear_01    2550
Tear_02    2000

========== RELATÓRIO POR TURNO ==========

turno
Manhã    2300
Tarde     980
Noite    2370
```

---

# 🧠 Conceitos Aplicados

- Manipulação de dados com Pandas
- Agrupamento (GROUP BY conceitual)
- Análise de dados industriais
- Estruturação de relatórios
- Modelagem básica de banco de dados SQL

---

# 👨‍🏫 Autor

Projeto acadêmico desenvolvido para fins educacionais no contexto de:

- Desenvolvimento Web
- Programação em Python
- Banco de Dados SQL
- Automação e Análise Industrial
