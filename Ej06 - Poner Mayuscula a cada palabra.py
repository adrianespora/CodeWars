def to_jaden_case(string):
    string = string.split(' ')
    cadena = ''
    for x in string:
        cadena = cadena + ' ' +(x.capitalize())
        resultado = cadena.lstrip(' ')
    
    print(resultado)
    
to_jaden_case("How can mirrors be real if our eyes aren't real")

"""
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
    
"""