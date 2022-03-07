# Is a number prime?
def is_prime(num):
    if num <= 1:
        print("Falso")
        return False
    else:
        i = 2
        while num%i !=0:
            i = i+1
        if i == num:
            print("El numero ingresado un numero primo")
        else:
            print("No es primo")

is_prime(4)
def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

is_prime(5)

