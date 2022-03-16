import os


def cambio(monto):
    numero = int(input("Ingrese su número celular: \n"))
    monto = str(monto)
    print("Ha escogido una recarga de $" + monto)
    pagado = int(input("Ingrese el monto con el que desea pagar: \n$"))
    monto = int(monto)
    if pagado < monto:
        print("La operación no se ha podido realizar.")
    else:
        cambio = pagado - monto
        cambio = str(cambio)
        numero = str(numero)
        monto = str(monto)
        print("La operación se ha realizado con éxito.") 
        print("Se ha recargado $" + monto + " al número " + numero)
        print("Su cambio es $" + cambio)


def otra_operacion():
    otra_opera = input("""\n¿Desea realizar otra operación?
    Escriba sí o no: 
    """)
    if otra_opera == "si" or otra_opera == "si " or otra_opera == "sí" or otra_opera == "sí ":
        run()
    else:
        print("Vuelva pronto.")


def consulta_saldo(saldo, nuevo_saldo):
    os.system("cls")
    nip = input('Ingrese su NIP: \n')
    if nip == 1:
        saldo -= nuevo_saldo
        saldo = str(saldo)
        print("Su saldo es $" + saldo)


def tiempo_aire():
    os.system("cls")
    print("Escoja la compañía: ")
    print("1. Telcel ")
    print("2. Movistar ")
    print("3. AT&T ")
    print("4. Unefon ")
    eleccion = int(input("Ingrese el número correspondiente (1-4) \n"))
    if eleccion == 1 or eleccion == 2 or eleccion == 3 or eleccion == 4:
        print("¿Cuánto tiempo aire desea recargar? ")
        print("1. $20")
        print("2. $50")
        print("3. $100")
        print("4. $150")
        print("5. $200")
        print("6. $500")
        eleccion2 = int(input("Ingrese el respecitvo número: \n"))
        if eleccion2 == 1:
            cambio(20)
        elif eleccion2 == 2:
            cambio(50)
        elif eleccion2 == 3:
            cambio(100)
        elif eleccion2 == 4:
            cambio(150)
        elif eleccion2 == 5:
            cambio(200)
        elif eleccion2 == 6:
            cambio(500)
        else:
            print("Por favor, ingrese una opción válida.")
    else:
        print("Por favor, ingrese una opción válida.")


def luz():
    os.system("cls")
    print("Por el momento solo está disponible el pago de luz. \n")
    servicio = input("Ingrese su número de servico/referencia: \n")
    a_pagar = int(input("Ingrese el monto a pagar: \n$"))
    pagado = int(input("Ingrese el dinero con el que va a pagar: \n$"))
    cambio = pagado - a_pagar
    if cambio < 0:
        print("Su pago no se ha podido realizar. Intente más tarde.")
    else:
        cambio = str(cambio)
        print("\nEl servicio " + servicio + " se ha pagado con éxito.")
        print("Su cambio es $" + cambio)
        cambio = int(cambio)
        #Billete 200
        billete200 = cambio // 200
        sobrante200 = cambio % 200
        print("")
        if billete200 > 0:
            print(f"{billete200} billete(s) de $200")
        #Billete 100
        billete100 = sobrante200 // 100
        sobrante100 = sobrante200 % 100
        if billete100 > 0:
            print(f"{billete100} billete(s) de $100")
        #Billete 50
        billete50 = sobrante100 // 50
        sobrante50 = sobrante100 % 50
        if billete50 > 0:
            print(f"{billete50} billete(s) de $50")
        #Billete 20
        billete20 = sobrante50 // 20
        sobrante20 = sobrante50 % 20
        if billete20 > 0:
            print(f"{billete20} billete(s) de $20")
        #Moneda 10
        moneda10 = sobrante20 // 10
        sobrante10 = sobrante20 % 10
        if moneda10 > 0:
            print(f"{moneda10} moneda(s) de $10")
        #Moneda 5
        moneda5 = sobrante10 // 5
        sobrante5 = sobrante10 % 5
        if moneda5 > 0:
            print(f"{moneda5} moneda(s) de $5")
        #Moneda 2
        moneda2 = sobrante5 // 2
        sobrante2 = sobrante5 % 2
        if moneda2 > 0:
            print(f"{moneda2} moneda(s) de $2")
        #Moneda peso
        if sobrante2 == 1:
            print("1 moneda de $1")


def retiro(saldo):
    os.system("cls")
    print("Ingrese el monto a retirar. \nÚnicamente múltiplos de 100 y máximo $9,300.00 ")
    monto_retirar = int(input("$"))
    monto_retiro = monto_retirar
    if monto_retirar % 100 == 0 and monto_retirar <= 9300:
        print("Se le han entregado: ")
        #Billete 500
        billete500 = monto_retirar // 500
        sobrante500 = monto_retirar % 500
        if billete500 > 0:
            print(f"{billete500} billete(s) de $500")
        #Billete 200
        billete200 = sobrante500 // 200
        sobrante200 = sobrante500 % 200
        if billete200 > 0:
            print(f"{billete200} billete(s) de $200")
        #Billete 200
        billete100 = sobrante200 // 100
        if billete100 > 0:
            print(f"{billete100} billete(s) de $100")
    else: 
        print("La operación no se ha podido realizar. \nPor favor, intente más tarde.")
    nuevo_saldo = saldo - monto_retiro
    saldo = nuevo_saldo
    print(f"Su nuevo saldo es {nuevo_saldo}")
    return nuevo_saldo
    

def run():
    print("Bienvenid@ al cajero automático.")
    print("""¿Qué operación desea realizar?"

    1. Consultar saldo
    2. Comprar tiempo aire
    3. Pago de servicios
    4. Retiro de efectivo
    5. Salir
    """)
    saldo = 50000
    choice = int(input("Escoja una opción con su respectivo número: \n"))
    if choice == 1:
        consulta_saldo(saldo, 0)
        otra_operacion()
    elif choice == 2:
        tiempo_aire()
        otra_operacion()
    elif choice == 3:
        luz()
        otra_operacion()
    elif choice == 4:
        retiro(saldo)
        otra_operacion()
    elif choice == 5:
        print("Gracias por su visita.")
    else:
        print("Por favor, ingrese una opción válida.")
        otra_operacion()


if __name__ == '__main__':
    run()