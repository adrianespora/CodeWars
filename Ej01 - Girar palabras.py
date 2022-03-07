"""Escriba una función que tome una cadena de una o más palabras y def spin_words(sentence):
devuelva la misma cadena, pero con las palabras de cinco o más letras
 invertidas (al igual que el nombre de este Kata). Las cadenas 
 pasadas consistirán solo en letras y espacios. Los espacios se 
 incluirán solo cuando haya más de una palabra presente."""


"""def spin_words(sentence):
    cadena = sentence.split(' ')
    cadena_cambiada = ''
    for i in cadena:
        if len(i) >= 5:
            j = i[::-1]
            cadena_cambiada = cadena_cambiada + ' ' +j
        else:
            cadena_cambiada = cadena_cambiada +' '+ i
        console.log(cadena_cambiada)

spin_words('Hola mundo como estan')"""

def spin_words(sentence):
    cadena = sentence.split(' ')
    cambio = ''
    if len(cadena) == 1:
        if len(sentence) >= 5:
            for i in cadena:
                cambio = str((i[::-1]))
                palabra = str(cambio)
                print(palabra)
        else:
            print(sentence)
    else:
        cadena = sentence.split(' ')
        cadena_cambiada = ''
        for i in cadena:
            if len(i) >= 5:
                j = i[::-1]
                cadena_cambiada = cadena_cambiada + ' ' +j
            else:
                cadena_cambiada = cadena_cambiada +' '+ i
        return (print(cadena_cambiada))
    return None

spin_words('pepa comera')