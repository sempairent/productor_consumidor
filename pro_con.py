import threading
import time

buffer = []  # Búfer compartido entre el productor y el consumidor
semaphore = threading.Semaphore(1)  # Semáforo para controlar el acceso al búfer

numeros = [1, 2, 3, 4, 5]  # Lista de números a producir/consumir

class Productor(threading.Thread):
    def run(self):
        global buffer, semaphore
        for elemento in numeros:
            time.sleep(1)  # Simulamos un tiempo de producción
            semaphore.acquire()  # Adquirir el semáforo

            if len(buffer) >= 10:  # Verificar si el búfer está lleno
                print("Buffer lleno. El productor espera.")
                semaphore.release()  # Liberar el semáforo
                continue

            buffer.append(elemento)  # Agregar el elemento al búfer
            print(f"El productor produjo el elemento {elemento}.")
            semaphore.release()  # Liberar el semáforo

class Consumidor(threading.Thread):
    def run(self):
        global buffer, semaphore
        for elemento in numeros:
            time.sleep(1)  # Simulamos un tiempo de procesamiento
            semaphore.acquire()  # Adquirir el semáforo

            if len(buffer) == 0:  # Verificar si el búfer está vacío
                print("Buffer vacío. El consumidor espera.")
                semaphore.release()  # Liberar el semáforo
                continue

            elemento = buffer.pop(0)  # Consumir el primer elemento del búfer
            print(f"El consumidor consumió el elemento {elemento}.")
            semaphore.release()  # Liberar el semáforo

productor = Productor()  # Crear una instancia de Productor
consumidor = Consumidor()  # Crear una instancia de Consumidor

productor.start()  # Iniciar el hilo del productor
consumidor.start()  # Iniciar el hilo del consumidor






