import unittest

# Escenario 1: Sistema de descuento de tienda
# Funcionalidad: Aplicar un descuento en función del total de la compra. Si el monto es mayor a $100, se aplica un 10% de descuento; si es mayor a $200, se aplica un 20%.
class compra:
    def aplicar_descuento(self, monto):
        valor = monto
        if(valor >= 200):
            valor = valor - valor * 0.2
        elif valor < 200 and valor >= 100:
            valor = valor - valor * 0.1
        return valor

# Casos de prueba:
# 1. Entrada: $50 → Esperado: $50 (sin descuento).
# 2. Entrada: $150 → Esperado: $135 (10% descuento).
# 3. Entrada: $250 → Esperado: $200 (20% descuento).

class pruebaCajaNegra(unittest.TestCase):
    def test_caso1(self):
        monto = 50
        esperado = 50
        cajero = compra()
        self.assertEqual(cajero.aplicar_descuento(monto), esperado)

    def test_caso2(self):
        monto = 150
        esperado = 135
        cajero = compra()
        self.assertEqual(cajero.aplicar_descuento(monto), esperado)
    def test_caso3(self):
        monto = 250
        esperado = 200
        cajero = compra()
        self.assertEqual(cajero.aplicar_descuento(monto), esperado)

if __name__ == '__main__':
    unittest.main()