import tkinter as tk
from PIL import Image, ImageTk
import random


class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.limpia = random.choice([True, False])
        self.ocupada = random.choice([True, False])

    def limpiar(self):
        self.limpia = True
        print(f"La habitación {self.nombre} ha sido limpiada.")

    def esta_limpia(self):
        return self.limpia

    def esta_ocupada(self):
        return self.ocupada

    def desocupar(self):
        self.ocupada = False
        print(f"La habitación {self.nombre} ahora está desocupada.")

class Aspiradora:
    def __init__(self, habitacion_inicial):
        self.habitacion_actual = habitacion_inicial
        print(f"La aspiradora inicia en la habitación {habitacion_inicial.nombre}.")

    def mover_a(self, habitacion):
        self.habitacion_actual = habitacion
        print(f"La aspiradora se ha movido a la habitación {habitacion.nombre}.")

    def intentar_limpiar_habitacion(self):
        if self.habitacion_actual.esta_ocupada():
            print(f"La habitación {self.habitacion_actual.nombre} está ocupada y no se puede limpiar en este momento.")
            return False
        elif self.habitacion_actual.esta_limpia():
            print(f"La habitación {self.habitacion_actual.nombre} ya está limpia.")
            return True
        else:
            self.habitacion_actual.limpiar()
            return True


class SimulacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Aspiradora")
        self.root.geometry("800x400")


        self.img_sucio = ImageTk.PhotoImage(Image.open("basura.png").resize((100, 100)))
        self.img_aspiradora = ImageTk.PhotoImage(Image.open("aspiradora.png").resize((100, 100)))


        self.habitacion_a = Habitacion("A")
        self.habitacion_b = Habitacion("B")
        self.aspiradora = Aspiradora(random.choice([self.habitacion_a, self.habitacion_b]))

        self.label_a = tk.Label(root, text="Habitación A", font=("Helvetica", 16))
        self.label_a.grid(row=0, column=0, padx=20, pady=20)
        self.label_a_img = tk.Label(root)
        self.label_a_img.grid(row=1, column=0)

        self.label_b = tk.Label(root, text="Habitación B", font=("Helvetica", 16))
        self.label_b.grid(row=0, column=2, padx=20, pady=20)
        self.label_b_img = tk.Label(root)
        self.label_b_img.grid(row=1, column=2)

        self.label_aspiradora = tk.Label(root, image=self.img_aspiradora)
        self.label_aspiradora.grid(row=1, column=1)

        self.label_accion = tk.Label(root, text="", font=("Helvetica", 14))
        self.label_accion.grid(row=2, column=1, pady=20)

        self.mostrar_estado()


        self.btn_start = tk.Button(root, text="Iniciar Simulación", command=self.ejecutar)
        self.btn_start.grid(row=3, column=1, pady=20)

    def mostrar_estado(self):

        if not self.habitacion_a.esta_limpia():
            self.label_a_img.config(image=self.img_sucio)
        else:
            self.label_a_img.config(image="")


        if not self.habitacion_b.esta_limpia():
            self.label_b_img.config(image=self.img_sucio)
        else:
            self.label_b_img.config(image="")


        if self.aspiradora.habitacion_actual.nombre == "A":
            self.label_aspiradora.grid(row=1, column=0)
        else:
            self.label_aspiradora.grid(row=1, column=2)

    def actualizar_accion(self, mensaje):
        self.label_accion.config(text=mensaje)

    def mover_aspiradora(self):

        if self.aspiradora.habitacion_actual == self.habitacion_a:
            self.aspiradora.mover_a(self.habitacion_b)
        else:
            self.aspiradora.mover_a(self.habitacion_a)

        self.mostrar_estado()
        self.root.update()
        self.root.after(1500)

    def ejecutar(self):
        habitaciones_revisadas = {self.habitacion_a: False, self.habitacion_b: False}
        habitaciones_ocupadas = []

        while True:
            print(f"\nLa aspiradora está en la habitación {self.aspiradora.habitacion_actual.nombre}.")


            if not self.aspiradora.habitacion_actual.esta_limpia():
                if self.aspiradora.intentar_limpiar_habitacion():
                    habitaciones_revisadas[self.aspiradora.habitacion_actual] = True
                    self.actualizar_accion(f"Limpieza completada en {self.aspiradora.habitacion_actual.nombre}.")
                else:
                    habitaciones_ocupadas.append(self.aspiradora.habitacion_actual)
                    self.actualizar_accion(f"La habitación {self.aspiradora.habitacion_actual.nombre} está ocupada.")
            else:
                habitaciones_revisadas[self.aspiradora.habitacion_actual] = True
                self.actualizar_accion(f"La habitación {self.aspiradora.habitacion_actual.nombre} ya está limpia.")

            self.mostrar_estado()
            self.root.after(1500)


            self.mover_aspiradora()


            if habitaciones_ocupadas:
                habitaciones_ocupadas[0].desocupar()
                habitaciones_ocupadas.pop(0)


            if all(habitaciones_revisadas.values()) and self.habitacion_a.esta_limpia() and self.habitacion_b.esta_limpia():
                self.actualizar_accion("¡Ambas habitaciones están limpias! Proceso terminado.")
                break

        self.mostrar_estado()

if __name__ == "__main__":
    root = tk.Tk()
    simulacion_gui = SimulacionGUI(root)
    root.mainloop()
