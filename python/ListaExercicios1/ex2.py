# -*- coding: utf-8 -*-
"""
Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 
"""
print("Digite a nota1:")
nota1 = int(input())
print("Digite a nota2:")
nota2 = int(input())

if nota1>=6 and nota2>=6:
    print("Aprovado.")
else:
    print("Reprovado.")
