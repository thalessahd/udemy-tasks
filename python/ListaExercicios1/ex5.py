# -*- coding: utf-8 -*-
"""
Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
"""

print("Digite o primeiro número:")
num1 = float(input())
print("Digite o segundo número:")
num2 = float(input())
print("Digite o sinal:")
sinal = input()

if sinal=="+":
    resu = num1+num2
    print(resu)
elif sinal=="-":
    resu = num1-num2
    print(resu)
elif sinal=="*":
    resu = num1*num2
    print(resu)
elif sinal=="/":
    try:
        resu = num1/num2
        print(resu)
    except:
        print("Não é possível divisão por 0.")
else:
    print("Sinal não reconhecido")
