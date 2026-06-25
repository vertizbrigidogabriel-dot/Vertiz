# 2) Figuras geométricas (área)

from abc import ABC, abstractmethod  # Importa las herramientas para crear clases abstractas y métodos obligatorios.
import math  # Importa la librería matemática de Python (se usará para obtener el valor de Pi).

class Figura(ABC):  # Define la clase abstracta base 'Figura' (plantilla principal que no se instancia).
    
    @abstractmethod  # Decorador que hace que el siguiente método sea obligatorio para las subclases.
    def area(self) -> float:  # Declara el método abstracto 'area', indicando que debe devolver un número decimal (float).
        pass  # Deja el método vacío; cada figura específica calculará su área a su manera.
        
    @abstractmethod  # Decorador que hace que el método de abajo sea obligatorio para las subclases.
    def dibujar(self):  # Declara el método abstracto 'dibujar'.
        pass  # Deja el método vacío para que las clases hijas lo definan.

class Circulo(Figura):  # Define la clase 'Circulo', la cual hereda de la clase base 'Figura'.
    
    def __init__(self, radio: float):  # Constructor del círculo; recibe un parámetro numérico llamado 'radio'.
        self.radio = radio  # Guarda el valor del radio dentro del objeto creado.
        
    def area(self) -> float:  # Define específicamente cómo se calcula el área para un círculo.
        return math.pi * self.radio ** 2  # Retorna el resultado de la fórmula del área del círculo: pi * r^2.
        
    def dibujar(self):  # Define específicamente cómo se "dibuja" (imprime) un círculo.
        print(f"Dibujando un círculo de radio {self.radio}")  # Imprime en pantalla la acción con el tamaño del radio.

class Rectangulo(Figura):  # Define la clase 'Rectangulo', que hereda de la clase base 'Figura'.
    
    def __init__(self, ancho: float, alto: float):  # Constructor del rectángulo; recibe valores de ancho y alto.
        self.ancho = ancho  # Guarda el valor del ancho dentro del objeto.
        self.alto = alto  # Guarda el valor del alto dentro del objeto.
        
    def area(self) -> float:  # Define cómo se calcula el área para un rectángulo.
        return self.ancho * self.alto  # Retorna el resultado de multiplicar la base (ancho) por la altura (alto).
        
    def dibujar(self):  # Define cómo se "dibuja" un rectángulo.
        print(f"Dibujando un rectángulo {self.ancho} x {self.alto}")  # Imprime en pantalla las medidas del rectángulo.

class Triangulo(Figura):  # Define la clase 'Triangulo', que hereda de la clase base 'Figura'.
    
    def __init__(self, base: float, altura: float):  # Constructor del triángulo; recibe valores de base y altura.
        self.base = base  # Guarda el valor de la base en el objeto.
        self.altura = altura  # Guarda el valor de la altura en el objeto.
        
    def area(self) -> float:  # Define cómo se calcula el área para un triángulo.
        return (self.base * self.altura) / 2  # Retorna el resultado de la fórmula: (base * altura) / 2.
        
    def dibujar(self):  # Define cómo se "dibuja" un triángulo.
        print(f"Dibujando un triángulo de base {self.base} y altura {self.altura}")  # Imprime en pantalla las medidas del triángulo.

def procesar_figura(figura: Figura):  # Crea una función externa que puede recibir cualquier objeto derivado de 'Figura'.
    # Polimorfismo: misma interfaz, distintas implementaciones
    figura.dibujar()  # Ejecuta el método 'dibujar' correspondiente a la figura que se haya pasado.
    print(f"Área = {figura.area():.2f}")  # Ejecuta el método 'area' e imprime el resultado limitándolo a 2 decimales (:.2f).

if __name__ == "__main__":  # Condición que verifica si el archivo se está ejecutando directamente.
    
    figuras = [  # Crea una lista llamada 'figuras' para almacenar múltiples objetos geométricos.
        Circulo(3),  # Crea un objeto 'Circulo' con radio 3 y lo agrega a la lista.
        Rectangulo(4, 5),  # Crea un objeto 'Rectangulo' con ancho 4 y alto 5, y lo agrega a la lista.
        Triangulo(6, 2)  # Crea un objeto 'Triangulo' con base 6 y altura 2, y lo agrega a la lista.
    ]  # Cierra la lista de figuras.
    
    for f in figuras:  # Inicia un ciclo para recorrer cada figura guardada en la lista.
        procesar_figura(f)  # Llama a la función enviándole la figura actual para dibujarla y calcular su área.
        print("-" * 20)  # Imprime una línea separadora hecha con 20 guiones para que la salida en consola sea más legible.