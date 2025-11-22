"""
Modulo de servicios 
"""

def agregar_producto(inventario,nombre,precio,cantidad):
    """
    Agrega un producto a la base de datos.
    """
    productos = {
        "nombre": str(nombre),
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    inventario.append(productos)
    print("Producto agregado correctamente.")

def mostrar_inventario(inventario):
    """
    Muestra la lista de productos existentes en un formato legible.
    """
    
    if not inventario:
        print("No hay Productos registrados")
        return

    print("\n=== LISTA DE PRODUCTOS ===")
    for prod in inventario:
        print(f"Producto: {prod['nombre']} | Precio: {prod['precio']} | Cantidad: {prod['cantidad']}")

def buscar_producto(inventario,nombre):
    """
    Busca un producto por nombre. Retorna el diccionario o None
    """
    for prod in inventario:
        if prod["nombre"] == nombre:
            return prod
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza datos de un producto si existen. 
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print("No se encontro el producto.")
        return
    
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    print("Producto actualizado correctamente.")

def eliminar_producto(inventario,nombre):
    """
    Elimina productos por nombre
    """
    producto = buscar_producto(inventario,nombre)
    if producto:
        inventario.remove(producto)
        print("Producto eliminado.")
    else:
        print("No se encontro el producto.")

def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario:
    - unidades_totales
    - valor_total
    - producto_mas_caro
    - producto_mayor_stock
    - ranking_por_valor (opcional)
    Retorna un diccionario con los resultados.
    """

    if not inventario:
        print("⚠ No hay datos para estadísticas.")
        return None

    # Listas auxiliares para cálculos
    subtotales = []
    
    # Lambda opcional para subtotal
    subtotal = lambda p: p["precio"] * p["cantidad"]

    for prod in inventario:
        subtotales.append((prod["nombre"], subtotal(prod)))

    # Cálculos generales
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    # Productos especiales
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    # Ranking opcional por valor total
    ranking = sorted(subtotales, key=lambda x: x[1], reverse=True)

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"]),
        "ranking_por_valor": ranking
    }

def mostrar_estadisticas(inventario):
    """
    Imprime estadísticas del inventario de manera legible.
    """
    est = calcular_estadisticas(inventario)
    if not est:
        return

    print("\n=== ESTADÍSTICAS DEL INVENTARIO ===")
    print(f"Unidades totales en inventario: {est['unidades_totales']}")
    print(f"Valor total del inventario: ${est['valor_total']:.2f}")

    print(f"Producto más caro: {est['producto_mas_caro'][0]} "
          f"(${est['producto_mas_caro'][1]:.2f})")

    print(f"Producto con mayor stock: {est['producto_mayor_stock'][0]} "
          f"({est['producto_mayor_stock'][1]} unidades)")

    print("\nRanking por valor (precio * cantidad):")
    for nombre, val in est["ranking_por_valor"]:
        print(f"- {nombre}: ${val:.2f}")
