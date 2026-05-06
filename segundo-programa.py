#!/usr/bin/env python3 para indicar que é um arquivo python
import sys

print("Olá, " + sys.argv[1] + "!")  #o sys.argv pega os argumentos passados pelo usuário no terminal (que entra como lista). O [1] indica qual elemento da lista eu quero pegar (1° nome) 

#Exemplo de chamada no terminal: python .\segundo-programa.py Nat
#Saída: Olá, Nat!