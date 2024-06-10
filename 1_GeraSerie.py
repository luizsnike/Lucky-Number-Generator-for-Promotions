import sys

# Verifica se foram fornecidos os argumentos corretos
if len(sys.argv) != 2:
    print("Uso: python script.py <fim>")
    sys.exit(1)

# Obtém os valores de início, fim e passo dos argumentos da linha de comando
inicio = 0
fim = int(sys.argv[1])-1
passo = 1

# Definindo o caminho do arquivo de saída
saida = "C:/ZED/GeradorDeBoletosMDP/Serie.txt".format(inicio, fim)

# Gera os números no intervalo especificado e os escreve no arquivo de saída
with open(saida, 'w') as f:
    for i in range(inicio, fim + 1, passo):
        f.write(f"{i}\n")

print("Processo concluído. O arquivo com os números de {} a {} foi salvo em {}".format(inicio, fim, saida))
