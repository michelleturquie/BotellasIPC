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

#Bienvenida

print(" \n¡Bienvenido al parque de diversiones!  \n\nEstara jugando a adivinar los colores con 5 botellas \nAzul = 1 Rojo = 2 Verde = 3 Negro = 4 Blanco = 5\n \nLos numeros del 1 al 5 han sido ordenados aleatoriamente.")

#Pide la cantidad de intentos
print("\nTenga en cuenta que el puntaje por cada botella se calcula como [10000 / intentos_totales]")

intentos = input (f"{negrita}¿Cuantos intentos tendrá? {resetear}")

#Instrucciones
print (f" \n \n{negrita}Instrucciones:{resetear} \nUsted deberá adivinar el orden en " + str(intentos) + " intentos. Por cada botella adivinado ganará 1000 puntos Por cada intento perdido perderá 100 puntos. \nTambién puede pedir ayuda escribiendo help [n] donde [n] es el número que quiere revelar. Esta ayuda le revelará el número a cambio de que ahora el puntaje de cada botella se divide a la mitad. Tenga en cuenta que solo puede pedir una ayuda y que también perderá un intento (-100 puntos). \n")

# Eliminar despues, es para que chequear que funcione ok
print(adivinanza)

intentos = int(intentos)

#Definir puntaje base

puntajebase = (10000/intentos)*5

rondas = 0
puntosfinales = 0

# Entra en el while a pedir los numeros hasta que se quede sin intentos

acertados = 0

while intentos > 0 and acertados < 5:

    ordeningresado = input("\nIngresa 5 números del 1 al 5 (sin espacios): ")
    
    rondas += 100
    intentos -= 1
    acertados = 0
    
    ordeningresadoL = [int(digito) for digito in ordeningresado]
       
    for i in range(5):
            
        if adivinanza[i] == ordeningresadoL[i]:
                
            acertados += 1

    print("Te quedan " + str(intentos) + " intentos")
    print("Hay " + str(acertados) + " posiciones acertadas")   

puntajefinal = puntajebase - rondas 

if acertados == 5:

    print("¡Felicidades! Todos los números están en la posición correcta.")

    puntajefinal = str(puntajefinal)

    print("Tu puntaje final es: " + puntajefinal + "!")

else:
    print("Perdiste! Ya tendras suerte")
         
    