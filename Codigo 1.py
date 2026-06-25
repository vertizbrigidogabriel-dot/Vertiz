# 1) Animales y sonido: (Título o descripción del bloque de código)

from abc import ABC, abstractmethod  # Importa las herramientas necesarias para crear clases abstractas.

class Animal(ABC):  # Define la clase base 'Animal' que hereda de 'ABC' (haciéndola abstracta, no se puede instanciar directamente).
    
    def __init__(self, nombre):  # Define el constructor de la clase. Se ejecuta automáticamente al crear un nuevo animal.
        self.nombre = nombre  # Guarda el valor del parámetro 'nombre' dentro del atributo del objeto (self).        
    @abstractmethod  # Decorador que obliga a cualquier clase "hija" a crear su propia versión del método de abajo.
    def hacer_sonido(self):  # Define el método 'hacer_sonido'.
        pass  # Indica que este método está vacío en la clase padre. La implementación se delega a las clases hijas.
class Perro(Animal):  # Define la clase 'Perro', que hereda todos los atributos y métodos de la clase 'Animal'.
    def hacer_sonido(self):  # Sobrescribe el método 'hacer_sonido' específicamente para los perros.
        return f"{self.nombre} dice: Guau!"  # Retorna un texto formateado (f-string) que incluye el nombre del perro y su ladrido.
class Gato(Animal):  # Define la clase 'Gato', que hereda de la clase 'Animal'.
    def hacer_sonido(self):  # Sobrescribe el método 'hacer_sonido' específicamente para los gatos.
        return f"{self.nombre} dice: Miau!"  # Retorna un texto formateado con el nombre del gato y su maullido.
class Pajaro(Animal):  # Define la clase 'Pajaro', que hereda de la clase 'Animal'.
    def hacer_sonido(self):  # Sobrescribe el método 'hacer_sonido' específicamente para los pájaros.
        return f"{self.nombre} dice: Pío pío!"  # Retorna un texto formateado con el nombre del pájaro y su canto.
def reproducir_sonido(animal: Animal):  # Define una función independiente que acepta cualquier objeto que sea de tipo 'Animal'.
    # Polimorfismo: el mismo método se comporta distinto según la subclase (Comentario original).
    print(animal.hacer_sonido())  # Llama al método 'hacer_sonido' del animal que recibe y lo imprime en la consola.
if __name__ == "__main__":  # Asegura que el siguiente código solo se ejecute si este archivo es el programa principal.
    
    animales = [  # Crea una lista de objetos que guardaremos en la variable 'animales'.
        Perro("Firulais"),  # Crea un objeto 'Perro' llamado "Firulais" y lo pone en la lista.
        Gato("Misu"),  # Crea un objeto 'Gato' llamado "Misu" y lo pone en la lista.
        Pajaro("Piolín")  # Crea un objeto 'Pajaro' llamado "Piolín" y lo pone en la lista.
    ]  # Cierra la lista de animales.
    
    for a in animales:  # Inicia un bucle que recorrerá uno por uno los elementos de la lista 'animales'.
        reproducir_sonido(a)  # Toma el animal actual del bucle (a) y se lo pasa a la función para que imprima su sonido.