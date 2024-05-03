# Estás trabajando en un programa que procesa listas, pero te enfrentas al desafío de
# eliminar los elementos duplicados de una lista, manteniendo el orden original.

# Especificaciones de la Función:
# Nombre de la función:
# ● El nombre de la función debe ser: eliminar_duplicados
# Parámetros:
# ● lista (list): Una lista que puede contener elementos duplicados.

# Retorno:
# ● list: Una nueva lista que contiene los elementos de la lista original sin
# duplicados, conservando el orden original.
# Ejemplo
# ● La función eliminar_duplicados toma la lista [1, 2, 3, 4, 4, 5, 6, 6, 7] como
# entrada y devuelve una nueva lista [1, 2, 3, 4, 5, 6, 7] sin elementos duplicados,
# manteniendo el orden original.

l=[]

def eliminar_duplicados(list):
    for i in list:
        print(list[i])
        # if i!=list[i]:
        #     print("lista:", list[i])
        #     print("i: ", i)


lista=[1, 2, 3, 4, 4, 5, 6, 6, 7]
eliminar_duplicados(lista)