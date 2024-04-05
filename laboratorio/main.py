#Cada examen tiene un atributo de valor 
#Menu donde vamos a poder crear una orden, agregar examenes a la orden, listar examenes de la orden, listar ordenes de un paciente, listar total de facturas de un paciente

from datetime import datetime
from orden import Orden
from examen import Examen
from factura import Factura
from paciente import Paciente
from personas import Persona
from medico import Medico
from entidad_salud import Entidad

pacientes = []
examenes = []
ordenes = []
facturas = []



def crear_examen():
    codigo = input("Ingrese el código del examen: ")
    fecha = input("Ingrese la fecha del examen: ")
    observaciones = input("Ingrese las observaciones del examen: ")
    valor = float(input("Ingrese el valor del examen: "))

    examen = Examen(codigo, fecha, observaciones, valor)
    examenes.append(examen)
    print("Examen creado correctamente.")

def crear_orden():
    fecha_solicitud = input("Ingrese la fecha de solicitud de la orden: ")
    medico = input("Ingrese el médico de la orden: ")
    numero_orden_medico = input("Ingrese el número de orden del médico: ")
    paciente_id = input("Ingrese el ID del paciente: ")
    examenes_orden = []

    paciente = next((paciente for paciente in pacientes if paciente.id == paciente_id), None)
    if not paciente:
        print("Paciente no encontrado.")
        return

    while True:
        examen_codigo = input("Ingrese el código del examen a agregar a la orden (o '0' para salir): ")
        if examen_codigo == '0':
            break

        examen = next((examen for examen in examenes if examen.codigo == examen_codigo), None)
        if not examen:
            print("Examen no encontrado.")
            continue

        examenes_orden.append(examen)

    orden = Orden(fecha_solicitud, medico, numero_orden_medico, paciente, examenes_orden)
    ordenes.append(orden)
    paciente.agregar_orden(orden)
    print("Orden creada correctamente.")

def listar_examenes_orden():
    orden_id = int(input("Ingrese el ID de la orden: "))
    orden = next((orden for orden in ordenes if orden.id == orden_id), None)
    if not orden:
        print("Orden no encontrada.")
        return

    orden.listar_examenes()

def listar_ordenes_paciente():
    paciente_id = input("Ingrese el ID del paciente: ")
    paciente = next((paciente for paciente in pacientes if paciente.id == paciente_id), None)
    if not paciente:
        print("Paciente no encontrado.")
        return

    paciente.listar_ordenes()

def listar_total_facturas_paciente(): 
    paciente_id = input("Ingrese el ID del paciente: ")
    paciente = next((paciente for paciente in pacientes if paciente.id == paciente_id), None)
    if not paciente:
        print("Paciente no encontrado.")
        return

    total = paciente.obtener_total_facturas()
    print(f"El total de facturas del paciente es: {total}")

def crear_factura():
    orden_id = int(input("Ingrese el ID de la orden: "))
    orden = next((orden for orden in ordenes if orden.id == orden_id), None)
    if not orden:
        print("Orden no encontrada.")
        return

    factura = Factura(orden)
    facturas.append(factura)
    print("Factura creada correctamente.")

def menu():
    while True:
        print("Menú:")
        print("1. Registrar paciente")
        print("2. Crear examen")
        print("3. Crear orden")
        print("4. Listar exámenes de una orden")
        print("5. Listar órdenes de un paciente")
        print("6. Listar total de facturas de un paciente")
        print("7. Crear factura")
        print("8. Salir")

        opcion = input("Ingrese la opción deseada: ")
        if opcion == '1':
            reistrar_paciente()
        elif opcion == '2':
            crear_examen()
        elif opcion == '3':
            crear_orden()
        elif opcion == '4':
            listar_examenes_orden()
        elif opcion == '5':
            listar_ordenes_paciente()
        elif opcion == '6':
            listar_total_facturas_paciente()
        elif opcion == '7':
            crear_factura()
        elif opcion == '8':
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    menu()

