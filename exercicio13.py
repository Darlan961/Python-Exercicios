# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Digite seu salário : R$ '))

increase = salary * (15/100)
total = salary + increase 

print('Seu salário atual é R${:.2f} com o aumento ficará : R${:.2f}'.format(salary, total))

