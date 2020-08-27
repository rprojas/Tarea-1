def numero_perfecto():
    num = int(input("Escribir un numero::> "))
    suma = 0

    for i in range(1, num):
        if num % i == 0:
            suma += i

    if suma == num:
        print("el numero es prefecto")
    else:
        print("el numero no es prefecto")

    return 0


def main():
    numero_perfecto()

if __name__ == "__main__":
    main()