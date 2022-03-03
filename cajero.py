import os


def cambio(monto):
    numero = int(input("Ingrese su número celular: "))
    print("Ha escogido una recarga de $" + monto)
    pagado = int(input("Ingrese el monto con el que desea pagar: \n$"))
    if pagado < monto:
        print("La operación no se ha podido realizar.")
    else:
       cambio = pagado - monto
       cambio = str(cambio)
       monto = str(monto)
       numero = str(numero)
       print("La operación se ha realizado con éxito. Se ha recargado $" + monto + " al número " + numero)
       print("Su cambio es $" + cambio)



def otra_operacion():
    otra_opera = input("""\n¿Desea realizar otra operación?
    Escriba sí o no: 
    """)
    if otra_opera == "si" or otra_opera == "si " or otra_opera == "sí" or otra_opera == "sí ":
        run()
    else:
        print("Vuelva pronto.")


def consulta_saldo(nuevo_saldo):
    os.system("cls")
    nip = input('Ingrese su NIP: ')
    if nip == 1:
        saldo -= nuevo_saldo
        saldo = str(saldo)
        print("Su saldo es $" + saldo)
    otra_operacion()


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
        elif eleccion2 == 2:
            cambio(100)
        elif eleccion2 == 2:
            cambio(150)
        elif eleccion2 == 2:
            cambio(200)
        elif eleccion2 == 2:
            cambio(500)

        print("\nLa compra de tiempo aire se ha realizado con éxito.")
        otra_operacion()


def luz():
    os.system("cls")
    print("Por el momento solo está disponible el pago de luz.")
    servicio = input("Ingrese su número de servico/referencia: ")
    a_pagar = int(input("Ingrese el monto a pagar: $"))
    pagado = int(input("Ingrese el dinero con el que va a pagar: $"))
    cambio = pagado - a_pagar
    if cambio < 0:
        print("Su pago no se ha podido realizar. Intente más tarde.")
    else:
        print("Su cambio es:")
        #Billete 200
        billete200 = cambio // 200
        billete200 = str(billete200)
        sobrante200 = cambio % 200
        print(billete200 + " billete(s) de $200")
        #Billete 100
        billete100 = sobrante200 // 100
        billete100 = str(billete100)
        sobrante100 = sobrante200 % 100
        print(billete100 + " billete(s) de $100")
        #Billete 50
        billete50 = sobrante100 // 50
        billete50 = str(billete50)
        sobrante50 = sobrante100 % 50
        print(billete50 + " billete(s) de $50")
        #Billete 20
        billete20 = sobrante50 // 20
        billete20 = str(billete20)
        sobrante20 = sobrante50 % 20
        print(billete20 + " billete(s) de $20")
        #Moneda 10
        moneda10 = sobrante20 // 10
        moneda10 = str(moneda10)
        sobrante10 = sobrante20 % 10
        print(moneda10 + " moneda(s) de $10")
        #Moneda 5
        moneda5 = sobrante10 // 5
        moneda5 = str(moneda5)
        sobrante5 = sobrante10 % 5
        print(moneda5 + " moneda(s) de $5")
        #Moneda 2
        moneda2 = sobrante5 // 2
        moneda2 = str(moneda2)
        sobrante2 = sobrante5 % 2
        print(moneda2 + " moneda(s) de $2")
        #Moneda peso
        if sobrante2 == 1:
            print("1 moneda de $1")
        else:
            print("0 monedas de $1")
        print("El pago se ha realizado con éxito.")
        otra_operacion()


def retiro():
    os.system("cls")
    print("Ingrese el monto a retirar. \nÚnicamente múltiplos de 100 y máximo $9,300.00 ")
    monto_retirar = int(input("$"))
    if monto_retirar % 100 == 0 and monto_retirar <= 9300:
        print("Se le han entregado: ")
        #Billete 500
        billete500 = monto_retirar // 500
        billete500 = str(billete500)
        sobrante500 = monto_retirar % 500
        print(billete500 + " billete(s) de $500")
        #Billete 200
        billete200 = sobrante500 // 200
        billete200 = str(billete200)
        sobrante200 = sobrante500 % 200
        print(billete200 + " billete(s) de $200")
        #Billete 200
        billete100 = sobrante200 // 100
        billete100 = str(billete100)
        print(billete100 + " billete(s) de $100")
        otra_operacion()
    else: 
        print("La operación no se ha podido realizar. \nPor favor, intente más tarde.")
        otra_operacion()
    

def run():
    print("Bienvenid@ al cajero automátio.")
    print("""¿Qué operación desea realizar?"

    1. Consultar saldo
    2. Comprar tiempo aire
    3. Pago de servicios
    4. Retiro de efectivo
    """)
    saldo = 50000
    choice = int(input("Escoja una opción con su respectivo número: "))
    if choice == 1:
        consulta_saldo()
    elif choice == 2:
        tiempo_aire(saldo)
    elif choice == 3:
        luz()
    elif choice == 4:
        retiro()
    else:
        print("Por favor, ingrese una opción válida.")
        otra_operacion()


if __name__ == '__main__':
    run()