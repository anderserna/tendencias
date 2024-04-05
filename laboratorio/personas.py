class Persona:
    def __init__(self, id, tipo_id, nombres, apellidos, fecha_nac, celular, email, contacto_nombre, contacto_tel):
        self.id = id
        self.tipo_id = tipo_id
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nac = fecha_nac
        self.celular = celular
        self.email = email
        self.contacto_nombre = contacto_nombre
        self.contacto_tel = contacto_tel

    def imprimir_persona(self):
        print(f"ID: {self.id}")
        print(f"Tipo de ID: {self.tipo_id}")
        print(f"Nombres: {self.nombres}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Fecha de nacimiento: {self.fecha_nac}")
        print(f"Celular: {self.celular}")
        print(f"Email: {self.email}")
        print(f"Contacto de emergencia: {self.contacto_nombre}")
        print(f"Teléfono de contacto de emergencia: {self.contacto_tel}")
        print("\n")

