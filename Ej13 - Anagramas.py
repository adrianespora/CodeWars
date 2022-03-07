# ¿Dónde están mis anagramas?
def anagrams(word, words):
    cantidad_word = {}
    for i in word:
        cantidad_word[i] = word.count(i)
    preseleccion = []
    diccionario = {}
    for palabra in words:
        if len(word) == len(palabra):
            preseleccion.append(palabra)
            diccionario[palabra] = ''
    
    for x in preseleccion:
        cantidad_palabra_lista = {}
        for letra in x:
            cantidad_palabra_lista[letra] = x.count(letra)
        diccionario[x] = cantidad_palabra_lista
    seleccion = []
    for x in diccionario:
        if cantidad_word != diccionario[x]:
            seleccion.append(x)
    for x in seleccion:
        del diccionario[x]
    Devolver = []
    for x in diccionario:
        Devolver.append(x)

    print(Devolver)

#anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dama']) # => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) #=> ['carer', 'racer']

#anagrams('laser', ['lazing', 'lazy',  'lacer']) #=> []

"""
def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]
"""