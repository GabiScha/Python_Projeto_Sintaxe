
# -> Códigos que não serão executados


#VARIÁVEIS --

#nome = input('Digite o seu nome: ')

#print(f'Olá {nome}, seja muito bem vindo')


#OPERAÇÕES --

#n1 = input('Digite a sua n1:')
#n2 = input('Digite a sua n2:')

#print(int(n1)+int(n2))


#n1 = int(input('Digite uma nota: '))
#n2 = int(input('Digite uma nota: '))

#media = (n1 + n2) / 2


#print(media)

#trfs = 5 < 6

#print(trfs)



#IFS --

#media = int(input('digite sua media'))
#taxa = int(input('sua taxa'))

#if media >= 6 and taxa >= 75:
#    print('vc foi aprovado')
#else:
#    print('vc n foi aprovado')


#aprovado = media >= 6 and taxa >=75
#print(aprovado)




# WHILE --

# i = 0
# while i <= 10:
#     print('oi')  
#     i += 1

# i = 0
# while i > 0:
#     print(f'{5} x {i} = {5*i}')
#     i+=1

# interromper while

soma = 0
cont = 0 
while True:
    nota = int(input('Digite uma nota ou -1 pra sair'))
    if nota == -1:
        break

    soma = soma + nota
    cont += 1
    print(soma)


print(f'a média da sala é: {soma/cont}')









