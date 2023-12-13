import tkinter as tk
from djitellopy import Tello
import time

# Definir una clase para el controlador del dron
class DroneController:
    def __init__(self):
        # Inicializar una instancia del dron Tello y la interfaz gráfica de Tkinter
        self.tello = Tello()
        self.root = tk.Tk()
        self.root.title("Tello Drone Controller")

        # Crear botones en la interfaz para realizar acciones específicas
        self.takeoff_button = tk.Button(self.root, text="Despegar", command=self.takeoff)
        self.takeoff_button.pack(pady=10)

        self.land_button = tk.Button(self.root, text="Aterrizar", command=self.land)
        self.land_button.pack(pady=10)

        self.square_button = tk.Button(self.root, text="Realizar Cuadrado", command=self.perform_square)
        self.square_button.pack(pady=10)

        self.triangle_button = tk.Button(self.root, text="Realizar Triángulo", command=self.perform_triangle)
        self.triangle_button.pack(pady=10)

        self.octagon_button = tk.Button(self.root, text="Realizar Octágono", command=self.perform_octagon)
        self.octagon_button.pack(pady=10)

        # Configurar la acción a realizar al cerrar la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    # Método para despegar el dron
    def takeoff(self):
        self.tello.connect()
        self.tello.takeoff()

    # Método para aterrizar el dron
    def land(self):
        self.tello.land()

    # Método para realizar un cuadrado con el dron
    def perform_square(self):
        # Realizar un cuadrado más pequeño
        for _ in range(4):
            self.tello.move_forward(50)
            time.sleep(1)
            self.tello.rotate_clockwise(90)
            time.sleep(0.5)

    # Método para realizar un triángulo con el dron
    def perform_triangle(self):
        # Realizar un triángulo más pequeño
        for _ in range(3):
            self.tello.move_forward(50)
            time.sleep(1)
            self.tello.rotate_clockwise(120)
            time.sleep(0.5)

    # Método para realizar un octágono con el dron
    def perform_octagon(self):
        # Realizar un octágono más pequeño
        for _ in range(8):
            self.tello.move_forward(50)
            time.sleep(1)
            self.tello.rotate_clockwise(45)
            time.sleep(0.5)

    # Método llamado al cerrar la ventana
    def on_closing(self):
        # Aterrizar el dron y cerrar la ventana
        self.tello.land()
        self.root.destroy()

    # Método para ejecutar la interfaz gráfica
    def run(self):
        self.root.mainloop()

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Crear una instancia del controlador y ejecutar la interfaz gráfica
    controller = DroneController()
    controller.run()
