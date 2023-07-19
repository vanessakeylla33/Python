# Estruturas condicionais

idade = 18
if idade >=18:
    print('você é maior de idade. ')
else:
    print('você é menor de idade')   

"""
imagine que você queira imprimir "aprovada(o)", caso o estudante tenha média superior 
, ou igua a 7, e "Reprovado", caso a média seja inferior a 7.
"""

media = float(input('informe a média do estudante:'))

if media >=7:
    print('Você foi Aprovado')
elif media >= 5:
    print('Recuperacao')
else:
    print('Você foi Reprovado')    
