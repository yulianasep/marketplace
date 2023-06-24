class Producto:
    def __init__(self, codigo_producto: str, nombre: str, 
        tipo_producto: str, precio: float, stock: int):
        self.set_codigo_producto(codigo_producto)
        self.set_nombre(nombre)
        self.set_tipo_producto(tipo_producto)
        self.set_precio(precio)
        self.set_stock(stock)

    def __str__(self):
        return f"Código: {self.__codigo_producto}\nNombre: {self.__nombre}\
        \nTipo: {self.__tipo_producto}\nPrecio: {self.__precio}\nStock: {self.__stock}"
    
    def set_codigo_producto(self, codigo_producto):
        self.__codigo_producto = codigo_producto

    @property
    def get_codigo_producto(self):
        return self.__codigo_producto
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    @property
    def get_nombre(self):
        return self.__nombre
    
    def set_tipo_producto(self, tipo_producto):
        self.__tipo_producto = tipo_producto

    @property
    def get_tipo_producto(self):
        return self.__tipo_producto
    
    def set_precio(self, precio):
        self.__precio = precio

    @property
    def get_precio(self):
        return self.__precio
    
    def set_stock(self, stock):
        self.__stock = stock

    @property
    def get_stock(self):
        return self.__stock