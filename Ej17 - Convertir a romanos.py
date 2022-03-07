class RomanNumerals:

    def to_roman(val):
        cadena = []
        numero_en_cadena = str(val)
        unidades = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X'}
        decenas = {0:'', 1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX',8:'LXXX',9:'XC' }
        centenas = {0:'', 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DX', 7:'DXX',8:'DXXX',9:'CM' }
        miles = {1:'M', 2:'MM', 3:'MMM'}

        if val > 0 and val <= 10:
            cadena.append(unidades[val])

        if len(numero_en_cadena) == 2 and val > 10:
            cadena.append(unidades[int(numero_en_cadena[-1])])
            cadena.append(decenas[int(numero_en_cadena[0])])

        if len(numero_en_cadena) == 3:
            cadena.append(unidades[int(numero_en_cadena[-1])])
            cadena.append(decenas[int(numero_en_cadena[1])])
            cadena.append(centenas[int(numero_en_cadena[0])])

        if len(numero_en_cadena) == 4:
            cadena.append(unidades[int(numero_en_cadena[-1])])
            cadena.append(decenas[int(numero_en_cadena[2])])
            cadena.append(centenas[int(numero_en_cadena[1])])
            cadena.append(miles[int(numero_en_cadena[0])])

        cadena.reverse() # invierto el orden de la lista
        resultado = ''.join(cadena) # convierto la lista en cadena

        print(resultado)
               
    def from_roman(roman_num):
        cuenta_miles = 0  
        cuenta_cientos = 0  
        cuenta_decenas = 0 
        cuenta_unidades = 0
        n = 0
        if roman_num[n] == 'M': # MILES
            m = 0
            for x in roman_num[n:]:
                if x == 'M':
                    cuenta_miles += 1000
                    m += 1
                else:
                    break
            n += m
        
        if n < len(roman_num):
            if roman_num[n] == 'D': # CIENTOS
                cuenta_cientos += 500
                m = 1
                for x in roman_num[n:]:
                    if x == 'C':
                        cuenta_cientos += 100
                        m += 1
                    else:
                        break
                n += m
        if n < len(roman_num):
            if roman_num[n] == 'C':
                for x in roman_num[n:]:
                    m = 0
                    if x == 'C':
                        cuenta_cientos += 100
                        m += 1
                    elif x == 'M':
                        cuenta_cientos += 800
                        m += 1
                    elif x == 'D':
                        cuenta_cientos += 300
                        m += 1
                    else:
                        break # Hasta aca OK
                    n += m
        
        if n < len(roman_num):
            if roman_num[n] == 'L': # DECENAS
                cuenta_decenas += 50
                m = 1
                for x in roman_num[n]:
                    if x == 'X':
                        cuenta_decenas += 10
                        m += 1
                    else:
                        break
                n += m
        if n < len(roman_num):
            if roman_num[n] == 'X':
                for x in roman_num[n:]:
                    m = 0
                    if x == 'C':
                        cuenta_decenas += 80
                        m += 1
                    elif x == 'X':
                        cuenta_decenas += 10
                        m += 1
                    elif x == 'L':
                        cuenta_decenas += 30
                        m += 1
                    elif x == 'V':
                        cuenta_unidades +=5
                        m += 1
                    else:
                        break
                n += m
        
        if n < len(roman_num):
            if roman_num[n] == 'V': # UNIDADES
                for x in roman_num[n]:
                    m= 0
                    if x == 'V':
                        cuenta_unidades +=5
                        m += 1
                    elif x == 'I':
                        cuenta_unidades += 1
                        m += 1
                    else:
                        break
                n += m
        if n < len(roman_num):
            if roman_num[n] == 'I':
                for x in roman_num[n:]:
                    m= 0
                    if x == 'X':
                        cuenta_unidades += 8
                        m += 1
                    elif x == 'V':
                        cuenta_unidades += 3
                        m += 1
                    elif x == 'I':
                        cuenta_unidades += 1
                        print('asd')
                        m += 1
                    else:
                        break
            

        total = cuenta_miles + cuenta_cientos + cuenta_decenas + cuenta_unidades
        
        """return total"""
        print(total)
        """print(cuenta_miles)
        print(cuenta_cientos)
        print(cuenta_decenas)
        print(cuenta_unidades)"""
        



RomanNumerals.to_roman(1237)
RomanNumerals.from_roman('MCCXXXVII')
RomanNumerals.to_roman(8)
RomanNumerals.from_roman('VIII')
"""RomanNumerals.to_roman(990)
RomanNumerals.from_roman('MCXI')
RomanNumerals.to_roman(40)
RomanNumerals.from_roman('MCMXL')
RomanNumerals.to_roman(1930)
RomanNumerals.from_roman('MCMXXX')
RomanNumerals.to_roman(1950)
RomanNumerals.from_roman('MCML')
RomanNumerals.to_roman(1970)
RomanNumerals.from_roman('MCMLXX')
RomanNumerals.to_roman(1666)
RomanNumerals.from_roman('MDCLXVI')"""