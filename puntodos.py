def numeroprimo():
    num = int(input("Escribir un numero::> "))
    contador = 0
    for i in range(1, num+1):
        if num % i == 0:
            contador += 1
    if contador == 2:
        print("Es primo")
        return True
    else:
        print("No es primo")
        return False

def main():
    numeroprimo()

if __name__ == "__main__":
    main()