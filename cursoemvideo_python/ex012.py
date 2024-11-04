#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com aumento de 15% de aumento.

salario = float(input('Digite o salário do funcionário: '))
novoSalario = salario + (salario*15/100)

print('Antigo salário: {}\nSalário com aumento de 15%: {}'.format(salario, novoSalario))