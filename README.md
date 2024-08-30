# DronTello Demostraciones de vuelo
# Universidad de Guanajuato FIMEE-2023

Codigo Creado por; Fernando Castillo Rodriguez.

° Codigo Bateria, este código se conecta al dron Tello, obtiene y muestra en la consola el nivel actual de la batería del dron. 

° Codigo Control, crea una interfaz gráfica simple para controlar un dron Tello, permitiendo despegar, aterrizar y realizar movimientos específicos en forma de cuadrado, triángulo y octágono. La interfaz utiliza la biblioteca Tkinter, mientras que la interacción con el dron se realiza mediante la biblioteca djitellopy.

° Codigo Elevacion, el código conecta y controla un dron Tello para realizar un patrón cuadrado, seguido de una elevación, un patrón triángulo, otra elevación, y finalmente un patrón octágono, concluyendo con el aterrizaje del dron. Las pausas (time.sleep()) se utilizan para permitir que el dron complete cada movimiento antes de realizar el siguiente.

# Proyecto de Control de Dron Tello con Tkinter y djitellopy

Introducción:
Este proyecto tiene como objetivo el control de un dron Tello mediante una interfaz gráfica implementada en Tkinter. Utiliza la biblioteca `djitellopy` para interactuar con el dron y realizar movimientos específicos, creando patrones geométricos.

Parte 1: Interfaz Gráfica

- Clase `DroneController`:
   - `__init__` - Inicialización:
     - Inicia el dron Tello y la interfaz gráfica de Tkinter.
     - Crea botones para acciones y configura la acción de cierre de la ventana para aterrizar el dron.
   - `takeoff` - Despegue:
     - Conecta al dron y lo hace despegar.
   - `land` - Aterrizaje:
     - Hace que el dron aterrice.
   - `perform_square`, `perform_triangle`, `perform_octagon` - Movimientos Geométricos:
     - Realizan movimientos específicos para formar un cuadrado, triángulo y octágono.
   - `on_closing` - Cierre de Ventana:
     - Aterriza el dron y cierra la ventana.
   - `run` - Ejecución de Interfaz:
     - Inicia el bucle principal de la interfaz gráfica.

Script de Ejecución de Interfaz Gráfica:
   - Crea una instancia de `DroneController` y ejecuta la interfaz gráfica.

Parte 2: Control de Dron Tello con Movimientos Específicos

- Script de Control de Dron Tello:
   - Creación y Conexión a Tello:
     - Se crea un objeto `Tello` para representar el dron y se establece la conexión.
   - Obtención y Visualización del Nivel de Batería:
     - Se obtiene y muestra el nivel de batería del dron.
   - Despegue:
     - El dron despega y espera 2 segundos.
   - Patrones Geométricos:
     - Realiza movimientos para formar un cuadrado, triángulo y octágono.
   - Elevación:
     - Eleva el dron 30 cm y espera 2 segundos.
   - Aterrizaje:
     - Aterriza el dron al finalizar los patrones.

Conclusiones:
Este proyecto demuestra la integración de una interfaz gráfica con la capacidad de controlar un dron Tello. 
La interfaz permite acciones intuitivas, mientras que el script controla el dron para realizar movimientos geométricos. Puede servir como base para futuras ampliaciones y desarrollos.

Posibles Mejoras y Desarrollos Futuros:
- Implementación de más movimientos y patrones geométricos.
- Integración de funciones avanzadas como seguimiento de objetos o reconocimiento de patrones.
- Mejora de la interfaz gráfica con información en tiempo real del dron.


