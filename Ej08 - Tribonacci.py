def tribonacci(signature, n):
    suma = 0
    for x in signature:
        suma = suma + x
    signature.append(suma)
    
    m = 3
    print(n)
    while m <= n:
        valor = 0
        for x in signature[-3:]:
            valor = valor + x
        signature.append(valor)
        m += 1
    print(m)
    
    print(signature[:n+1])

tribonacci([0.5, 0.5, 0.5], 30)

"""
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
  """
"""
def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]
    """