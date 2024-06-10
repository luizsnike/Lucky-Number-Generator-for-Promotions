# Gerador de 'Números da Sorte' para Promoções (Português)

Script em Python3 simples para gerar números da sorte para promoções.

A série começa em 0, então um grupo de 10 séries vai de 0 até 9

Os números iniciam de 1 então não haverá número da sorte com sequencias de 0.

O Gerador irá perguntar a quantidade de séries e quantidades de números, após isso irá fazer o embaralhamento e colocar em um arquivo chamado boletos.txt sendo o primeiro item um ID para servir de chave primária para inserção em tabelas, cuidado para trabalhar com isso ou ignore o ID.

Após o término o script irá fazer uma verificação de integridade para garantir que não existe a combinacação Série|Número repetida.

Para usar basta executar o arquivo 00_GeraBoletosFull.py e seguir os passos, os demais arquivos são complementares para executar separadamente os passos caso necessário.

Aviso: Cuidado para gerar quantidades muito grandes, pois ele faz isso em memória e pode consumir toda memória da máquina.

# 'Lucky Number' Generator for Promotions (English)

Simple Python3 script to generate lucky numbers for promotions.

The series starts at 0, so a group of 10 series goes from 0 to 9

The numbers start at 1, so there will be no lucky numbers with sequences of 0.

The Generator will ask for the number of series and number quantities, after that it will shuffle and place them in a file called boletos.txt, with the first item being an ID to serve as a primary key for insertion into tables, be careful when working with this or ignore the ID.

After finishing, the script will perform an integrity check to ensure that there is no repeated Series|Number combination.

To use, simply run the file 00_GeraBoletosFull.py and follow the steps; the other files are complementary so you can perform the steps separately if necessary.

Warning: Be careful when generating very large quantities, as it does this in memory and can consume all of the machine's memory.

# Generador de 'Números de la Suerte' para Promociones (Spanish)

Script Python3 simple para generar números de la suerte para promociones.

La serie empieza en 0, por lo que un grupo de 10 series va del 0 al 9.

Los números comienzan desde 1 por lo que no habrá números de la suerte con secuencias de 0.

El Generador solicitará el número de series y la cantidad de números, después de lo cual los barajará y los colocará en un archivo llamado boletos.txt, siendo el primer elemento una identificación que sirva como clave principal para la inserción en tablas. Tenga cuidado al trabajar con esto o ignore la identificación.

Una vez completado, el script realizará una verificación de integridad para garantizar que no haya una combinación repetida de Serie|Número.

Para utilizar simplemente ejecuta el archivo 00_GeraBoletosFull.py y sigue los pasos, los demás archivos son complementarios para realizar los pasos por separado si es necesario.

Advertencia: Tenga cuidado al generar cantidades muy grandes, ya que lo hace en la memoria y puede consumir toda la memoria de la máquina.