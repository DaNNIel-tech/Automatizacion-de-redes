# Práctica 03 - Representación de dispositivos de red con Python

1. Propósito de la práctica

El propósito de esta práctica fue desarrollar un programa básico en Python para representar y organizar la información de los dispositivos utilizados en nuestra red simulada en GNS3 durante la Práctica 2.

Utilizamos variables, diccionarios, listas, ciclos, condiciones y funciones para almacenar y mostrar los datos de dos routers y un switch. También realizamos pruebas para comprobar el funcionamiento del programa y observar cómo responde al modificar la información.

2. Conceptos utilizados

- **Variables:** permiten almacenar información como el nombre, dirección IP y estado de los dispositivos.
- **Tipos de datos:** utilizamos principalmente cadenas de texto (`str`) para representar los datos de nuestra red.
- **print():** permite mostrar información en la terminal de Python.
- **Diccionarios:** permiten organizar los datos de cada dispositivo mediante claves y valores.
- **Listas:** nos ayudan a agrupar varios dispositivos dentro de una misma estructura.
- **Ciclo for:** permite recorrer la lista y mostrar la información de todos los dispositivos.
- **Condicional if y else:** permite comprobar si un dispositivo está activo o requiere atención.
- **Funciones:** permiten reutilizar instrucciones y mantener nuestro programa organizado.

3. Dispositivos representados

Para desarrollar el programa utilizamos tres dispositivos de la infraestructura configurada anteriormente en GNS3.

| Dispositivo | Tipo | Dirección IP | Estado | Función |
|---|---|---|---|---|
| R1 | Router | 10.1.1.1 | Activo | Enrutamiento |
| R2 | Router | 10.1.1.2 | Activo | Enrutamiento |
| S1 | Switch | 10.1.1.3 | Activo | Conectividad de red |

Los routers R1 y R2 utilizan la plataforma Cisco IOSv y tienen configuradas las direcciones Loopback 1.1.1.1 y 2.2.2.2, respectivamente.

El switch S1 utiliza Cisco IOSvL2 y cuenta con la dirección IP 10.1.1.3 en la interfaz Vlan1.

La información se representa mediante diccionarios de Python y posteriormente se agrupa en una lista denominada `dispositivos`.

**Archivo del programa:** [dispositivos.py](../../src/dispositivos.py)

4. Evidencias y pruebas

Durante el desarrollo realizamos diferentes actividades para comprobar el funcionamiento del programa.

### Evidencias

1. Estructura del repositorio de GitHub.
2. Creación de las primeras variables en Python.
3. Ejecución correcta del primer programa.
4. Representación de los routers R1 y R2.
5. Uso de listas y diccionarios para almacenar dispositivos.
6. Ejecución del programa mostrando R1, R2 y S1.
7. Uso de condiciones y funciones para consultar el estado de los dispositivos.

Las capturas de pantalla se encuentran en la carpeta `evidencias/`.

### Tabla de pruebas

| Prueba | Resultado esperado | Resultado obtenido |
|---|---|---|
| Mostrar dispositivos | Visualizar todos los dispositivos | R1, R2 y S1 se muestran correctamente. |
| Mostrar IP | Mostrar las direcciones IP | Se muestran las IP registradas en Python. |
| Verificar estado | Identificar el estado de cada dispositivo | El programa distingue entre activo y fuera de servicio. |
| Modificar IP | Mostrar el nuevo valor | R1 muestra temporalmente 10.1.1.99. |
| Restaurar información | Recuperar la dirección original | R1 vuelve a mostrar 10.1.1.1. |

5. Problemas y soluciones

| Problema | Causa | Solución |
|---|---|---|
| No se podía ejecutar `git pull`. | La carpeta local no contenía el directorio `.git`. | Se clonó nuevamente el repositorio de GitHub en una carpeta diferente. |
| Necesidad de organizar la información de varios dispositivos. | Utilizar muchas variables individuales complicaba el código. | Se utilizaron diccionarios y una lista para organizar los datos. |
| El switch no tenía direcciones IP en sus puertos físicos. | La dirección de administración estaba configurada en Vlan1. | Se utilizó la dirección 10.1.1.3 de la interfaz Vlan1. |

6. Conclusión

Durante esta práctica aprendí a utilizar diferentes elementos de Python para representar la información de una red. Comprendí cómo funcionan las variables, los diccionarios, las listas y las funciones para organizar los datos de varios dispositivos. También aprendí a utilizar condiciones para identificar su estado y realizar pruebas modificando la información almacenada. Una de las partes más importantes fue relacionar nuestro programa con los dispositivos que configuramos anteriormente en GNS3. Considero que esta práctica nos ayudará en las siguientes actividades, ya que podremos mejorar el programa para obtener información directamente de los dispositivos y realizar tareas de automatización de redes.

7. Reto final: Búsqueda de dispositivos

Como parte del reto final, desarrollamos una función en Python que permite buscar dispositivos de nuestra red utilizando su nombre.

Para realizar esta tarea utilizamos un ciclo `for`, una condición `if` y la función `input()`, que permite ingresar información desde la terminal.

El programa recorre la lista de dispositivos y, cuando encuentra el nombre solicitado, muestra sus datos utilizando la función `mostrar_dispositivo()`.

También realizamos pruebas con dispositivos existentes y nombres que no están registrados, comprobando que el programa puede identificar ambas situaciones.

Esta función nos permitió comprender cómo podemos consultar información específica dentro de una infraestructura de red representada en Python.
