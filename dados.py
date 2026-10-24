'''
 -> str: Para funciones que devuelven texto ("Hola", "Código", etc.).
 -> int: Para funciones que devuelven números enteros (5, -10, 100).
 -> float: Para funciones que devuelven números con decimales (3.14, 19.50).
 -> bool: Para funciones que devuelven un valor booleano (True o False).
 -> None: Para funciones que no devuelven nada.
'''

import random

class Dados:
    def __init__(self, num_caras: int, num_dados: int):
        """
        Inicializa la clase con el número de caras y dados.
        """
        if num_caras <= 0 or num_dados <= 0:
            raise ValueError("El número de caras y de dados debe ser mayor a 0.")

        self.num_caras = num_caras
        self.num_dados = num_dados

    def tirar_dados(self) -> list[int]:
        """
        Simula la tirada de los dados.
        Devuelve una lista con los resultados de cada dado.
        """
        resultados = [random.randint(1, self.num_caras) for _ in range(self.num_dados)]
        return resultados

    def obtener_total(self) -> int:
        """
        Simula la tirada y devuelve la suma total de los resultados.
        """
        return sum(self.tirar_dados())
        
