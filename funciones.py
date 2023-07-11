import os
import numpy as np

def llenarMatriz(mat):
    p=1
    for i in range(10):
        for j in range(4):
            mat[i,j]=p
            p+=1
def valid(op):
    while(True):
        try:
            op=int(input("   Elija opción: "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar opción entre 1 y 5")
        except ValueError:
            print("Debe ser un número entero")
def mostrardisponibles(departamento):
    os.system("cls")
    for i in range (10):
        print("")
        for j in range (4):
            if(j==1):
                print(departamento[i,j], end="        ")
            else:
                print(departamento[i,j], end="    ")
def validadepart():
    compra=0
    while(True):
        try:
            compra=int(input("ingrese cual quiere comprar del 1 al 40: "))
            if (compra>=1 and compra<=40):
                    break
            else:
                print(" Error.. entre  1 y 40")
        except ValueError:
            print("debe ser un numero entero")
    return compra
def buscarDisponible(departamento,compra):
    for x in range(10):
        for i in range(4):
            if (compra==departamento[x,i]):
                return True
def comprardep(departamento, compra):
    for x in range(10):
        for i in range(4):
            if (departamento[x,i]==compra):
                departamento[x,i]="x"
                if (i==0) :
                    pago=3800
                if (i==1):
                    pago=3000
                if (i==2):
                    pago=2800
                if (i==3):
                    pago=3500
    return pago
def totalVenta(departamento):
    suma=0
    for x in range(10):
        for i in range(4):
            if (departamento[x,i]==0):
                if (i==0):
                    suma+=3800
                elif (i==1):
                    suma+=3000
                elif (i==2):
                    suma+=2800
                elif (i==3):
                    suma+=3500
    return suma
