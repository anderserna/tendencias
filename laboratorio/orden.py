from datetime import datetime
class Orden: 

    contador_ordenes = 0
    

    def __init__(self, fecha_solicitud , medico, numero_orden_medico, paciente, examenes= []):
        Orden.contador_ordenes += 1
        self.id = Orden.contador_ordenes
        self.fecha_solicitud = fecha_solicitud 
        self.fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.medico = medico
        self.numero_orden_medico = numero_orden_medico
        self.examenes = examenes
        self.paciente = paciente

    def agregar_examen(self, examen):
        self.examenes.append(examen)

    def listar_examenes(self):
        if not self.examenes:
            print("No hay exámenes registrados para esta orden.")
            return
        print(f"Exámenes de la orden {self.id}:")
        for examen in self.examenes:
            print(f"Código: {examen.codigo}, Fecha: {examen.fecha}, Observaciones: {examen.observaciones}")
     
    def obtener_info(self):
        return f"Orden ID: {self.id}, Paciente: {self.paciente.nombre} {self.paciente.apellidos}, Fecha de Solicitud: {self.fecha_solicitud}, Médico: {self.medico.nombres} {self.medico.apellidos}, Observaciones: {self.observaciones}"
    

    def __str__(self):
        return self.obtener_info()
    