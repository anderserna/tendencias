class Entidad:
    def __init__(self, nit,telefonos,celular,correo,otro_contacto, telefono_otro_contacto,tipo_entidad_prestadora):
        self.nit = nit
        self.telefonos = telefonos
        self.celular = celular
        self.correo = correo
        self.otro_contacto = otro_contacto
        self.telefono_otro_contacto = telefono_otro_contacto
        self.tipo_entidad_prestadora = tipo_entidad_prestadora


    def imprimir_entidad(self):
        print(f"NIT: {self.nit}")
        print(f"Teléfonos: {self.telefonos}")
        print(f"Celular: {self.celular}")
        print(f"Correo: {self.correo}")
        print(f"Otro contacto: {self.otro_contacto}")
        print(f"Teléfono otro contacto: {self.telefono_otro_contacto}")
        print(f"Tipo de entidad prestadora: {self.tipo_entidad_prestadora}")
        print("\n")


