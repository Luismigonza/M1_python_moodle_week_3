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
        print("9. Salir")

        opcion = input("Seleccione la opcion: ")

        if not opcion.isdecimal():   
            print("Opcion invalida")
            continue

        opcion = int(opcion)


        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ")
            try:
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))

                if precio < 0 or cantidad < 0:
                    print("El precio y la cantidad no pueden ser negativos.")
                    continue

            except ValueError:
                print("El precio y cantidad deben ser numéricos.")
                continue


            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            nom = input("Nombre del producto: ")
            prod = buscar_producto(inventario, nom)
            if prod:
                print(prod)
            else:
                print("No se encontro el producto.")

        elif opcion == 4:
            nom = input("Nombre del producto: ")
            try:
                precio = input("Nuevo precio del producto (ENTER para no cambiar): ")
                precio = float(precio) if precio else None

                cantidad = input("Ingrese la cantidad del producto (ENTER para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None

                if precio is not None and precio < 0:
                    print("El precio no puede ser negativo.")
                    continue

                if cantidad is not None and cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue

            except ValueError:
                print("El precio y cantidad deben ser numéricos.")
                continue

            actualizar_producto(inventario, nom, precio, cantidad)

        elif opcion == 5:
            nom = input("Nombre del producto: ")
            eliminar_producto(inventario,nom)

        elif opcion == 6:
            mostrar_estadisticas(inventario)

        elif opcion == 7:
            ruta = input("Ruta del archivo CSV: ")
            guardar_csv(inventario, ruta)

        elif opcion == 8:
            ruta = input("Ruta del CSV a cargar: ")
            nuevos, errores = cargar_csv(ruta)

            if not nuevos and errores == 0:
                continue

            print(f"Se cargaron {len(nuevos)} productos. Filas invalidas: {errores}")

            opc = input("¿Sobrescribir datos actuales? (S/N): ").upper()
            if opc == "S":
                inventario = nuevos
                print("Inventario reemplazado.")
            else:
                #Fusion
                existentes = {e["nombre"]: e for e in inventario}
                for prod in nuevos:
                    if prod["nombre"] in existentes:
                        #Actualiza datos
                        existentes[prod["nombre"]].update(prod)
                    else:
                        inventario.append(prod)
                print("Datos fusionados correctamente.")

        elif opcion == 9:
            print("Hasta luego.")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()