# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open('stock.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    cantidad_de_filas = len(data)
        
    cantidad_de_tornillos = 0
    
    for i in range(cantidad_de_filas):
            
        valor = data[i].get('tornillos')
            
        cantidad_de_tornillos = int(valor) + cantidad_de_tornillos
        print('registro',i+1,':', valor, '-----> Subtotal:',cantidad_de_tornillos)
    print('Stock total de tornillos:', cantidad_de_tornillos)

    
        


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open('propiedades.csv') as csvfile:
        deptos = list(csv.DictReader(csvfile))
    filas = len(deptos)
    depto_2_amb = 0
    depto_3_amb = 0

    for k in range(filas):
        try:    
            amb = int(deptos[k].get('ambientes'))
            
            if amb == 2:
                depto_2_amb += 1
            elif amb == 3:
                depto_3_amb += 1
        except:
            continue
    print('Cantidad de departamentos disponibles de 2 ambientes:',depto_2_amb)
    print('Cantidad de departamentos disponibles de 3 ambientes:',depto_3_amb)



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
