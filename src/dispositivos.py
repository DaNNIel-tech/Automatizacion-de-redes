
# Diccionario del Router R1
router1 = {
    "nombre": "R1",
    "tipo": "Router",
    "ip": "10.1.1.1",
    "loopback": "1.1.1.1",
    "interfaz": "GigabitEthernet0/0",
    "estado": "Activo",
    "fabricante": "Cisco",
    "plataforma": "Cisco IOSv",
    "funcion": "Enrutamiento"
}

# Diccionario del Router R2
router2 = {
    "nombre": "R2",
    "tipo": "Router",
    "ip": "10.1.1.2",
    "loopback": "2.2.2.2",
    "interfaz": "GigabitEthernet0/0",
    "estado": "Activo",
    "fabricante": "Cisco",
    "plataforma": "Cisco IOSv",
    "funcion": "Enrutamiento"
}

# Diccionario del Switch S1
switch1 = {
    "nombre": "S1",
    "tipo": "Switch",
    "ip": "10.1.1.3",
    "interfaz": "Vlan1",
    "estado": "Activo",
    "fabricante": "Cisco",
    "plataforma": "Cisco IOSvL2",
    "funcion": "Conectividad de red"
}

# Lista de dispositivos
dispositivos = [router1, router2, switch1]


def mostrar_dispositivo(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])

 
    if "loopback" in dispositivo:
        print("Loopback:", dispositivo["loopback"])

    print("Interfaz:", dispositivo["interfaz"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Plataforma:", dispositivo["plataforma"])
    print("Funcion:", dispositivo["funcion"])


    if dispositivo["estado"] == "Activo":
        print("El dispositivo esta disponible.")
    else:
        print("El dispositivo requiere atencion.")

# Mostrar todos los dispositivos
for dispositivo in dispositivos:
    mostrar_dispositivo(dispositivo)
    print("------------------------------")



def buscar_dispositivo(nombre_buscado):
    for dispositivo in dispositivos:
        if dispositivo["nombre"].lower() == nombre_buscado.lower():
            return dispositivo

    return None


print("\n===== BUSQUEDA DE DISPOSITIVOS =====")

nombre = input("Ingrese el nombre del dispositivo: ").strip()

# Buscar el dispositivo
resultado = buscar_dispositivo(nombre)

if resultado is not None:
    print("\nDispositivo encontrado:")
    mostrar_dispositivo(resultado)
else:
    print("\nNo se encontro el dispositivo.")
