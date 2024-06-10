import itertools
import time
import random

# Caminhos dos arquivos de entrada e saída
arquivoSerie = "C:/ZED/GeradorDeBoletosMDP/Serie.txt"
arquivoNumeros = "C:/ZED/GeradorDeBoletosMDP/Numeros.txt"
saida = "C:/ZED/GeradorDeBoletosMDP/BoletosBandFM.txt"


# Função para ler números de um arquivo
def ler_numeros(arquivo, preencher_zeros=False):
    with open(arquivo, 'r') as f:
        if preencher_zeros:
            return [line.strip().zfill(5) for line in f]
        else:
            return [line.strip() for line in f]

# Lê os números dos arquivos
numeros1 = ler_numeros(arquivoSerie)
numeros2 = ler_numeros(arquivoNumeros, preencher_zeros=True)

# Inicia a contagem de tempo
start_time = time.time()

# Realiza o cruzamento dos números
cruzamento = [(a, b) for a, b in itertools.product(numeros1, numeros2)]

# Embaralha os números
random.shuffle(cruzamento)

# Escreve o resultado no arquivo de saída
with open(saida, 'w') as f:
    for i, (a, b) in enumerate(cruzamento, 1):
        f.write(f"{i};{a}.{b}\n")

# Calcula o tempo de execução
end_time = time.time()
execution_time = end_time - start_time

print("Processo concluído. O resultado foi salvo em", saida)
print("Tempo de execução:", execution_time, "segundos")
