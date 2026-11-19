import json
from collections import defaultdict
def cargar_ventas(ruta="data.json"):
    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return datos["ventas"]
def total_facturado(ventas):
    return sum(v["cantidad"] * v["precio_unitario"] for v in ventas)
def ventas_por_categoria(ventas):
    resumen = defaultdict(float)
    for v in ventas:
        resumen[v["categoria"]] += v["cantidad"] * v["precio_unitario"]
    return dict(resumen)
def producto_mas_vendido(ventas):
    unidades = defaultdict(int)
    for v in ventas:
        unidades[v["producto"]] += v["cantidad"]
    return max(unidades, key=unidades.get)
if __name__ == "__main__":
    ventas = cargar_ventas()
    print(f"Total facturado: {total_facturado(ventas):.2f} €")
    print("Ventas por categoría:", ventas_por_categoria(ventas))
    print("Producto más vendido:", producto_mas_vendido(ventas))
