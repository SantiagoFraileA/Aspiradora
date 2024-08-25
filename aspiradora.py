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

def simular_proceso_limpieza():
    # Crear habitaciones
    habitacion_a = Habitacion("A")
    habitacion_b = Habitacion("B")

    print(f"Estado inicial:")
    print(f"Habitación A: {'Limpia' if habitacion_a.esta_limpia() else 'Sucia'}, {'Ocupada' if habitacion_a.esta_ocupada() else 'Desocupada'}")
    print(f"Habitación B: {'Limpia' if habitacion_b.esta_limpia() else 'Sucia'}, {'Ocupada' if habitacion_b.esta_ocupada() else 'Desocupada'}")
    

    habitacion_inicial = random.choice([habitacion_a, habitacion_b])
    aspiradora = Aspiradora(habitacion_inicial)
    

    habitaciones_revisadas = {habitacion_a: False, habitacion_b: False}
    habitaciones_ocupadas = []

    # Proceso de limpieza
    while True:
        print(f"\nLa aspiradora está en la habitación {aspiradora.habitacion_actual.nombre}.")
        

        if aspiradora.intentar_limpiar_habitacion():
            habitaciones_revisadas[aspiradora.habitacion_actual] = True
        else:
            habitaciones_ocupadas.append(aspiradora.habitacion_actual)
        

        if aspiradora.habitacion_actual == habitacion_a:
            aspiradora.mover_a(habitacion_b)
        else:
            aspiradora.mover_a(habitacion_a)


        if habitaciones_ocupadas:
            habitaciones_ocupadas[0].desocupar()
            habitaciones_ocupadas.pop(0)


        if all(habitaciones_revisadas.values()) and habitacion_a.esta_limpia() and habitacion_b.esta_limpia():
            print("\nAmbas habitaciones están limpias. Proceso terminado.")
            break

simular_proceso_limpieza()
