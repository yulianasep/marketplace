from CarritoCompra import CarritoCompra

class Compra:
    def __init__(self, carrito_compra: CarritoCompra):
        self.set_carrito_compra(carrito_compra)
        self.set_total_compra(self.calcular_total_compra())
    
    def __str__(self):
        return f"Carrito: {self.__carrito_compra}\nTotal: {self.__total_compra}"
    
    def set_carrito_compra(self, carrito_compra):
        self.__carrito_compra = carrito_compra

    @property
    def get_carrito_compra(self):
        return self.__carrito_compra    
    
    def set_total_compra(self, total_compra):
        self.__total_compra = total_compra

    def get_total_compra(self):
        return self.__total_compra
    
    def calcular_total_compra(self):
        total = 0
        for producto in self.__carrito_compra.get_productos:
            total += producto["precio"] * producto["cantidad"]
        print(total)