# Questão 04
soma=0
somam=0
somaf=0
pessoas=1
while (pessoas!=0):
    sexo=str(input('Digite o sexo (m)masculino e (f)feminino: '))
    soma+=pessoas
    if sexo=='m':
        somam+=1
    elif sexo =='f':
        somaf+=1
    pessoas=int(input('Digite 0 para SAIR e 1 para CONTINUAR: '))
print('Total: {} Masculino: {} Feminino; {}'.format(soma, somam, somaf))
