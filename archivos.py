"""
modulo para manejo de archivos CSV.
Incluye funciones para guardar y cargar datos de inventario con validacion
"""

import csv

HEADER = ["nombre", "precio", "cantidad"]


def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guardar la base de productos en un archivo CSV.
    """
    if not inventario:
        print("No hay datos para guardar.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if incluir_header:
                writer.writerow(HEADER)
            for prod in inventario:
                writer.writerow([
                    prod["nombre"], prod["precio"], prod["cantidad"]
                ])
        print(f"Archivo guardado correctamente en: {ruta}")
    except Exception as e:
        print("Error al guardar CSV:", e)


def cargar_csv(ruta):
    """
    Cargar datos desde un CSV
    Retorna lista de productos validos + contador de errores.
    """
    
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)

            if header != HEADER:
                print("El archivo no tiene el encabezado correcto.")
                return [], 0

            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue

                nombre, pre, canti = fila
                try:
                    inventario.append({
                        "nombre": nombre,
                        "precio": pre,
                        "cantidad": canti
                    })
                except:
                    errores += 1

        return inventario, errores

    except FileNotFoundError:
        print("Archivo no encontrado.")
        return [], 0
    except Exception as e:
        print("Error al leer CSV:", e)
        return [], 0