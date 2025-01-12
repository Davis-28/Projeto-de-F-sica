# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:57:09 2024

@author: fec12
"""


G = 6.67430e-11  
M = 5.972e24     
R = 6371000      
delta_t = 1      


def calcular_gravidade(altura):
    d = R + altura  
    return G * M / d**2


altura_inicial = float(input("Digite a altura inicial em metros: "))
v0 = 0  


altura = altura_inicial
velocidade = v0
tempo = 0


print("\nSimulação da queda livre:\n")
print(f"Tempo (s)\tAltura (m)\tVelocidade (m/s)\tGravidade (m/s²)")

while altura > 0:
    gravidade = calcular_gravidade(altura)
    delta_h = velocidade * delta_t + 0.5 * gravidade * delta_t**2
    velocidade += gravidade * delta_t
    altura = max(altura - delta_h, 0)  
    tempo += delta_t

 
    print(f"{tempo}\t\t{altura:.2f}\t\t{velocidade:.2f}\t\t{gravidade:.2f}")

print("\nO objeto atingiu o solo.")
