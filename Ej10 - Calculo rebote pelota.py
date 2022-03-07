def bouncing_ball(h, bounce, window):
    cuenta = 0
    altura = float(h)
    rebote = float(bounce)
    ventana = float(window)
    if altura > 0 :
        if 1 > rebote and rebote > 0:
            while ventana < altura:
                altura = altura*rebote
                print(altura)
                cuenta += 1
          
    else:
        print('error')
        return -1
    cuenta = cuenta + cuenta - 1
    print(cuenta) 

bouncing_ball(30,0.75,1.5)