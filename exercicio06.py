# Crie um algoritimo que leia um número e mostre o seu dobro o seu triplo e sua raiz quadrada.

n1 = int(input('Digite um número : '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print('O dobro do número {} é {} o triplo é {} e a raiz é {}'.format(
    n1, dobro, triplo, raiz))
