#!/usr/bin/env python
# -*- coding: utf-8 -*-
from _ast import If
class Principal:

    def ejercicio1():
        nombre = "Alberto"
        apellido = "Merino"
        edad = 20
        altura = 2.50
        peso = 80.3
        print('Mi nombre es: ', nombre, ' mi primer apellido es: ', apellido, ' Mi edad es: ', edad, ' Mido: ', altura, ' y peso: ', peso) 
    
    ejercicio1()
    
    def ejercicio2():
        a = 2
        b = 3
        c = 5
        resultado = 0
        resultado = a + b
        print('El resultado de a + b es: ', resultado)
    ejercicio2()
    
    def ejercicio3():
        #Lista de nombres
        nombres = ["Alberto", "Luis", "Alejandro", "Izan", "Mario"]                  
        #Lista de nombres
        edades = [18, 19, 20, 21, 22]
        #Lista de frutas
        frutas = ["Papaya", "Mango", "Nispero", "Pomelo", "Mora"]
        print (nombres[0])
        print (edades[0])
        print(frutas[0])
        print(nombres[-1])
        print(edades[-1])
        print(frutas[-1])
    ejercicio3()
    
    def ejercicio4():
        #Lista par
        par = [2, 4, 6, 8]
        #Lista impar
        impar = [1, 3, 5, 7]
        resultado = 0
        
        #Ejercicio SUMA
        resultado = par[0] + impar[0]
        print (resultado)
        
        #Ejercicio RESTA
        resultado = par[1] - impar[1]
        print(resultado)
        
        #Ejercicio MULTIPLICACION
        resultado = par[-1] * impar[2]
        print(resultado)
        
        #Ejercicio DIVISION
        resultado = par[-1] / impar[0]
        print(resultado)
        
        #Ejercicio SUMA2
        resultado = impar[1] + par[2] + impar[-1]
        print(resultado)
    ejercicio4()
    
    def ejercicio5():
        num = int(input("Introduce un numero y descubre si es par, impar o 0"))
        
        if(num%2 == 0):
            print(num, " es un numero par")
        elif (num%2 != 0):
            print(num, " es un numero impar")
    ejercicio5()
    
    def ejercicio6():
        listanum = []
        num = int(input("Por favor, introduce el numero 1"))
        listanum.insert(-1, num)
        num = int(input("Por favor, introduce el numero 2"))
        listanum.insert(-1, num)
        num = int(input("Por favor, introduce el numero 3"))
        listanum.insert(-1, num)
        listanum.sort(reverse=False)
        print(listanum)       
    ejercicio6()  
    
    def ejercicio7():
         meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
         indice = int(input("Escribe un numero del 1 al 12 para escoger un mes"))
         if indice > 0 & indice <= 12:
             print(meses[indice-1])
         else:
             print("El numero escrito no esta entre 1 y 12")
    ejercicio7()
    
    def ejercicio8():
        num = [8, 1, 5, 10, 2, 4]
        print(max(num))
    ejercicio8()
    
    def ejercicio9():
        anio = int(input("Introduce un año para saber si es bisiesto: "))
        
        if (
            anio%4 == 0 and anio%100 != 0
            ):
            print("El año es bisiesto")
        else:
            print("El año NO es bisiesto")
    ejercicio9()
    
    def ejercicio10():
        for i in range(1, 3):
            for j in range(1, 4): 
                if i == 2 and j == 1:
                    print(i, ' ',j+2)
                else:             
                    print(i, ' ', j)
                if i == 2 and j == 2:
                    i+=1
    ejercicio10()