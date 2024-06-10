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


        f.write("\nQuantidade de duplicatas: {}\n".format(len(duplicados)))
        f.write("Registros duplicados:\n")
        for dup in duplicados:
            f.write(f"{dup}\n")

# Exemplo de uso
arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
arquivo_saida = "estatisticasDeIntegridade.txt"
encontrar_duplicados_e_agrupar(arquivo_entrada, arquivo_saida)
