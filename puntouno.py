def numeropar_impar():
    num = int(input("Escribir un numero::> "))
    if num%2==0:
            print("el numero es par")
    else:
         print("el numero es impar")

    return num

def main(): 
    numeropar_impar()

if __name__ == "__main__":
    main()
