# FILA DE CLIENTES
def queue_time(customers, n):
    if n == 1:
        print(sum(customers))
    elif n > len(customers):
        print(max(customers))
    elif customers == '':
        print('0')
    else:
        lista = []
        for x in customers[:n]:
            lista.append(x)
        lista.sort()
        cuenta=0
        m = 0
        for x in customers[n:]:
            lista.append(lista[m]+x)
            lista.sort()
            m += 1
            cuenta += 1
        print(max(lista))
       
queue_time([40, 42, 35, 13, 34, 39, 47, 46, 12, 32, 49, 12, 12, 38, 15, 17, 29, 3], 4)

"""
def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
    """