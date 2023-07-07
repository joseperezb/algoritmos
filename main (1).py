class Empleado:
    def __init__(self, rol, nombre, cedula):
        self.rol = rol
        self.nombre = nombre
        self.cedula = cedula
        self.balance = 0

    def retirar_dinero(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se han retirado {cantidad} del balance de {self.nombre}.")
        else:
            print("Saldo insuficiente.")

    def pagar_salario(self, cantidad):
        self.balance += cantidad
        print(f"Se ha pagado un salario de {cantidad} a {self.nombre}.")

    def mostrar_informacion(self):
        print(f"""
        Rol: {self.rol}
        Nombre: {self.nombre}
        Cédula: {self.cedula}
        Balance: {self.balance}
        """)

class Nomina:
    def __init__(self, presupuesto):
        self.presupuesto = presupuesto
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print("Empleados:")
        for empleado in self.empleados:
            empleado.mostrar_informacion()

    def pagar_nomina(self):
        total_salarios = 0
        for empleado in self.empleados:
            if empleado.rol == "Programador Junior":
                salario = 1000
            elif empleado.rol == "Programador Senior":
                salario = 2000
            elif empleado.rol == "Manager":
                salario = 3000
            else:
                salario = 0

            if salario <= self.presupuesto:
                empleado.pagar_salario(salario)
                total_salarios += salario
                self.presupuesto -= salario

        print(f"Se ha pagado un total de {total_salarios} en salarios.")

    def agregar_presupuesto(self, cantidad):
        self.presupuesto += cantidad
        print(f"Se ha agregado {cantidad} al presupuesto de nómina.")


def menu():
    nomina = Nomina(5000)

    while True:
        print("""
        Menú Principal
        1. Registrar empleado
        2. Mostrar empleados
        3. Pagar nómina
        4. Agregar presupuesto
        5. Salir
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            rol = input("Rol del empleado: ")
            nombre = input("Nombre del empleado: ")
            cedula = input("Cédula del empleado: ")
            empleado = Empleado(rol, nombre, cedula)
            nomina.agregar_empleado(empleado)
            print("Empleado registrado exitosamente.")
        elif opcion == "2":
            nomina.mostrar_empleados()
        elif opcion == "3":
            nomina.pagar_nomina()
        elif opcion == "4":
            cantidad = float(input("Cantidad a agregar al presupuesto: "))
            nomina.agregar_presupuesto(cantidad)
        elif opcion == "5":
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


menu()
print('Arreglo Agregado')

      
