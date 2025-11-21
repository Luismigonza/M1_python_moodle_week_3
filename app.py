#de archivos traer todo
from archivos import *
#de servicios traer todo
from servicios import *

def main():
    inventario = []

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

        if not opcion.isdecimal():   
            print("Opcion invalida")
            continue

        opcion = int(opcion)


        if opcion == 1:
            nombre = str(input("Ingrese el nombre del producto: "))
            try:
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
            except ValueError:
                print("el precio y cantidad deben ser numericos.")
                continue

            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 2:
            mostrar_inventario(inventario)





if __name__ == "__main__":
    main()