# Escreva um programa que leia um número inteiro qualquer e mostre sua tabuada.

n1 = int(input('Digite um número : '))

print('\n####### Tabuada do {} ####### '.format(n1))
for tab in range(1, 11):
    print(n1, '*', tab, ' = ', n1*tab)
