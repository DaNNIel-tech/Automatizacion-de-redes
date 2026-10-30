# Práctica 05: Mi primer script de automatización

## Integrantes

 Carlos Daniel Guillen Rios
 Carlos Uribe Herbia
 Diego Gael Guzmán Flores
 Jesús Emilio Villarreal Alemán

## 1. Objetivo

Desarrollar un script en Python que permita automatizar la configuración de un router Cisco IOSv mediante el protocolo Telnet, utilizando el Network Automation Container (NAC) dentro del simulador GNS3.

La práctica contempla la creación de interfaces Loopback, la configuración del protocolo OSPF y la verificación de los resultados.

## 2. Relación con las prácticas anteriores

Esta actividad da continuidad a las prácticas de automatización de redes, en las que se preparó el entorno de trabajo y se realizaron configuraciones de dispositivos en GNS3.

En esta ocasión se utiliza Python para enviar comandos de configuración a un router de manera remota, aplicando los conocimientos adquiridos anteriormente.

## 3. Topología y direccionamiento

La topología está formada por cinco dispositivos:

| Dispositivo | Función |
|---|---|
| NAC1 | Ejecutar los scripts de automatización. |
| Ethernet Switch | Interconectar los dispositivos. |
| NAT | Proporcionar conectividad y servicio DHCP. |
| Cisco IOSvL2 | Realizar la conmutación de capa 2. |
| R1 | Recibir las configuraciones automatizadas. |

### Direccionamiento utilizado

Se utilizó una red privada de laboratorio con direccionamiento IPv4.

| Interfaz | Configuración |
|---|---|
| NAC1 | Dirección privada mediante DHCP |
| R1 - GigabitEthernet0/0 | Dirección estática de la red del laboratorio |
| Loopback0 | 1.1.1.1/32 |
| Loopback1 | 2.2.2.2/32 |

La información específica de acceso a los dispositivos no se publica en este documento.

## 4. Herramientas y entorno

 GNS3 y GNS3 VM.
 VMware Workstation.
 Network Automation Container.
 Python y biblioteca telnetlib.
 Protocolo Telnet.
 Wireshark.
 Visual Studio Code.
 Git y GitHub.

**Versión de Python:** Pendiente de confirmar mediante `python3 --version` en NAC1.

## 5. Desarrollo de la práctica

### 5.1. Preparación del entorno

Se creó un proyecto en GNS3 y se incorporaron los dispositivos necesarios para construir la topología.

Posteriormente, se configuró el NAC para obtener una dirección IP mediante DHCP y se realizaron pruebas de conectividad.

### 5.2. Configuración de R1

Se configuró la interfaz de red del router Cisco IOSv y se habilitó el acceso remoto mediante Telnet utilizando autenticación local.

Las credenciales empleadas se mantienen fuera del repositorio.

### 5.3. Desarrollo del script

Se creó un archivo Python utilizando la biblioteca telnetlib para establecer una conexión remota con R1.

El script permite establecer una sesión Telnet, acceder al modo de configuración, crear interfaces Loopback y configurar OSPF.

El código desarrollado se almacena en `src/automatizacion_telnet.py`.

### 5.4. Configuración de Loopback

Mediante el script se configuraron dos interfaces virtuales:

 Loopback0: 1.1.1.1/32.
 Loopback1: 2.2.2.2/32.

La configuración se comprobó utilizando `show ip interface brief`.

### 5.5. Configuración de OSPF

Se configuró el proceso OSPF 1 utilizando el área 0.

Para comprobar su funcionamiento se utilizó el comando `show ip ospf interface brief`, verificando las interfaces participantes.

## 6. Tabla de pruebas

| Prueba | Herramienta o comando | Resultado |
|---|---|---|
| Direccionamiento del NAC | `ifconfig` | Dirección IPv4 obtenida. |
| Conectividad de red | `ping` | Pruebas de conectividad realizadas. |
| Acceso remoto | Telnet | Acceso comprobado durante la práctica. |
| Ejecución del script | Python | Ejecución realizada en NAC. |
| Interfaces Loopback | `show ip interface brief` | Interfaces configuradas. |
| Configuración OSPF | `show ip ospf interface brief` | Interfaces participantes verificadas. |

