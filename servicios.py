"""
Metodo de servicios 
"""

def agregar_producto(inventario,nombre,precio,cantidad):
    
    productos = {
        "nombre": str(nombre),
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    inventario.append(productos)
    print("Producto agregado correctamente.")

def mostrar_inventario(inventario):
    