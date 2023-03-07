
class Compra:
    def __init__(self, cliente, productos, direccion_envio):
        self.cliente = cliente
        self.productos = productos
        self.direccion_envio = direccion_envio

    def mostrar_resumen(self):
        print("Resumen de compra:")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Email: {self.cliente.email}")
        print(f"Dirección: {self.cliente.direccion}")
        print(f"Tarjeta de crédito: {self.cliente.tarjeta_credito}")
        print("Productos comprados:")
        for producto in self.productos:
            print(f"- {producto.nombre}")
        print(f"Dirección de envío: {self.direccion_envio}")

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Crear un cliente nuevo
cliente1 = Cliente("Juan Perez", "juanperez@gmail.com", "Calle Falsa 123", "1234567890123456")

# Crear una compra nueva
producto1 = Producto("Camiseta", 25.99)
compra1 = Compra(cliente1, [producto1], "Calle Falsa 123")

# Agregar la compra a la lista de compras realizadas por el cliente
cliente1.agregar_compra(compra1)

# Mostrar las compras realizadas por el cliente
cliente1.mostrar_compras()

