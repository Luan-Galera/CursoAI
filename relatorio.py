import pandas as pd

# =========================================================
# 1. LEITURA DO ARQUIVO CSV
# =========================================================
# Aqui carregamos os dados da produção têxtil para análise

df = pd.read_csv("producao_textil.csv", sep=",")

# Remove espaços invisíveis nos nomes das colunas
df.columns = df.columns.str.strip()


# =========================================================
# 2. VERIFICAÇÃO (opcional, mas útil para validação)
# =========================================================
# Mostra as colunas disponíveis no dataset

print("\nCOLUNAS DO ARQUIVO:")
print(df.columns)


# =========================================================
# 3. RELATÓRIO DE PRODUÇÃO POR MÁQUINA
# =========================================================
# Agrupamos os dados por id_maquina e somamos as peças produzidas

relatorio_maquina = df.groupby("id_maquina")["pecas_produzidas"].sum()


# =========================================================
# 4. RELATÓRIO DE PRODUÇÃO POR TURNO
# =========================================================
# Agrupamos os dados por turno e somamos as peças produzidas

relatorio_turno = df.groupby("turno")["pecas_produzidas"].sum()


# =========================================================
# 5. EXIBIÇÃO DOS RESULTADOS
# =========================================================
# Mostramos os relatórios no terminal

print("\n========== RELATÓRIO POR MÁQUINA ==========\n")
print(relatorio_maquina)

print("\n========== RELATÓRIO POR TURNO ==========\n")
print(relatorio_turno)


# =========================================================
# 6. EXPORTAÇÃO DOS RESULTADOS (OPCIONAL)
# =========================================================
# Salvamos os relatórios em arquivos CSV para uso externo

relatorio_maquina.to_csv("relatorio_maquinas.csv")
relatorio_turno.to_csv("relatorio_turnos.csv")

print("\nArquivos de relatório gerados com sucesso!")