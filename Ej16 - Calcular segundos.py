def format_duration(seconds):
    segundos_resultado = seconds
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
        cadena = cadena + 'Ahora'
    elif seconds == 1:
        cadena = cadena + '1 segundo'
        """ AÑOS """
    else:
        if seconds >= 31536000 and seconds < (31536000*2): # si los segundos estan entre esos valores es 1 año
            cadena = cadena + '1 año'
            resto = seconds - 31536000*(int(seconds/31536000)) #guardo en resto los segundos que estan entre 1 año y 2
            if resto > 0:
                if resto in dias or resto in horas or resto in minutos or resto in segundos:
                        seconds = resto
                        cadena = cadena + ' y '
                else:
                    cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                    seconds = resto # almaceno en SECONDS el RESTO
        elif seconds >= 31536000*2: # si es mayor a 2 años
            cadena = cadena + str(int(seconds/31536000)) + ' años'
            resto = seconds - 31536000*(int(seconds/31536000))
            if resto in dias or resto in horas or resto in minutos or resto in segundos:
                seconds = resto
                cadena = cadena + ' y '
            else:
                cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                seconds = resto # almaceno en SECONDS el RESTO


        """ DIAS """
        if seconds >= 86400 and seconds < 172800: # si los segundos estan entre esos valores es 1 dia
            cadena = cadena + '1 dia'
            resto = seconds - 86400*(int(seconds/86400)) # guardo en RESTO los segundos que estan entre 1 dia y 2
            if resto > 0:
                if resto in horas or resto in minutos or resto in segundos:
                    seconds = resto
                    cadena = cadena + ' y '
                else:
                    cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                    seconds = resto # almaceno en SECONDS el RESTO
        elif seconds >= 172800 and seconds < 31536000: # si es mayor a 2 dias
            cadena = cadena + str(int(seconds/86400)) + ' dias'
            resto = seconds - 86400*(int(seconds/86400))
            if resto in horas or resto in minutos or resto in segundos:
                seconds = resto
                cadena = cadena + ' y '
            elif resto == 0:
                pass
            else:
                cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                seconds = resto # almaceno en SECONDS el RESTO
                
        """ HORAS """
        if seconds >= 3600 and seconds < 7200: # si los segundos estan entre esos valores es 1 dia
            cadena = cadena + '1 hora'
            resto = seconds - 3600*(int(seconds/3600)) # guardo en RESTO los segundos que estan entre 1 dia y 2
            if resto > 0:
                if resto in minutos or resto in segundos:
                    seconds = resto
                    cadena = cadena + ' y '
                else:
                    cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                    seconds = resto # almaceno en SECONDS el RESTO
        elif seconds >= 7200 and seconds < 86400: # si es mayor a 2 dias
            cadena = cadena + str(int(seconds/3600)) + ' horas'
            resto = seconds - 3600*(int(seconds/3600))
            if resto in minutos or resto in segundos:
                seconds = resto
                cadena = cadena + ' y '
            elif resto == 0:
                pass
            else:
                cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                seconds = resto # almaceno en SECONDS el RESTO

        """ MINUTOS """
        if seconds >= 60 and seconds < 120: # si los segundos estan entre esos valores es 1 dia
            cadena = cadena + '1 minuto'
            resto = seconds - 60*(int(seconds/60)) # guardo en RESTO los segundos que estan entre 1 dia y 2
            if resto > 0:
                if resto in segundos:
                    seconds = resto
                    cadena = cadena + ' y '
                else:
                    cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                    seconds = resto # almaceno en SECONDS el RESTO
        elif seconds >= 120 and seconds < 3600: # si es mayor a 2 dias
            cadena = cadena + str(int(seconds/60)) + ' minutos'
            resto = seconds - 60*(int(seconds/60))
            if resto in segundos:
                seconds = resto
                cadena = cadena + ' y '
            elif resto == 0:
                pass
            else:
                cadena = cadena + ', ' # como RESTO es mayor agrego ', '
                seconds = resto # almaceno en SECONDS el RESTO

                
        """ SEGUNDOS """
        if seconds == 1:
            cadena = cadena + '1 segundo'
        elif seconds >1 and seconds < 60:
            cadena = cadena + str(int(seconds)) + ' segundos'
        
    
    print(f'\nLos {segundos_resultado} segundos representan: {cadena}\n')



def menu():
    while True: 
        print("""CONVERSOR DE SEGUNDOS\n\n
        1 - Ingresar Segundos\n
        2 - Salir\n
        """)
        try:
            opcion = int(input("Ingrese una opcion: "))
        except:
            print('Hay un error, debe ingresar 1 o 2!\n')
            menu()
        try:    
            if opcion == 1:
                seconds = int(input('Ingrese los segundos: '))
                format_duration(seconds) #para referir la variable 'seconds' a otra funcion
            elif opcion == 2:
                break
        except:
            print('Hay un error, debe ingresar un Numero entero!\n')
            seconds = int(input('Ingrese los segundos: '))
            format_duration(seconds) #para referir la variable 'seconds' a otra funcion
    
    return
    
menu()
