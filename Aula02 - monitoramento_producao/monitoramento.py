import csv
from collections import defaultdict

# Dicionários para armazenar os dados
producao_por_maquina = defaultdict(int)
producao_por_turno = defaultdict(int)

# Nome do arquivo CSV
arquivo_csv = "producao.csv"

try:
    # Leitura do arquivo CSV
    with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            id_maquina = linha['id_maquina']
            turno = linha['turno']
            pecas = int(linha['pecas_produzidas'])

            # Soma produção por máquina
            producao_por_maquina[id_maquina] += pecas

            # Soma produção por turno
            producao_por_turno[turno] += pecas

    # Exibição do relatório
    print("=" * 50)
    print("RELATÓRIO DE PRODUÇÃO - INDÚSTRIA TÊXTIL")
    print("=" * 50)

    print("\nTotal produzido por máquina:\n")

    for maquina, total in producao_por_maquina.items():
        print(f"Máquina {maquina}: {total} peças")

    # Identifica o melhor turno
    melhor_turno = max(producao_por_turno, key=producao_por_turno.get)

    print("\n" + "=" * 50)
    print("DESEMPENHO DOS TURNOS")
    print("=" * 50)

    for turno, total in producao_por_turno.items():
        print(f"Turno {turno}: {total} peças")

    print("\nMelhor turno:", melhor_turno)
    print(f"Total produzido: {producao_por_turno[melhor_turno]} peças")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")