#Listado de expediente, debemos usar condiciones, ciclo,TODo!
#hacer un programa que permita llenar N cantadidas de datos
#1. listado de expedientes, 2. preguntar si desea seguir add (usar si/no), 3. listar rodos los expedientes con sus datos

datos = [] 
print("\t\t Nuevo expediente \n")

while True:
    dato = {}
    dato["ID del expediente"] = input("Ingrese el ID del expediente: ")
    dato["Conductor"] = input("Ingrese el nombre del coductor: ")
    dato["Aseguradora"] = input("Ingrese la aseguradora (ANCON .S.A., ASSA, MAPFRE, ACERTA): ")
    dato["Número de caso"] = input("Ingrese el número de caso: ")
    dato["Tipo de proceso"] = input("Tipo de proceso (pendiente, en curso, cerrado): ")
    datos.append(dato)

    seguir = input("¿Desea seguir agregando más expediente? (Si o No)")
    if seguir.lower() == "no":
        break

print("\t\tDatos Generales ")
for dato in datos:
    print("ID del expediente: ", dato["ID del expediente"])
    print("Conductor:" , dato["Conductor"])
    print("Aseguradora: ", dato["Aseguradora"])
    print("Número de caso:", dato["Número de caso"])
    print("Tipo de proceso:", dato["Tipo de proceso"])
    print("")

t_pendiente = 0
t_enproceso = 0
t_cerrado = 0

for dato in datos:
    if dato["Tipo de proceso"] == "pendiente":
        t_pendiente += 1
    elif dato["Tipo de proceso"] == "en curso":
        t_enproceso += 1
    elif dato["Tipo de proceso"] == "cerrado":
        t_cerrado += 1

print("Total de expedientes pendientes: ", t_pendiente)
print("total de expedientes en proceso: ", t_enproceso)
print("Total de expedientes cerrados: ", t_cerrado)