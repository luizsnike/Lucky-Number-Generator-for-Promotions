import sys
import itertools
import time
import random
# Definindo o caminho do arquivo de saída
saida_numeros = "numeros.txt"
saida_series = "series.txt"
saida_boletos = "boletos.txt"
saida_integridade = "estatisticasDeIntegridade.txt"
print("ATENÇÃO\n")
print("Seus números serão armazenados no arquivo {} nesta mesma pasta, se houver numeros neste arquivo eles serão eliminados.\n".format(saida_numeros))
print("Suas séries serão armazenadas no arquivo {} nesta mesma pasta, se houver séries neste arquivo elas serão eliminadas.\n".format(saida_series))
print("Seus boletos serão armazenados no arquivo {} nesta mesma pasta, se houver boletos neste arquivo eles serão eliminados.\n".format(saida_boletos))
sair = input('Digite [s] para Sair ou qualquer tecla para continuar: ')
if sair.lower() == 's':
    print('Você abortou o processo, nenhum arquivo foi modificado!\n')
    exit()
#obtém os numeros do prompt
try:
    qtd_series = int(input('\nDigite a quantidade de SERIES que deseja gerar: '))
    qtd_numeros = int(input('\nDigite a quantidade de NUMEROS por serie que deseja gerar: '))
except:
    print('Você digitou um valor inválido!')
    exit()

# Obtém o valor final do range do argumento da linha de comando
fim_numeros=int(qtd_numeros)+1

print("\nGerando números sequenciais: ")

# Gera os números sequenciais e os escreve no arquivo de saída
with open(saida_numeros, 'w') as f:
    for i in range(1, fim_numeros):
        num = str(i).zfill(5)
        f.write(num + "\n")

print("Processo concluído. Quantidade de numeros gerados {} foi salvo em {}".format(fim_numeros-1, saida_numeros))

######### GERANDO AS SERIES
# Obtém os valores de início, fim e passo dos argumentos da linha de comando
inicio_series = 0
fim_series = int(qtd_series)-1
passo_series = 1

# Definindo o caminho do arquivo de saída
saida = saida_series.format(inicio_series, fim_series)
print("\nGerando series: ")
# Gera os números no intervalo especificado e os escreve no arquivo de saída
with open(saida, 'w') as f:
    for i in range(inicio_series, fim_series + 1, passo_series):
        f.write(f"{i}\n")

print("Processo concluído. O arquivo com as séries de {} a {} foi salvo em {}".format(inicio_series, fim_series, saida))

print("\nGerando Boletos: ")
# Função para ler números de um arquivo
def ler_numeros(arquivo, preencher_zeros=False):
    with open(arquivo, 'r') as f:
        if preencher_zeros:
            return [line.strip().zfill(5) for line in f]
        else:
            return [line.strip() for line in f]

# Lê os números dos arquivos
num_series = ler_numeros(saida_series)
num_numeros_seq = ler_numeros(saida_numeros, preencher_zeros=True)

# Inicia a contagem de tempo
print("Aqui demora um pouco, vamos calcular o tempo: ")
start_time = time.time()

# Realiza o cruzamento dos números
cruzamento = [(a, b) for a, b in itertools.product(num_series, num_numeros_seq)]

# Embaralha os números
random.shuffle(cruzamento)

# Escreve o resultado no arquivo de saída
with open(saida_boletos, 'w') as f:
    for i, (a, b) in enumerate(cruzamento, 1):
        f.write(f"{i};{a}.{b}\n")

# Calcula o tempo de execução
end_time = time.time()
execution_time = end_time - start_time

print("Processo concluído. O resultado foi salvo em", saida_boletos)
print(f"Tempo de execução para gerar os BOLETOS: {execution_time:,.2f} segundos")

###### Teste de Integridade

def encontrar_duplicados_e_agrupar(arquivo_entrada, arquivo_saida):
    # Dicionário para armazenar a contagem de ocorrências de cada registro
    contagem = {}

    # Lista para armazenar os registros duplicados
    duplicados = []


    # Contador para a quantidade total de números
    total_numeros = 0

    # Lê o arquivo de entrada e verifica duplicatas e agrupa os números em séries
    with open(arquivo_entrada, 'r') as f:
        for linha in f:
            partes = linha.strip().split(";")  # Assumindo que o delimitador é ";"
            if len(partes) < 2:
                continue  # Ignora linhas com menos de duas partes
            registro = partes[1]  # Considera apenas a segunda parte como o registro

            # Atualiza a contagem de ocorrências do registro
            contagem[registro] = contagem.get(registro, 0) + 1

            # Se for uma duplicata, adiciona à lista de duplicados
            if contagem[registro] == 2:
                duplicados.append(registro)

            # Atualiza o contador de números
            total_numeros += 1

    # Escreve as estatísticas no arquivo de saída
    with open(arquivo_saida, 'w') as f:
        f.write(f"Quantidade total de números: {total_numeros}\n\n")
        print(f"\nQuantidade total de números: {total_numeros}")
        f.write("\nQuantidade de duplicatas: {}\n".format(len(duplicados)))
        print("\nQuantidade de duplicatas: {}".format(len(duplicados)))
        f.write("Registros duplicados:\n")
        for dup in duplicados:
            f.write(f"{dup}\n")
            print(f"{dup}\n")

print("\nEfetuando teste de Integridade / Duplicidade: ")
encontrar_duplicados_e_agrupar(saida_boletos, saida_integridade)
print(f"\nDados de Integridade salvos em: {saida_integridade}")

print("\nPROCESSO CONCLUIDO COM EXITO")