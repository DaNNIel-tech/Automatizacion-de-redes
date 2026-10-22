### 1. Tabla comparativa de confiabilidad

## Evaluación de confiabilidad de los recursos

| Criterio | Documentación de Python | Documentación de GNS3 | Repositorio de Netmiko |
|---|---|---|---|
| ¿Quién publica o mantiene el recurso? | Python Software Foundation y colaboradores del proyecto Python. | Equipo y colaboradores del proyecto GNS3. | Desarrolladores y colaboradores del proyecto Netmiko. |
| ¿La información corresponde al tema investigado? | Sí, explica el lenguaje Python y sus funciones. | Sí, aborda la simulación y configuración de redes. | Sí, se relaciona con la automatización de dispositivos mediante Python. |
| ¿Incluye ejemplos o instrucciones verificables? | Sí, contiene ejemplos y explicaciones de código. | Sí, ofrece guías y procedimientos de configuración. | Sí, incluye ejemplos de conexión y uso de la biblioteca. |
| ¿Se identifica la versión o fecha de actualización cuando corresponde? | Sí, permite consultar documentación de distintas versiones de Python. | La información puede incluir versiones y requisitos según la guía consultada. | Sí, mediante las versiones publicadas y el historial de cambios de GitHub. |
| ¿Es posible comprobar la información con otra fuente? | Sí, mediante ejemplos prácticos y otras referencias técnicas. | Sí, realizando pruebas en GNS3 y consultando otras guías. | Sí, consultando su documentación y probando ejemplos compatibles. |
| ¿Qué utilidad tiene para el proyecto integrador? | Ayuda a desarrollar y corregir programas en Python. | Permite construir y solucionar problemas de la topología de red. | Facilita investigar cómo automatizar tareas de administración de dispositivos. |

### 2. Preguntas de análisis

1. ¿Cuál de los recursos consideras más útil para resolver dudas de Python? ¿Por qué?

La documentación oficial de Python, porque contiene información confiable sobre el lenguaje, ejemplos de código y explicaciones que ayudan a resolver errores durante la programación.

2. ¿Cuál consultarías para resolver un problema relacionado con GNS3?

Consultaría la documentación oficial de GNS3, ya que ofrece guías para configurar dispositivos, crear topologías y solucionar problemas relacionados con el funcionamiento de la red simulada.

3. ¿Por qué no conviene copiar directamente una solución sin comprobar que funciona en el entorno de trabajo?

Porque una solución puede estar diseñada para otra versión del programa, sistema operativo o configuración. Es importante comprobar que funciona correctamente para evitar errores y problemas en el proyecto.

### 3. Fuentes consultadas

1. **Documentación oficial de Python**
   https://docs.python.org/es/3/
   - Información sobre sintaxis, funciones y estructuras de datos.

2. **Documentación oficial de GNS3**
   https://docs.gns3.com/
   - Guías sobre configuración, simulación y solución de problemas de redes.

3. **Repositorio de Netmiko**
   https://github.com/ktbyers/netmiko
   - Biblioteca de Python para automatizar la administración de dispositivos de red.

### 3.Analisis de un problema técnico hipotético

1. situacion

El programa dispositivos.py, desarrollado en la Práctica 3, muestra correctamente la información de R1 y R2, pero al intentar buscar un dispositivo por su nombre, el programa no identifica el equipo solicitado.

2. Tabla de estrategia

## Estrategia de solución de un problema técnico

| Elemento | Respuesta del equipo |
|---|---|
| Problema identificado | El programa dispositivos.py muestra correctamente los datos de R1 y R2, pero no encuentra un dispositivo cuando se busca por su nombre. |
| Palabras clave para realizar la búsqueda | Python buscar elementos en lista de diccionarios, comparar cadenas en Python, método lower(), búsqueda de dispositivos por nombre. |
| Documentación o comunidad que consultarían primero | La documentación oficial de Python, especialmente los apartados relacionados con listas, diccionarios y comparación de cadenas. |
| Información que revisarían en el código | La estructura de los datos, los nombres registrados, el ciclo utilizado para buscar y las condiciones que comparan los nombres de los dispositivos. |
| Tipo de ejemplo o solución que buscarían | Ejemplos de cómo recorrer listas de diccionarios y comparar nombres utilizando condicionales y el método lower(). |
| Cómo comprobarían que la solución funciona | Realizando búsquedas de R1 y R2, probando nombres con mayúsculas y minúsculas, y verificando que el programa muestre la información correcta. |
| Cómo documentarían la solución encontrada | Registrando el problema, las causas identificadas, los recursos consultados, la solución propuesta y los resultados de las pruebas en GitHub. |

3. Ejemplo de una posible solución

dispositivos = [
    {"nombre": "R1", "ip": "192.168.1.1"},
    {"nombre": "R2", "ip": "192.168.1.2"}
]

nombre_buscar = input("Ingrese el nombre del dispositivo: ")

for dispositivo in dispositivos:
    if dispositivo["nombre"].lower() == nombre_buscar.lower():
        print("Dispositivo encontrado:", dispositivo)
        break
else:
    print("Dispositivo no encontrado")

El programa recorre los dispositivos y compara sus nombres utilizando lower(), que convierte el texto a minúsculas. Esto permite encontrar un dispositivo aunque el usuario escriba r1, R1 o R2. Las direcciones IP son ilustrativas.