Los resultados finales se respaldan con las evidencias correspondientes.

## 7. Problemas y soluciones

### Problema 1. Aceleración de virtualización

Durante la preparación del entorno se presentaron dificultades para utilizar la aceleración KVM.

Se revisó la configuración de virtualización y se realizaron los ajustes necesarios para habilitar la aceleración.

### Problema 2. Actualización de paquetes

Durante la actualización del NAC se detectó un problema relacionado con la verificación de un repositorio de software.

Se identificó el repositorio que generaba el error y se realizaron los ajustes necesarios para continuar con la actividad.

### Problema 3. Problemas de conectividad

Se detectaron fallas de comunicación entre los dispositivos de la topología.

Para investigar el problema se utilizaron herramientas de diagnóstico como ping, comandos de Cisco IOS y Wireshark.

También se identificó que uno de los switches estaba ejecutándose en un servidor diferente, por lo que se revisó la ubicación de los dispositivos dentro de GNS3.

## 8. Evidencias

Las capturas se almacenan en `docs/practica-05/evidencias/`.

| Evidencia | Archivo |
|---|---|
| Topología de GNS3 | [01-topologia.png](evidencias/01-topologia.png) |
| Direccionamiento del NAC | [02-ip_nac.png](evidencias/02-ip_nac.png) |
| Conectividad hacia R1 | [03-conectividad-r1.png](evidencias/03-conectividad-r1.png) |
| Acceso Telnet | [04-acceso-telnet.png](evidencias/04-acceso-telnet.png) |
| Ejecución del script | [05-ejecucion-script.png](evidencias/05-ejecucion-script.png) |
| Interfaces Loopback | [06-interfaces-loopback.png](evidencias/06-interfaces-loopback.png) |
| Configuración OSPF | [07-configuracion-ospf.png](evidencias/07-configuracion-ospf.png) |


Las capturas deben ocultar credenciales y cualquier información privada.

## 9. Conclusiones individuales

### Carlos Daniel Guillen Rios

Esta práctica me permitió comprender mejor cómo se puede utilizar Python para automatizar configuraciones en dispositivos de red. Aunque tuvimos algunos problemas con la conectividad y la máquina virtual, logramos avanzar mediante diferentes pruebas. También aprendí que antes de ejecutar un script es importante comprobar que los dispositivos puedan comunicarse correctamente.

### Carlos Uribe Herbia

Una de las cosas que aprendí durante esta actividad fue cómo funciona la conexión Telnet entre un contenedor y un router Cisco. Me pareció interesante que mediante un programa se puedan ejecutar diferentes configuraciones sin escribir cada comando directamente en el router. Además, reforcé mis conocimientos sobre el uso de GNS3 y la administración de dispositivos.

### Diego Gael Guzmán Flores

Al realizar esta práctica pude conocer mejor las interfaces Loopback y la configuración del protocolo OSPF. También comprendí cómo se relacionan estos elementos con la automatización de redes. Considero que fue una actividad útil porque nos permitió aplicar conocimientos de programación y redes dentro de un mismo entorno de trabajo.

### Jesús Emilio Villarreal Alemán

Lo que más me dejó esta actividad fue aprender a identificar problemas durante la configuración de una red. Tuvimos que revisar interfaces, conexiones y diferentes parámetros para encontrar posibles fallas. Esto me ayudó a entender que en la automatización no solamente importa que el código funcione, sino también que toda la infraestructura esté correctamente preparada.

## 10. Relación con el proyecto integrador

Esta práctica representa un avance en el proyecto integrador de automatización de redes, al permitir la configuración remota de un dispositivo Cisco mediante Python.

El script desarrollado constituye una base para implementar otras tareas de automatización dentro de la infraestructura de red.

## 11. Repositorio

El código y las evidencias se encuentran organizados en:

Script: `src/automatizacion_telnet.py`.
Documentación: `docs/practica-05/README.md`.
Evidencias: `docs/practica-05/evidencias/`.
