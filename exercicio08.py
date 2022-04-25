# Escreva um programa que leia um valor em métros e converta ele em Quilômetro, Hectômetro, Decâmetro, centímetros e milímetros.

n1 = float(input('Digite quantos métros você quer converter : '))

km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
cm = n1 * 100
mm = n1 * 1000

print('{} Quilômetro, {} Hectômetro, {} Decâmetro, {} centímetros, {} milímetros'.format(
    km, hm, dam, cm, mm))
