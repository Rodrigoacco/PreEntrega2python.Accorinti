class Cliente:
    def __init__(self, nombre, email, direccion, tarjeta_credito):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.tarjeta_credito = tarjeta_credito
        self.compras_realizadas = []

    def agregar_compra(self, compra):
        self.compras_realizadas.append(compra)

    def mostrar_compras(self):
        print(f"Compras realizadas por {self}:")
        for compra in self.compras_realizadas:
            print(f"- {compra.mostrar_resumen()}")

    def __str__(self):
        return self.nombre
    
    