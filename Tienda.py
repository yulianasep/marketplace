from Producto import Producto
from Compra import Compra

class Tienda:
    def __init__(self, codigo_tienda: str, nombre_tienda: str):
        self.set_codigo_tienda(codigo_tienda)
        self.set_nombre_tienda(nombre_tienda)
        self.set_productos()
        self.set_compras()

    def __str__(self):
        return f"Código: {self.get_codigo_tienda}\nNombre: {self.get_nombre_tienda}\nProductos: {self.get_productos}"
    
    def set_codigo_tienda(self, codigo_tienda):
        self.__codigo_tienda = codigo_tienda

    @property
    def get_codigo_tienda(self):
        return self.__codigo_tienda
    
    def set_nombre_tienda(self, nombre_tienda):
        self.__nombre_tienda = nombre_tienda

    @property
    def get_nombre_tienda(self):
        return self.__nombre_tienda
    
    def set_productos(self):
        self.__productos = []

    @property
    def get_productos(self):
        return self.__productos
    
    def set_compras(self):
        self.__compras = []

    @property
    def get_compras(self):
        return self.__compras
    
    def agregar_producto(self, producto: Producto):
        detalle_producto={
            "codigo_producto": producto.get_codigo_producto,
            "nombre": producto.get_nombre,
            "tipo_producto": producto.get_tipo_producto,
            "precio": producto.get_precio,
            "stock": producto.get_stock
        }
        self.__productos.append(detalle_producto)

    def eliminar_producto(self, producto: Producto):
        self.__productos.remove(producto)

    def agregar_compra(self, compra: Compra):
        detalle_compra={
            "total_compra": compra.calcular_total_compra(),
            "usuario": compra.get_carrito_compra.get_usuario.get_usuario,
        }
        self.__compras.append(detalle_compra)        

    def ver_historial_compras(self):
        usuarios_compras = {}

        for compra in self.__compras:
            usuario = compra['usuario']
            if usuario in usuarios_compras:
                usuarios_compras[usuario].append(compra)
            else:
                usuarios_compras[usuario] = [compra]

        for usuario, compras in usuarios_compras.items():
            print(f"Usuario: {usuario}")
            for compra in compras:
                print(f"Código de compra: {compra['codigo_compra']}")
                print(f"Total de compra: {compra['total_compra']}")
                print("---")