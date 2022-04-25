# Faça um algoritimo que leia o preço e mostre seu novo preço com desconto de 5%

price = float(input('Digite o preço : '))

discount = price * (5/100)
total = price - discount

print('O novo valor com desconto é R${:.2f} '.format(total))
