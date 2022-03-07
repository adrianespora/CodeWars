# return masked string
from dataclasses import replace


def maskify(cc):
    if len(cc) <= 4:
        return cc
        pass
    else:
        encriptado = ''
        for x in cc[0:-4]:
            encriptado = encriptado+str('#')
        for x in cc[-4:]:
            encriptado = encriptado+x
        
        print(encriptado)
    

maskify('c0mandant3')


"""# return masked string
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
    """












