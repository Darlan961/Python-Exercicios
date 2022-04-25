# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²


largura = float(input('Digite a largura da parede : '))
altura = float(input('Digite a altura da parede : '))

area = largura * altura
qtdTinta = area / 2

print('\nSua parede tem a dimensão de {}x{}'.format(largura, altura))
print('Você irá precisar de {} litros de tinta para pintar uma parede com {}m²' .format(
    qtdTinta, area))
