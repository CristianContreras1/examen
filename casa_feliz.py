from tkinter.tix import Tree
import numpy as np
import os
import funciones as fn
departamento=np.empty([10,4], type(int))
fn.llenarMatriz(departamento)
os.system("cls")
compra=0
op=0


def buscarDisponible(departamento,compra):
    for x in range(10):
        for i in range(4):
            if (compra==departamento[x,i]):
                return True

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


while(op!=5):
    os.system("cls")
    print("    bienvenido a Casa feliz")
    print("[1] -> Comprar departamento")
    print("[2] -> Mostrar departamentos disponibles")
    print("[3] -> Ver listado de compradores")
    print("[4] -> Mostrar ganancias totales")
    print("[5] -> Salir")
    print("")
    while(True):
        try:
            op=int(input("   Elija opción: "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar opción entre 1 y 5")
        except ValueError:
            print("Debe ser un número entero")
    if (op==1):
        fn.mostrardisponibles(departamento)
        print("")
        print("considere que la primera fila pertenece al tipo A con el precio de 3800 UF")
        print("considere que la segunda fila pertenece al tipo B con el precio de 3000 UF")
        print("considere que la tercera fila pertenece al tipo C con el precio de 2800 UF")
        print("considere que la cuarta  fila pertenece al tipo D con el precio de 3500 UF")
        while(True):
            try:
                compra=int(input("ingrese cual quiere comprar del 1 al 40: "))
                if (compra>=1 and compra<=40):
                        break
                else:
                    print(" Error.. entre  1 y 40")
            except ValueError:
                print("debe ser un numero entero")
        comprueba= buscarDisponible(departamento,compra)
        if comprueba:       #comprueba devuelve valor true
            print("El departamento esta disponible!!")
            pagar=fn.comprardep(departamento, compra)
            print("Usted va a cancelar: ", pagar)
            while(True):
                try:
                    rut=int(input("ingrese su rut para confirmar la compra (sin guion y minimo 8 numeros)"))
                    if(rut>9999999):
                        break
                    else:
                        print("debe tener como minimo 8 numeros")
                except ValueError:
                    print("deben ser numeros enteros")
        else: 
            print("El el departamento no esta disponible")
        
        os.system("pause")
        
    if (op==2):
        os.system("cls")
        for i in range (10):
            print("")
            for j in range (4):
                if(j==1):
                    print(departamento[i,j], end="        ")
                else:
                    print(departamento[i,j], end="    ")
        os.system("pause")        
    if (op==3):
        print("")
    if (op==4):
        suma=totalVenta(departamento)
        if (suma!=0):
            print(" El total vendido $ es: ", suma)
        else:
            print(" no hay departamentos vendidos")
        os.system("pause")
    if (op==5):
        print("adios, hasta luego cristian contreras")