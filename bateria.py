# Importar la clase Tello desde el módulo djitellopy
from djitellopy import Tello

# Crear una instancia de la clase Tello
tello = Tello()

# Conectar con el dron Tello
tello.connect()

# Imprimir el nivel de batería del dron Tello
print(tello.get_battery())

#-----------------------------------------------------
# from djitellopy import Tello: Importa la clase Tello desde el módulo 
# djitellopy, que proporciona una interfaz para interactuar con el dron Tello.

# tello = Tello(): Crea una instancia del objeto Tello. 
# Esta instancia se utilizará para enviar comandos al dron y recibir información de él.

#tello.connect(): Establece una conexión con el dron Tello. 
# Antes de enviar comandos al dron, es necesario establecer una conexión.

# print(tello.get_battery()): Obtiene el nivel de batería actual del dron Tello y lo imprime en la consola. 
# get_battery() es un método proporcionado por la biblioteca djitellopy para obtener la información sobre la batería del dron.

# En resumen, este código se conecta al dron Tello, obtiene y muestra en la consola el nivel actual de la batería del dron. 
