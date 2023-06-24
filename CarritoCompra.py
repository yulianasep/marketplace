from Usuario import Usuario
from Producto import Producto

class CarritoCompra:
    def __init__(self, codigo_carrito: str, usuario: Usuario):
        self.set_codigo_carrito(codigo_carrito)
        self.set_usuario(usuario)
        self.set_productos()

    def __str__(self):
        return f"Código: {self.__codigo_carrito}\nUsuario: {self.__usuario}\
            \nProductos: {self.__productos}"
    
    def set_codigo_carrito(self, codigo_carrito):
        self.__codigo_carrito = codigo_carrito

    @property
    def get_codigo_carrito(self):
        return self.__codigo_carrito

    def set_usuario(self, usuario):
        self.__usuario = usuario

    @property
    def get_usuario(self):
        return self.__usuario
    
    def set_productos(self):
        self.__productos = []

    @property
    def get_productos(self):
        return self.__productos

    def agregar_producto(self, producto: Producto, cantidad: int):
        if producto.get_stock > 0:
            producto_item = {
                "nombre":producto.get_nombre,
                "cantidad":cantidad,
                "precio":producto.get_precio
            }
            self.__productos.append(producto_item)
            producto.set_stock(producto.get_stock - 1)

        else:
            print("No hay stock disponible")

    def eliminar_producto(self, producto: Producto, cantidad: int):
        for producto_item in self.__productos:
            if producto_item["nombre"] == producto.get_nombre:
                producto.set_stock(producto.get_stock + cantidad)
                self.__productos.remove(producto_item)
            
            else:
                print("No se encontró el producto")

