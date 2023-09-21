#DESAFIO: MANTENDO SUA PONTUAÇÃO
print('''Qual a primeira letra do alfabeto?
a - B
b-  D
c -  A
d - C
''')
resposta=input()
score=0
ponto= score + 1

if  resposta == "a" :
    print(f' Parabéns, você não é tãooooo burro, Sua pontuação é: {ponto}')
    
elif resposta == "c":
    print(f'Aí que burro, dá zero pra ele!!Sua pontuação é: {score}')
else:
    print( f' Leia novamente a questão, faça-me um favor!Sua pontuação é: {score}')
    
