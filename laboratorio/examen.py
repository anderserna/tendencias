class Examen:

    def __init__(self, codigo, fecha_realizacion, observaciones,nombre,valor):
        self.codigo = codigo
        self.fecha_realizacion = fecha_realizacion
        self.observaciones = observaciones
        self.valor = valor
        self.nombre = nombre
    
    def imprimir_examen(self):
        print(f"Examen: {self.nombre}, Código: {self.codigo}, Fecha de realización: {self.fecha_realizacion}, Observaciones: {self.observaciones}, Valor: {self.valor}")

    def __str__(self):
        return f"{self.nombre}, Código: {self.codigo}, Valor: {self.valor}"