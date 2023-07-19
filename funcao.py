# Funcao inicial 


def saudacao():
    print('Seja bem vinda(o)!')
    print('Olá é um prazer ter você fazendo parte desse curso!')

saudacao()

    # Funcao com paramentro

def saudacao(nome):
    print(f'Seja bem vinda(o),{nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de!')

saudacao('Vanessa')

    #funcao com retorno

def soma(num1, num2):
    return num1 +  num2
resultado = soma (5,7)
print('O resultado da soma é', resultado)


def calculadora(num1, num2, operacao = '+'):
    if operacao == '+':
        return num1 + num2
    elif operacao  == '-':
        return num1 + num2
        
resultado = calculadora (10,20,)

print(resultado)