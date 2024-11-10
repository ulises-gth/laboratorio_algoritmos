#Definimos las clases de la persona para despues usarla en el programa mas adelante
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
#Definimos al cliente(persona) y sus atributos despues del self
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
#con el metodo STR imprimimos los detalles del cliente
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Cuenta: {self.numero_cuenta}, Balance: ${self.balance}"
#funcion para gestionar las operaciones de deposito en la cuenta del cliente
    def depositar(self, monto):
        self.balance += monto
        print(f"Depósito de ${monto} realizado. Nuevo balance: ${self.balance}")
#funcion para gestionar las operaciones de retiro en la cuenta del cliente
    def retirar(self, monto):
        if monto > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= monto
            print(f"Retiro de ${monto} realizado. Nuevo balance: ${self.balance}")
#funcion para crear el cliente(para solicitar los datos necesarios)
def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    balance = float(input("Ingrese el balance inicial: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)#para que devuelva un objeto en este caso el cliente
#creamos la funcion para organizar(el menu y sus respectivos ciclos)para que el usuario realize operaciones hasta que quiera quitar el programa
def inicio():
    cliente = crear_cliente()
    print(f"\n¡Bienvenido, {cliente.nombre} {cliente.apellido}!")
#ciclo para mostrar menu interactivoval usuario
    while True:
        print("\n--- Menú de Operaciones ---")
        print("1- Depositar dinero")
        print("2- Retirar dinero")
        print("3- Mostrar balance")
        print("4- Salir")
        opcion = input("Elija una opcion por favor: ")
        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cliente.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cliente.retirar(monto)
        elif opcion == "3":
            print(cliente)
        elif opcion == "4":
            print("Gracias por usar nuestro sistema. Que tengas buen dia")
            print("Trabajo hecho por Ulises Arguello")
            break
        else:
            print("Opción no valida. Intentelo de nuevo")
#este if sin condicionales para poder ejecutar el codigo
if __name__ == "__main__":
    inicio()


















