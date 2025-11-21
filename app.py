#de archivos traer todo
from archivos import *
#de servicios traer todo
from servicios import *

def main():
    bd = []

    while True:
        print("\n===== Inventario avanzado =====")
        print("1. Ingrese el producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Actualizar Producto")
        print("5. Eliminar producto")
        print("6. Estadisticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")

        opcion = input("Seleccione la opcion: ")

        if opcion.isdecimal():
            print("Opcion invalida")
            continue

        opcion = int(opcion)

        if opcion == 1:
            name = input("Ingrese el nombre del producto: ")
            