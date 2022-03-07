"""
Formato de duración legible por humanos
61 segs = 1 min, 1 seg
"""
def format_duration(seconds):
    cadena = ''
    dias = []
    horas =[]
    minutos = []
    segundos = []
    for x in range(1,60,1):
        segundos.append(x)
    for x in range(60,3600,60):
        minutos.append(x)
    for x in range(3600,86400,3600):
        horas.append(x)
    for x in range(86400,31536000,86400):
        dias.append(x)
    if seconds == 0:
        cadena = cadena + 'now'
    elif seconds == 1:
        cadena = cadena + '1 second'
        """ AÑOS """
    else:
        if seconds >= 31536000 and seconds < (31536000*2): # si los segundos estan entre esos valores es 1 año
            cadena = cadena + '1 year'
            resto = seconds - 31536000*(int(seconds/31536000)) #guardo en resto los segundos que estan entre 1 año y 2
            if resto > 0:
                if resto in dias or resto in horas or resto in minutos or resto in segundos:
                        seconds = resto
                        cadena = cadena + ' and '
                else:
                    cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                    seconds = resto # almaceno en SECONDS el RESTO
        elif seconds >= 31536000*2: # si es mayor a 2 años
            cadena = cadena + str(int(seconds/31536000)) + ' years'
            resto = seconds - 31536000*(int(seconds/31536000))
            if resto in dias or resto in horas or resto in minutos or resto in segundos:
                seconds = resto
                cadena = cadena + ' and '
            else:
                cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                seconds = resto # almaceno en SECONDS el RESTO


        """ DIAS """
        if seconds >= 86400 and seconds < 172800: # si los segundos estan entre esos valores es 1 dia
            cadena = cadena + '1 day'
            resto = seconds - 86400*(int(seconds/86400)) # guardo en RESTO los segundos que estan entre 1 dia y 2
            if resto > 0:
                if resto in horas or resto in minutos or resto in segundos:
                    seconds = resto
                    cadena = cadena + ' and '
                else:
                    cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                    seconds = resto # almaceno en SECONDS el RESTO
        elif seconds >= 172800 and seconds < 31536000: # si es mayor a 2 dias
            cadena = cadena + str(int(seconds/86400)) + ' days'
            resto = seconds - 86400*(int(seconds/86400))
            if resto in horas or resto in minutos or resto in segundos:
                seconds = resto
                cadena = cadena + ' and '
            elif resto == 0:
                pass
            else:
                cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                seconds = resto # almaceno en SECONDS el RESTO
                
        """ HORAS """
        if seconds >= 3600 and seconds < 7200: # si los segundos estan entre esos valores es 1 dia
            cadena = cadena + '1 hour'
            resto = seconds - 3600*(int(seconds/3600)) # guardo en RESTO los segundos que estan entre 1 dia y 2
            if resto > 0:
                if resto in minutos or resto in segundos:
                    seconds = resto
                    cadena = cadena + ' and '
                else:
                    cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                    seconds = resto # almaceno en SECONDS el RESTO
        elif seconds >= 7200 and seconds < 86400: # si es mayor a 2 dias
            cadena = cadena + str(int(seconds/3600)) + ' hours'
            resto = seconds - 3600*(int(seconds/3600))
            if resto in minutos or resto in segundos:
                seconds = resto
                cadena = cadena + ' and '
            elif resto == 0:
                pass
            else:
                cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                seconds = resto # almaceno en SECONDS el RESTO

        """ MINUTOS """
        if seconds >= 60 and seconds < 120: # si los segundos estan entre esos valores es 1 dia
            cadena = cadena + '1 minute'
            resto = seconds - 60*(int(seconds/60)) # guardo en RESTO los segundos que estan entre 1 dia y 2
            if resto > 0:
                if resto in segundos:
                    seconds = resto
                    cadena = cadena + ' and '
                else:
                    cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                    seconds = resto # almaceno en SECONDS el RESTO
        elif seconds >= 120 and seconds < 3600: # si es mayor a 2 dias
            cadena = cadena + str(int(seconds/60)) + ' minutes'
            resto = seconds - 60*(int(seconds/60))
            if resto in segundos:
                seconds = resto
                cadena = cadena + ' and '
            elif resto == 0:
                pass
            else:
                cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                seconds = resto # almaceno en SECONDS el RESTO

                
        """ SEGUNDOS """
        if seconds == 1:
            cadena = cadena + '1 second'
        elif seconds >1 and seconds < 60:
            cadena = cadena + str(int(seconds)) + ' seconds'
        
    
    print(cadena)

año = 31536000
dia = 86400
hora = 3600
minuto = 60
UnMin_DosSeg = 62
DosMin_Dos_Seg = 122
año_dia = 31536000+86400
año_2dias = 31536000+(86400*2)
año_dia_hora = 31536000+86400+3600
año_dia_hora_min = 31536000+86400+3600+60
año_dia_hora_min_seg = 31536000+86400+3600+60+40
numero = 92536000+126400+8900+60+5
años_dias_horas_minutos_segundos = año_dia_hora_min_seg*2
DosAños_UnDia = (31536000*2)+86400
DosAños_DosDias = (31536000*2)+(86400*2)
DosAños_DosDias_UnaHora = (31536000*2)+(86400*2)+3600
DosAños_DosDias_DosHoras_UnMinuto = (31536000*2)+(86400*2)+(3600*2)+60

format_duration(año_2dias)
format_duration(DosAños_DosDias)

format_duration(año)
format_duration(dia)
format_duration(hora)
format_duration(minuto)
format_duration(UnMin_DosSeg)
format_duration(DosMin_Dos_Seg)
format_duration(año_dia)
format_duration(año_2dias)
format_duration(año_dia_hora)
format_duration(año_dia_hora_min)
format_duration(año_dia_hora_min_seg)
format_duration(años_dias_horas_minutos_segundos)
format_duration(DosAños_UnDia)
format_duration(DosAños_DosDias_UnaHora)
format_duration(DosAños_DosDias_DosHoras_UnMinuto)



"""
test.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
"""