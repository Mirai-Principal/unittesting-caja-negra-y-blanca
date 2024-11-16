import unittest
# Escenario 2: Cálculo de Descuento en Carrito de Compras
# Funcionalidad: Crear una función que aplique un descuento al total de la compra según las condiciones:
# • Si el total de la compra es mayor o igual a $100 y menor que $200, aplicar un 10% de descuento.
# • Si el total de la compra es de $200 o más, aplicar un 20% de descuento.
# • Si el total de la compra es menor a $100, no aplicar descuento.

# Casos de prueba (cobertura de caminos):
# 1. Ruta 1: total_compra = 250 → Aplica el 20% de descuento.
# 2. Ruta 2: total_compra = 150 → Aplica el 10% de descuento.
# 3. Ruta 3: total_compra = 50 → Sin descuento.
class compra:
    def aplicar_descuento(self, monto):
        valor = monto
        if(valor >= 200):
            valor = valor - valor * 0.2
        elif valor >= 100 and valor < 200 :
            valor = valor - valor * 0.1
        return valor

class pruebaCajaNegra(unittest.TestCase):
    def test_caso1(self):
        monto = 250
        esperado = 200
        cajero = compra()
        self.assertEqual(cajero.aplicar_descuento(monto), esperado)

    def test_caso2(self):
        monto = 150
        esperado = 135
        cajero = compra()
        self.assertEqual(cajero.aplicar_descuento(monto), esperado)
        
    def test_caso3(self):
        monto = 50
        esperado = 50
        cajero = compra()
        self.assertEqual(cajero.aplicar_descuento(monto), esperado)

    

if __name__ == "__main__":
    unittest.main()