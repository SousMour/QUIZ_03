#DESAFIO: QUESTÃO DE TEMPO
print("Pense em um número de 0 a 1000:")
n=int(input())
par = n %2
if  par==0:
    print("Você pensou em um número par")
else:
    print("Você pensou em um número impar")
