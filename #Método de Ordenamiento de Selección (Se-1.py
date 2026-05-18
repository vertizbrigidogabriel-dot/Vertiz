#Método de Ordenamiento de Selección (SelectionSort)

from random import sample 

lista = list(range(100))

vectorselect = sample(lista,8)

def selectionsort(vectorselect):
    """Esta función ordenara el vector que le pases como argumento con el Método Selection Sort"""

    print ("El vector a ordenar es:",vectorselect)

    largo = 0

    for _ in vectorselect:
        largo += 1

        for i in range(largo):

            minimo = i
            for j in range(i+1, largo):
                if vectorselect[minimo] > vectorselect[j]:
                    minimo = j
            vectorselect[i], vectorselect[minimo] = vectorselect[minimo], vectorselect[i]

    print("El  vector ordenado es: ",vectorselect)

selectionsort(vectorselect)