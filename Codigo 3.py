# 3) Vehículos y movimientos:

from abc import ABC, abstractmethod  # Importa las herramientas necesarias para crear clases y métodos abstractos.

class Vehiculo(ABC):  # Define la clase base abstracta 'Vehiculo'. Sirve como plantilla genérica.
    
    def __init__(self, marca: str):  # Constructor de la clase; recibe un texto (str) que representa la marca.
        self.marca = marca  # Guarda la marca recibida dentro del objeto creado.
        
    @abstractmethod  # Decorador que obliga a las clases hijas (Auto, Moto, etc.) a crear este método.
    def arrancar(self):  # Declara el método abstracto 'arrancar'.
        pass  # Lo deja vacío porque un vehículo genérico no sabe cómo arrancar; las clases hijas lo definirán.
        
    @abstractmethod  # Decorador que obliga a las clases hijas a crear este método.
    def moverse(self):  # Declara el método abstracto 'moverse'.
        pass  # Lo deja vacío por la misma razón anterior.

class Auto(Vehiculo):  # Define la clase 'Auto', la cual hereda todas las propiedades de 'Vehiculo'.
    
    def arrancar(self):  # Define específicamente cómo arranca un Auto.
        print(f"Auto {self.marca} arrancando con llave.")  # Imprime el mensaje de arranque incluyendo su marca.
        
    def moverse(self):  # Define específicamente cómo se mueve un Auto.
        print(f"Auto {self.marca} circulando por la carretera.")  # Imprime el mensaje de movimiento.

class Moto(Vehiculo):  # Define la clase 'Moto', la cual también hereda de 'Vehiculo'.
    
    def arrancar(self):  # Define específicamente cómo arranca una Moto.
        print(f"Moto {self.marca} arrancando con botón eléctrico.")  # Imprime el mensaje de arranque de la moto.
        
    def moverse(self):  # Define específicamente cómo se mueve una Moto.
        print(f"Moto {self.marca} avanzando entre el tráfico.")  # Imprime el mensaje de movimiento.

class Camion(Vehiculo):  # Define la clase 'Camion', heredando de 'Vehiculo'.
    
    def arrancar(self):  # Define específicamente cómo arranca un Camión.
        print(f"Camión {self.marca} encendiendo motor diésel.")  # Imprime el mensaje de arranque pesado.
        
    def moverse(self):  # Define específicamente cómo se mueve un Camión.
        print(f"Camión {self.marca} transportando carga pesada.")  # Imprime el mensaje de movimiento con carga.

def iniciar_viaje(vehiculo: Vehiculo):  # Crea una función externa que puede recibir cualquier tipo de 'Vehiculo'.
    # Polimorfismo: misma llamada, diferente comportamiento
    vehiculo.arrancar()  # Ejecuta el método 'arrancar' de la clase específica que haya recibido.
    vehiculo.moverse()  # Ejecuta el método 'moverse' de la clase específica que haya recibido.

if __name__ == "__main__":  # Asegura que el código de abajo solo corra si se ejecuta este archivo directamente.
    
    flota = [  # Crea una lista llamada 'flota' para almacenar varios objetos de vehículos.
        Auto("Toyota"),  # Crea un objeto 'Auto' de marca Toyota y lo añade a la lista.
        Moto("Yamaha"),  # Crea un objeto 'Moto' de marca Yamaha y lo añade a la lista.
        Camion("Volvo")  # Crea un objeto 'Camion' de marca Volvo y lo añade a la lista.
    ]  # Cierra la definición de la lista.
    
    for v in flota:  # Inicia un bucle que revisará cada vehículo guardado en la lista 'flota'.
        iniciar_viaje(v)  # Pasa el vehículo actual a la función para que imprima cómo arranca y se mueve.
        print("-" * 20)  # Imprime una línea divisoria de 20 guiones para separar la información en la pantalla.