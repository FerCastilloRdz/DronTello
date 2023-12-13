from djitellopy import Tello
import time

# Crear objeto Tello
tello = Tello()

# Conectar a Tello
tello.connect()

# Imprimir nivel de batería
print(f"Batería: {tello.get_battery()}%")

# Despegue
tello.takeoff()
time.sleep(2)  # Permitir tiempo para el despegue

# Patrón cuadrado
longitud_lado = 40
for _ in range(4):
    tello.move_forward(longitud_lado)
    time.sleep(2)  # Permitir tiempo para que el dron se desplace hacia adelante
    tello.rotate_clockwise(90)
    time.sleep(2)  # Permitir tiempo para que el dron rote

# Elevación después del cuadrado
tello.move_up(30)  # Eleva el dron 30 cm
time.sleep(2)      # Espera 2 segundos

# Patrón triángulo
longitud_lado = 40
for _ in range(3):
    tello.move_forward(longitud_lado)
    time.sleep(4)  # Permitir tiempo para que el dron se desplace hacia adelante
    tello.rotate_clockwise(120)
    time.sleep(4)  # Permitir tiempo para que el dron rote

# Elevación después del triángulo
tello.move_up(30)  # Eleva el dron 30 cm
time.sleep(2)      # Espera 2 segundos

# Patrón octágono
longitud_lado_octagono = 30
for _ in range(8):
    tello.move_forward(longitud_lado_octagono)
    time.sleep(3)  # Permitir tiempo para que el dron se desplace hacia adelante
    tello.rotate_clockwise(45)
    time.sleep(3)  # Permitir tiempo para que el dron rote

# Aterrizar al finalizar el octágono
tello.land()

