import unittest
import math
# Escenario 1: Calcular el área de un triángulo
# Funcionalidad: Calcular el área de un triángulo, dado el tipo de triángulo: equilátero, isósceles o escaleno.
class calcular_areas:
    def calcular_area(self, tipo, base = None, altura = None, lado = None):
        if tipo == 'equilatero':
            if lado is None:
                return "Datos insuficientes"
            area = (lado ** 2 * math.sqrt(3)) / 4
            return area
        elif tipo == 'isosceles':
            if base is None or altura is None:
                return "Datos insuficientes"
            area = (base * altura) / 2
            return area
        elif tipo == 'escaleno':
            if base is None or altura is None:
                return "Datos insuficientes"
            area = (base * altura) / 2
            return area
        else:
            return "Tipo de triángulo no válido"
# Casos de prueba (cobertura de rutas):
# 1. Caso 1: tipo = "equilatero", lado = 5 → Calcula área de un triángulo equilátero.
# 2. Caso 2: tipo = "isosceles", base = 4, altura = 3 → Calcula área de un triángulo isósceles.
# 3. Caso 3: tipo = "escaleno", base = 4, altura = 3 → Calcula área de un triángulo escaleno.
# 4. Caso 4: tipo no coincide con los valores válidos, base y altura no especificadas → Devuelve "Datos insuficientes".
class pruebaCajaBlanca(unittest.TestCase):
    def test_equilatero(self):
        calculadora = calcular_areas()
        resultado = calculadora.calcular_area( 'equilatero', lado = 5)
        esperado = 10.8253
        self.assertAlmostEqual(resultado, esperado, 4)
    def test_isosceles(self):
        calculadora = calcular_areas()
        resultado = calculadora.calcular_area("isosceles", base=4, altura=3)
        self.assertEqual(resultado, 6)
    
    def test_escaleno(self):
        calculadora = calcular_areas()
        resultado = calculadora.calcular_area("escaleno", base=4, altura=3)
        self.assertEqual(resultado, 6)

    def test_datos_insuficientes(self):
        calculadora = calcular_areas()
        
        resultado = calculadora.calcular_area("equilatero")
        self.assertEqual(resultado, "Datos insuficientes")
        
        resultado = calculadora.calcular_area("isosceles")
        self.assertEqual(resultado, "Datos insuficientes")
        
        resultado = calculadora.calcular_area("escaleno")
        self.assertEqual(resultado, "Datos insuficientes")

    def test_tipo_no_valido(self):
        calculadora = calcular_areas()
        resultado = calculadora.calcular_area("rectangulo", base=4, altura=3)
        self.assertEqual(resultado, "Tipo de triángulo no válido")

if __name__ == "__main__":
    unittest.main()