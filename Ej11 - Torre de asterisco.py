"construir torre"
def tower_builder(n_floors):
    if n_floors > 0:
        lista = []
        for i in range(n_floors):
            lista.append(' '* (n_floors-i-1)+'*'*(2*i+1)+' '* (n_floors-i-1))
        print(lista)
    
tower_builder(6)

"""
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
    """