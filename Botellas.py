import random

# Colores y diseño para la consola

negrita = '\033[1m'
subrayado = '\033[4m'

colorazul = '\033[34m'
colorverde = '\033[32m'
colorojo = '\033[31m'
colorblanco = '\033[30;47m'
colornegro = '\033[37;40m'

resetear = '\033[0m'

colores = {

"1": colorazul,
"2": colorojo,
"3": colorverde,
"4": colornegro,
"5": colorblanco

}

#Define el orden de las botellas

botellas = list(range(1, 6))
random.shuffle(botellas)
adivinanza = botellas[:5]

#Bienvenida

print(f" \n¡Bienvenido al parque de diversiones!  \n\nEstara jugando a adivinar los colores con 5 botellas \n{colorazul} Azul = 1 {resetear} {colorojo} Rojo = 2 {resetear} {colorverde} Verde = 3 {resetear} {colornegro} Negro = 4 {colorblanco} Blanco = 5 {resetear}\n \nLos numeros del 1 al 5 han sido ordenados aleatoriamente.")

#Pide la cantidad de intentos
print("\nTenga en cuenta que el puntaje por cada botella se calcula como [10000 / intentos_totales]")

intentos = input (f"{negrita}¿Cuantos intentos tendrá? {resetear}")

#Instrucciones
print (f"\n{negrita}{subrayado}Instrucciones:{resetear} \nUsted deberá adivinar el orden en " + str(intentos) + " intentos. Por cada botella adivinado ganará 1000 puntos Por cada intento perdido perderá 100 puntos. \nTambién puede pedir ayuda escribiendo help en lugar de la adivinanza. Esta ayuda le revelará el número a cambio de que ahora el puntaje de cada botella se divide a la mitad. Tenga en cuenta que solo puede pedir una ayuda y que también perderá un intento (-100 puntos). \n")

intentos = int(intentos)

#Definir puntaje base

puntajebase = (10000/intentos)*5

rondas = 0
puntosfinales = 0

# Entra en el while a pedir los numeros hasta que se quede sin intentos

acertados = 0
ayuda = 0

while intentos > 0 and acertados < 5:

    ordeningresado = input("Ingresa 5 números del 1 al 5 (sin espacios): ")
    
    rondas += 100
    intentos -= 1
    acertados = 0

    # Sistema de ayudas

    if ordeningresado.lower() == "help" and ayuda == 0:

        ayuda += 1
        puntajebase = (5000/intentos)*5
        numerohelp=input(f"{negrita}Que numero desea revelar?{resetear} ")

        posicionhelp = adivinanza.index(int(numerohelp)) + 1

        revelar = ["_"] * 5
        revelar[posicionhelp - 1] = str(numerohelp) 

        concolor = [colores[num] + num + resetear if num != "_" else "_" for num in revelar]

        str_1 = " "
    
        print(str_1.join(concolor))

    # Permitir solo una ayuda

    elif ordeningresado.lower() == "help" and ayuda > 0:

        print(f"{negrita}Solo se permite una ayuda, perdio el turno{resetear}, \nIngrese adivinanzas o seguira perdiendo turnos.")

    # Condiciones para que se ingrese correctamente, si no va al else    

    elif len(str(ordeningresado)) == 5:

        ordeningresadoL = [int(digito) for digito in ordeningresado]

        # Comparar para ver cuantas posciones hay correctas    

        for i in range(5):
                    
            if adivinanza[i] == ordeningresadoL[i]:
                        
                acertados += 1

    else: 

        print(f"\n{negrita}Perdio el turno{resetear} \nIngrese correctamente los numeros o seguira perdiendo turnos.")                

    print("Te quedan " + str(intentos) + " intentos")
    print("Hay " + str(acertados) + " posiciones acertadas")   


# Puntaje

puntajefinal = puntajebase - rondas 

# En caso de ganar

puntajefinal = round(puntajefinal)

if acertados == 5:

    print(f"{negrita}¡Felicidades!{resetear} Todos los números están en la posición correcta.")

    print(f"{negrita}{subrayado}Tu puntaje final es{resetear}: " + str(puntajefinal))

# En caso de perder

else:
    print(f"\n{negrita}Perdiste!{resetear} Ya tendras suerte\n{negrita}{subrayado}Tu puntaje final es:{resetear} " + str(puntajefinal) + "\nLa respuesta correcta era " + str(adivinanza) + "!")
         
    