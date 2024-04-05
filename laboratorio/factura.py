class Factura:

    secuencia_factura = 0

    def __init__(self,orden):
        Factura.secuencia_factura += 1
        self.numero_factura = Factura.secuencia_factura 
        self.valor_total = self.calcular_valor_total()
        self.fecha_creacion = self.fecha_creacion()
        self.detalle_factura = self.detalle_factura()
        self.orden = orden
        self.paciente = orden.paciente

    def calcular_valor_total(self):
        total = sum(examen.valor for examen in self.orden.examenes) 
        return total

    def fecha_creacion(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def detalle_factura(self):
        detalle = []
        for examen in self.orden.examenes:
            detalle.append(f"Examen: {examen.nombre}, Valor: {examen.valor}")
        return detalle

    def imprimir_factura(self):
        print(f"Factura N°: {self.numero_factura}")
        print(f"Fecha de creación: {self.fecha_creacion}")
        print(f"Paciente: {self.paciente.nombres} {self.paciente.apellidos}")
        print(f"Valor total: {self.valor_total}")
        print("Detalle de la factura:")
        for examen in self.detalle_factura:
            print(examen)
        print("")


        
