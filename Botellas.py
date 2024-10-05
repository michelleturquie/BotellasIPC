# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:12:25 2024
"""
import random

negrita = '\033[1m'
resetear = '\033[0m'

#Define el orden de las botellas

botellas = list(range(1, 6))
random.shuffle(botellas)
adivinanza = botellas[:5]

Azul = 1
Rojo = 2 
Verde = 3
Negro = 4
Blanco = 5

print("Los numeros del 1 al 5 han sido ordenados aleatoriamente.")

#Pide la cantidad de intentos
print("Tenga en cuenta que el puntaje por cada botella se calcula como [10000 / intentos_totales]")

intentos = input ("¿Cuantos intentos tendrá? ")

#Instrucciones
print (f"{negrita}Instrucciones:{resetear} Usted deberá adivinar el orden en " + str(intentos) + " intentos. Por cada botella adivinado ganará 1000 puntos Por cada intento perdido perderá 100 puntos También puede pedir ayuda escribiendo help [n] donde [n] es el número que quiere revelar. Esta ayuda le revelará el n úmero a cambio de que ahora el puntaje de cada botella se divide a la mitad. Tenga en cuenta que solo puede pedir una ayuda y que también perderá un intento (-100 puntos)")

# Eliminar despues, es para que chequear que funcione ok
print(adivinanza)

intentos = int(intentos)

#Definir puntaje base

puntajebase = (10000/intentos)*5

rondas = 0
puntosfinales = 0

# Entra en el while a pedir los numeros hasta que se quede sin intentos

while intentos > 0:

    ordeningresado = input("Ingresa 5 números del 1 al 5 (sin espacios): ")
    
    intentos -= 1
    
    rondas += 100
    
    ordeningresadoL = [int(digito) for digito in ordeningresado]
    
    comparar = []
       
    for i in range(5):
            
        if adivinanza[i] == ordeningresadoL[i]:
                comparar.append(adivinanza[i])
                
                print("Te quedan " + str(intentos) + " intentos")
    
        if len(comparar) == 5:
            
            print("¡Felicidades! Todos los números están en la posición correcta.")
            
            break
        
        else:
            print(f"No todos los números están en la posición correcta. Números en la posición correcta: {', '.join(map(str, comparar))}.")