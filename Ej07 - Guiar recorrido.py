from logging.config import valid_ident


def is_valid_walk(walk):
    if len(walk) != 10:
        return False
        pass
    else:
        cuentaN, cuentaS, cuentaE, cuentaW = 0,0,0,0
        for x in walk:
            if x == 'n':
                cuentaN += 1
            elif x == 's':
                cuentaS += 1
            elif x == 'e':
                cuentaE += 1
            elif x == 'w':
                cuentaW += 1
        if cuentaN-cuentaS==0 and cuentaE-cuentaW == 0:
            return True
        else:
            return False


is_valid_walk(['n', 'n', 'w', 'e', 'e', 'w', 's', 'e', 'w', 'w'])

"""
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
    """