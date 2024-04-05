class Medico: 
    def __init__(self, cedula, nombre, apellidos, numero_celular, direccion, num_tarjeta_pro):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_celular = numero_celular
        self.direccion = direccion
        self.num_tarjeta_pro = num_tarjeta_pro
 
    def imprimir_medico(self):
        print(f"Cédula: {self.cedula}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Celular: {self.numero_celular}")
        print(f"Dirección: {self.direccion}")
        print(f"Número de tarjeta profesional: {self.num_tarjeta_pro}")
        print("\n")

