import sys

# Verifica se foi fornecido o argumento correto
if len(sys.argv) != 2:
    print("Uso: python script.py <fim>")
    sys.exit(1)

# Obtém o valor final do range do argumento da linha de comando
fim=int(sys.argv[1])+1

# Definindo o caminho do arquivo de saída
saida = "C:/ZED/GeradorDeBoletosMDP/Numeros.txt"

print("Gerando números sequenciais:")

# Gera os números sequenciais e os escreve no arquivo de saída
with open(saida, 'w') as f:
    for i in range(1, fim):
        num = str(i).zfill(5)
        f.write(num + "\n")

print("Processo concluído. Quantidade de numeros gerados {}".format(fim-1))


