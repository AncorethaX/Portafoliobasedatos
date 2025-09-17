productos = ["Notebook", "Polera", "Cereal", "Celular", "Audífonos"]

productos.append("Zapatos")
productos.append("Tablet")
productos_destacados = productos[:3]

inventario = {
    "Notebook": 10,
    "Polera": 20,
    "Cereal": 15,
    "Celular": 5,
    "Audífonos": 12
}

inventario["Zapatos"] = 8
print("Stock de Cereal:", inventario["Cereal"])

categorías = ("Electrónica", "Ropa", "Alimentos")
print("Segunda categoría:", categorías[1])

categoria1, categoria2, categoria3 = categorías
print("Categoría 1:", categoria1)
print("Categoría 2:", categoria2)
print("Categoría 3:", categoria3)

productos_unicos = set(productos)
print("Productos únicos:", productos_unicos)

productos_mayusculas = [producto.upper() for producto in productos]
print("Productos en mayúsculas:", productos_mayusculas)

print("Lista completa de productos:", productos)
print("Productos destacados:", productos_destacados)