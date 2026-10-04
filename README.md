Mi estación de automatización de redes
1. Datos del equipo

Materia: Automatización de Infraestructura Digital I
Grupo: 3IRI2V

Integrantes:
* Carlos Daniel Guillen Rios
* Carlos Uribe Herebia
* Diego Gael Guzman Flores
* Jesús Emilio Villlarreal Aleman


2. Propósito de la práctica

El propósito de esta práctica fue preparar nuestra computadora para trabajar con automatización de redes.
Para esto instalamos diferentes programas que vamos a utilizar durante las siguientes prácticas, como Python, VS Code, Git, GitHub, Docker y GNS3.
También hicimos algunas pruebas para comprobar que los programas funcionaran antes de seguir con las demás prácticas.


3. Herramientas instaladas

Durante la práctica instalamos:

* Python
* Visual Studio Code
* Git
* GitHub
* Postman
* OpenConnect
* Docker
* GNS3
* GNS3 VM
* VMware Workstation

También instalamos la extensión de Python en VS Code y creamos un entorno virtual.


4. Configuración realizada

Primero instalamos Python y comprobamos desde la terminal que funcionara.
Después instalamos VS Code y la extensión de Python. Creamos la carpeta "automatizacion-redes" y seleccionamos el intérprete de Python.
También creamos un entorno virtual para el proyecto.

Para comprobar que Python funcionaba, hicimos un archivo llamado "hola_mundo.py" y lo ejecutamos desde VS Code. El resultado fue:
"Hola Mundo"

Después instalamos Git y configuramos nuestro nombre y correo.
Creamos el repositorio de GitHub llamado "automatizacion-redes", donde vamos a guardar los archivos y evidencias de las prácticas.

También instalamos Postman, OpenConnect y Docker.

Por último instalamos GNS3, descargamos la GNS3 VM, instalamos VMware Workstation e importamos la máquina virtual. Después conectamos la GNS3 VM con GNS3.


5. Verificación del entorno

Al terminar revisamos que las herramientas funcionaran correctamente.

| Herramienta        | Resultado             |
| ------------------ | ------------------    |
| Python             | ☒ Funciona           |
| VS Code            | ☒ Funciona           |
| Python en VS Code  | ☒ Configurado        |
| Entorno virtual    | ☒ Funciona           |
| Hola Mundo         | ☒ Ejecutado          |
| Git                | ☒ Funciona           |
| Identidad de Git   | ☒ Configurada        |
| GitHub             | ☒ Repositorio creado |
| Postman            | ☒ Funciona           |
| OpenConnect        | ☒ Instalado          |
| Docker             | ☒ Funciona           |
| GNS3               | ☒ Funciona           |
| GNS3 VM            | ☒ Disponible         |
| VMware Workstation | ☒ Funciona           |
| GNS3 VM en VMware  | ☒ Importada          |
| GNS3 + GNS3 VM     | ☒ Integradas         |

También revisamos que la documentación y las evidencias estuvieran en el repositorio de GitHub.

6. Estructura del proyecto

El proyecto quedó organizado de esta manera:

```text
automatizacion-redes/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── hola_mundo.py
│
├── tests/
├── data/
│
└── docs/
    └── practica-01/
        ├── evidencias/
        │   ├── 01-python.png
        │   ├── 02-vscode.png
        │   ├── 03-python-vscode.png
        │   ├── 04-entorno-virtual.png
        │   ├── 05-hola-mundo.png
        │   ├── 06-git.png
        │   ├── 07-git-identidad.png
        │   ├── 08-github.png
        │   ├── 09-postman.png
        │   ├── 10-openconnect.png
        │   ├── 11-docker.png
        │   ├── 12-gns3.png
        │   ├── 13-gns3-vm.png
        │   ├── 14-vmware.png
        │   ├── 15-importacion-gns3-vm.png
        │   └── 16-integracion-gns3.png
        │
        ├── instalacion.md
        ├── configuracion.md
        └── verificacion.md
```
"README.md" tiene la información de la práctica.

"src" es donde se van a guardar los programas.

"tests" será para las pruebas.

"data" será para los datos que se utilicen.

"docs" tiene la documentación y las evidencias.

El archivo "requirements.txt" por ahora está vacío porque todavía no usamos bibliotecas externas de Python.


7. Problemas encontrados y soluciones

Durante la práctica tuvimos algunos problemas.

Con VMware Workstation no podíamos conseguir el instalador, así que tuvimos que pedírselo al profesor y nos lo pasó en una USB.

También tuvimos problemas para descargar la GNS3 VM porque el servidor donde estaba la descarga no estaba funcionando bien. Por eso la descarga no se podía hacer correctamente.

Con Git también tuvimos un pequeño problema porque se tuvo que agregar un `PATH` para poder conectarlo y usarlo correctamente.

Otro detalle fue que tuvimos que registrarnos en algunos programas y servicios, lo cual tomó un poco de tiempo, pero después pudimos continuar.


8. Conclusiones

En esta práctica instalamos varios programas que vamos a necesitar para trabajar en automatización de redes.
Al principio tuvimos algunos problemas con VMware, GNS3 VM y Git, pero pudimos solucionarlos y continuar con la práctica.
También aprendimos que los programas se van a usar juntos. Por ejemplo, usamos Python y VS Code para programar, Git y GitHub para guardar el proyecto,
Docker para trabajar con contenedores y GNS3 con VMware para hacer las prácticas de redes.

9. Avance del proyecto integrador

### Práctica 1

Preparación de la estación de automatización de redes.

Estado: Completada.

Durante esta práctica preparamos las herramientas necesarias para comenzar a trabajar con automatización de redes, como Python, VS Code, Git, GitHub, Docker, GNS3, GNS3 VM y VMware Workstation.

### Práctica 2

Construcción de la red simulada en GNS3.

Estado: Completada.

Durante esta práctica construimos y configuramos dos topologías de red en GNS3.

Infraestructura construida:

* Topología básica PC-Switch-PC.
* Topología con dos routers Cisco IOSv y un switch multicapa Cisco IOSvL2.
* Configuración de direccionamiento IP.
* Pruebas de conectividad mediante ping.
* Configuración de interfaces Loopback.
* Configuración del protocolo OSPF.
* Verificación de vecinos OSPF.
* Verificación de la tabla de enrutamiento.

La primera topología permitió comprobar la comunicación entre dos computadoras conectadas mediante un switch.

La segunda topología permitió trabajar con routers y un switch multicapa, configurar sus interfaces y utilizar OSPF para intercambiar información de enrutamiento.

