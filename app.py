# Trabajo Práctico I - Programación II

import bibloteca as b
import os

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Eliminar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")
    
def gestionar_prestamo():
    codigo_libro = input("ingrese el codigo del libro: ")
    indice_libro = int()
    encontrado = False

    for i,libro in enumerate(b.libros):
        if libro.get('cod') == codigo_libro:
            indice_libro = i
            encontrado = True
            break
        
    if encontrado == True:
        titulo = b.libros[indice_libro]['titulo']
        autor = b.libros[indice_libro]['autor']
        ejemplares_disponibles = b.libros[indice_libro]['cant_ej_ad'] - b.libros[indice_libro]['cant_ej_pr']
        print(f"""
              Titulo: {titulo }
              Autor: {autor}
              Ejemplares disponibles: {ejemplares_disponibles}
              """)
        if ejemplares_disponibles > 0:
           confirmar_prestamo = input("¿Desea confirmar el prestamo de este libro? (Si/No) ")
           confirmar_prestamo = confirmar_prestamo.upper()
           if confirmar_prestamo == "SI":
               b.libros[indice_libro]['cant_ej_pr'] += 1
               print("Prestamo realizado con exito.")
           else:
               print("Prestamo cancelado.")
        else:
            print("No quedan mas ejemplares disponibles.")  
    else:
        print("Libro no encontrado")
            
           

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            gestionar_prestamo()
            print()
        elif int(opt) == 2:
            #completar
            print()
        elif int(opt) == 3:
            #completar
            print()
        elif int(opt) == 4:
            #completar
            print()
        elif int(opt) == 5:
            #completar
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")