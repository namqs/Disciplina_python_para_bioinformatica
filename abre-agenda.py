arquivo = open("agenda.txt", 'r')
'''
print("Nome do arquivo: ", arquivo.name)
print("Modo de operação do arquivo: ", arquivo.mode)
print("Status do arquivo: ", arquivo.closed)

arquivo.close()
print("Novo status do arquivo: ", arquivo.closed)
'''

# Gravando o conteúdo do arquivo, linha a linha, em uma variável
linhas = arquivo.readlines()
# Qual o tipo de dados dessa variável?
print(type(linhas))
# Iterando linha a linha, elemento a elemento dessa variável
for linha in linhas:
 print(linha)

# neste modo, deve-se sempre fechar o arquivo após o uso
arquivo.close()
