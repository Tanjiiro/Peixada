massa = 0.0
tempo = 0
massa = float(input('Informe a massa inicial do material : '))
while (massa >= 0.5):
    massa = massa / 2
    tempo = tempo + 50
print('A perda de massa e de : {} levando {} segundos . '.format(massa,tempo))