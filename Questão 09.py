# Questão 09
total_digitado = 0
numeros_pares = 0
numeros_impares = 0
numero = 1
while (numero != 0):
    number = int(input('Digite seu número: '))
    total_digitado+=numero
    resultado = number % 2
    if resultado == 0:
        numeros_pares+=1
        print ('O número {} é PAR'.format(number))
    else:
        numeros_impares+=1
        print ('O número {} é IMPAR'.format(number))
    numero = int(input('Digite 0 para SAIR e 1 para CONTINUAR: '))
print ('Número digitados {}, Números pares {} e Números ímpares {}'.format(total_digitado, numeros_pares, numeros_impares))

