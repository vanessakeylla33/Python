numero_sorteado = 15

numero_escolhido = int(input('informe um numero entre 1 e 20:'))

while numero_escolhido != numero_sorteado:
    print ('você errou o numero, tente novamente...')

    numero_escolhido = int(input('informe um numero entre 1 e 20:'))
   
    print ('Parabéns! você acertou!')



   # Ex: Estrutura com contador

contador = 0

while contador < 5:
    print(contador)

    contador = contador +1 