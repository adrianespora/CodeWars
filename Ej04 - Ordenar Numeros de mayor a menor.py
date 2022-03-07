from dataclasses import replace

def high_and_low(numbers): 
    numbers = numbers.split(' ') # Separo los valores por espacio
    ListaNumeros = []
    for x in numbers:
        ListaNumeros.append(int(x))  # Agrego los valores de x a la lista
    ListaNumeros.sort() # Ordeno la lista de menos a mayor
    
    numeros = str(ListaNumeros[-1]) + ' ' + str(ListaNumeros[0])
    print(numeros)
    return numeros


""" REALIZADO POR ALGUNO MAS PRO
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
    """