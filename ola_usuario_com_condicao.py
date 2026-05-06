import sys

if (len(sys.argv) >= 2): #se o usuario passar argumento,
    print(f"Olá, {sys.argv[1]}!") #dê olá a ele
else: #senão
    print("Por favor, indique o seu nome") #peça para que ele passe o argumento

