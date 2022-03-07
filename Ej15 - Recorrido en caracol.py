""" RECORRIDO EXTERNO SENTIDO AGUJAS RELOJ"""
def snail(snail_map):
    if snail_map == [[]]:
        return []
    elif snail_map == [[1]]:
        return [1]
    resultado = []
    indice_inicio = 0
    n = 0
    while n < len(snail_map):
        """
        1
        Tomo la lista 0, la asigno a resultado y borro esa linea
        """
        for x in snail_map[indice_inicio]:
            resultado.append(x)
        snail_map.pop(0)

        """ 
        2
        BUCLE PARA GUARDAR EN LA NUEVA LISTA LOS ULTIMOS VALORES DE CADA LINEA 
        Y ELIMIAR LUEGO ELIMINARLOS
        """
        lineas = 0
        indice_fin = -1
        while lineas < len(snail_map):
            resultado.append(snail_map[indice_inicio][indice_fin]) # agrego el ultimo valor de la linea 0 a RESULTADO
            valor = snail_map[indice_inicio] #asigno esa linea a una variable
            valor.pop(-1) # elimino el ultimo valor de la variable
            snail_map[indice_inicio] = valor # ubico la nueva linea en el lugar de la anterior
            indice_inicio += 1 # sumo 1 a indice_inicio
            lineas += 1 # sumo 1 a lineas
            #print('Ejecute while 1')
            """ 
            3
            CUANDO LLEGO A LA LINEA FINAL LA RECORRO INVERSAMENTE 
            Y LOS VOY AGREGANDO A LA NUEVA LISTA
            """
            if lineas == len(snail_map):
                snail_map[-1].reverse() # invierto el orden de la ultima linea
                #print('Ejecute if 1')
                for x in snail_map[-1]:
                    resultado.append(x)
                snail_map.pop() # borro la ultima linea
                lineas -= 1 
                indice_inicio -= indice_inicio # modifico el indice restandole la cantidad de lineas
                
        """
        4
        BUCLUE PARA AGREGAR A RESULTADOS LOS PRIMEROS VALORES DE CADA LINEA Y ELIMIARLOS DE LA OTRA
        """
        lineas -= 1
        while lineas > -1:
            resultado.append(snail_map[lineas][indice_inicio]) # agrego el primer valor de la nueva ultima linea
            valor = snail_map[lineas] #asigno esa linea a una variable
            valor.pop(0) # elimino el ultimo valor de la variable
            snail_map[lineas] = valor # ubico la nueva linea en el lugar de la anterior
            lineas -= 1
            
    else:
        print(resultado)
    
    
    
    """
    RESPUESTA
    """
    #return resultado
    #print(resultado)
    #print(snail_map)


array1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

#expected = [1,2,3,6,9,8,7,4,5]

array2 = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]
#expected = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


"""
[1, 2, 3, 4, 5, 
 6, 7, 8, 9, 10, 
 11, 12, 13, 14, 15,
 16, 17, 18, 19, 20
 21, 22, 23, 24, 25]
"""
array3 = [[1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10], 
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]

array4 = [[1,2,3,4,5,6],
        [7,8,9,10,11,12],         
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28,29,30],
        [31,32,33,34,35,36]]

snail(array4)

""" VERSION PRO

import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m
"""