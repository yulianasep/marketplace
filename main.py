from Usuario import Usuario
from Producto import Producto
from CarritoCompra import CarritoCompra
from Compra import Compra
from Tienda import Tienda 

luisa = Usuario("luma", "luisa", "estrada",12544632)
Daniel = Usuario("dante", "Daniel", "lopez", 5422335)
Maria = Usuario("mari", "Maria", "gomez", 12544632)

print(Maria)
print(Daniel.get_usuario)
print(Daniel.get_nombres)
print(Daniel.get_apellidos)
print(Daniel.get_identificacion)

tomate = Producto("v854", "tomate", "fruta", 1000, 500 )
papa = Producto("v855", "papa", "verdura", 2000, 1000 )
cebolla = Producto("v856", "cebolla", "verdura", 3000, 1500 )
zanahoria = Producto("v857", "zanahoria", "verdura", 4000, 2000 )
arroz = Producto("v858", "arroz", "grano", 5000, 0 )

print(tomate) 
print(papa.get_codigo_producto)
print(papa.get_nombre)
print(papa.get_tipo_producto)
print(papa.get_precio)
print(papa.get_stock)

carrito_luisa = CarritoCompra("CC1", luisa)
carrito_daniel = CarritoCompra("CC2", Daniel)

print(carrito_luisa)
print(carrito_luisa.get_codigo_carrito)
print(carrito_luisa.get_usuario)
carrito_luisa.agregar_producto(tomate, 2)
carrito_luisa.agregar_producto(papa, 5)
carrito_luisa.agregar_producto(cebolla, 4)
carrito_luisa.agregar_producto(zanahoria, 8)
carrito_luisa.agregar_producto(arroz,1)
print(carrito_luisa.get_productos)


compra_luisa = Compra(carrito_luisa)
print(compra_luisa)
compra_luisa.calcular_total_compra()

tienda1 = Tienda("T1", "Tienda de verduras")
print(tienda1)
print(tienda1.get_codigo_tienda)
print(tienda1.get_nombre_tienda)
tienda1.agregar_producto(tomate)
tienda1.agregar_producto(papa)
tienda1.agregar_producto(cebolla)
tienda1.agregar_producto(zanahoria)
tienda1.agregar_producto(arroz)

print(tienda1.get_productos)

tienda1.agregar_compra(compra_luisa)
print(tienda1.get_compras)

