""" 
Crea una clase "CuentaBancaria" que tenga atributos para el nombre del titular y el saldo. 
Agrega métodos para depositar y retirar dinero, así como uno para mostrar el saldo actual.
"""

class CuentaBancaria:
    def __init__(self, nombre_titular, saldo):
        self.nombre = nombre_titular
        self.saldo = saldo

    def depositar(self, cantidad):
        # Validamos que la cantidad sea positiva
        if (cantidad > 0):
            self.saldo += cantidad
        else:
            print("La cantidad a depositar debe ser positiva")
    
    def retirar(self, cantidad):
        # Validamos que la cantidad sea positiva y menor o igual al saldo actual
        if (cantidad > 0 and cantidad <= self.saldo):
            self.saldo -= cantidad
        else:
            print("La cantidad a retirar es inválida")

    def get_saldo(self):
        return self.saldo

cuenta_1 = CuentaBancaria("Miguel", 1000) # Se crea un objeto CuentaBancaria
cuenta_1.depositar(2.55)
print(cuenta_1.get_saldo())
cuenta_1.retirar(1000)
print(cuenta_1.get_saldo()) 


        
        