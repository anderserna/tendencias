from personas import Persona

class Paciente(Persona):
    def __init__(self, id, tipo_id, nombres, apellidos, fecha_nac, celular, email, contacto_nombre, contacto_tel, tipo_paciente):
        super().__init__(id, tipo_id, nombres, apellidos, fecha_nac, celular, email, contacto_nombre, contacto_tel)
        self.ordenes = []
        self.tipo_paciente = tipo_paciente
        
    def agregar_orden(self, orden):
        self.ordenes.append(orden)

    def registrar_paciente(cls):
        id = input("Ingrese el ID del paciente: ")
        tipo_id = input("Ingrese el tipo de ID del paciente: ")
        nombres = input("Ingrese los nombres del paciente: ")
        apellidos = input("Ingrese los apellidos del paciente: ")
        fecha_nac = input("Ingrese la fecha de nacimiento del paciente: ")
        celular = input("Ingrese el celular del paciente: ")
        email = input("Ingrese el email del paciente: ")
        contacto_nombre = input("Ingrese el nombre del contacto de emergencia: ")
        contacto_tel = input("Ingrese el teléfono del contacto de emergencia: ")
        tipo_paciente = input("Ingrese el tipo de paciente: ")

        paciente = Paciente(id, tipo_id, nombres, apellidos, fecha_nac, celular, email, contacto_nombre, contacto_tel, tipo_paciente)
        Pacientes.append(paciente)
        print("Paciente registrado correctamente.")

    def listar_ordenes(self):
        if not self.ordenes:
            print("No hay órdenes registradas para este paciente.")
            return
        for orden in self.ordenes:
            print(f"Orden ID: {orden.id}, Fecha de Solicitud: {orden.fecha_solicitud}, Médico: {orden.medico.nombres} {orden.medico.apellidos}")

    def obtener_total_facturas(self):
        total = 0
        for orden in self.ordenes:
             for examen in orden.examenes:
                total += examen.valor
        return total
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}, ID: {self.id}, Tipo de paciente: {self.tipo_paciente}"