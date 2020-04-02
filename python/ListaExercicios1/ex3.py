# -*- coding: utf-8 -*-
"""
Escreva um programa que resolva uma equação de segundo grau. 
"""
import math

print("Digite o valor de 'a':")
a = float(input())
print("Digite o valor de 'b':")
b = float(input())
print("Digite o valor de 'c':")
c = float(input())

print("A equação de segundo grau é: " +str(a)+"x² + "+str(b)+"x + "+str(c))

raiz = b*b - 4*a*c 
if raiz>0:
    raiz = math.sqrt(raiz)
    x1 = (-b + raiz)/(2*a)
    x2 = (-b - raiz)/(2*a)
    print("x1 = "+str(x1)+"\nx2 = "+str(x2))
elif raiz==0:
    x = -b/(2*a)
    print("x = "+str(x))
else:
    print("A solução da equação não está no conjunto dos números reais.")