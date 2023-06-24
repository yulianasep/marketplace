class Usuario:
    def __init__(self, usuario: str, nombres: str, apellidos: str, identificacion: int):
        self.set_usuario(usuario)
        self.set_nombres(nombres)
        self.set_apellidos(apellidos)
        self.set_identificacion(identificacion)

    def __str__(self):
        return f"Usuario: {self.get_usuario}\nNombres: {self.get_nombres}\
        \nApellidos: {self.get_apellidos}\nIdentificación: {self.get_identificacion}"

    def set_usuario(self, usuario):
        self.__usuario = usuario

    @property
    def get_usuario(self):
        return self.__usuario

    def set_nombres(self, nombres):
        self.__nombres = nombres

    @property
    def get_nombres(self):
        return self.__nombres
    
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def get_apellidos(self):
        return self.__apellidos
    
    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    @property
    def get_identificacion(self):
        return self.__identificacion