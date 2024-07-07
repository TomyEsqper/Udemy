def calcular_ingresos(ventas):
    return sum(venta[1] * venta[2] for venta in ventas)

def producto_mas_vendido(ventas):
    return max(ventas, key=lambda venta: venta[1])[0]

def producto_mayores_ingresos(ventas):
    return max(ventas, key=lambda venta: venta[1] * venta[2])[0]

def calcular_promedio_precio(ventas):
    precios = sum(venta[2] for venta in ventas)
    promedio = precios/len(ventas)
    return promedio

def filtar_producto(ventas):
    precio_minimo = min(venta[2] for venta in ventas)
    return [venta[0] for venta in ventas if venta[2] >= precio_minimo]

# Lista de ventas de ejemplo
ventas = [
    ("producto1", 10, 100),
    ("producto2", 5, 200),
    ("producto3", 7, 150),
    ("producto4", 3, 250),
    ("producto5", 20, 50)
]

# Pruebas de las funciones corregidas
print(calcular_ingresos(ventas))              # Debería imprimir 4800
print(producto_mas_vendido(ventas))           # Debería imprimir "producto5"
print(producto_mayores_ingresos(ventas))      # Debería imprimir "producto1"
print(calcular_promedio_precio(ventas))       # Debería imprimir 150.0
print(filtar_producto(ventas))                # Debería imprimir ["producto2", "producto3", "producto4"]
