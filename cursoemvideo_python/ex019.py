# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome deles e escrevendo o nome escolhido.
from random import choice
a1 = input(str('primeiro aluno: '))
a2 = input(str('segundo aluno: '))
a3 = input(str('terceiro aluno: '))
a4 = input(str('quarto aluno: '))

lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print("O aluno sorteado foi: {}".format(escolhido))
