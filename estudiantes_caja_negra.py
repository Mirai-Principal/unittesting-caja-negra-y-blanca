import unittest
# Escenario 2: Sistema de Calificación de Estudiantes
# Funcionalidad: Asignar una calificación final basada en el promedio de las calificaciones obtenidas en cuatro exámenes. Los criterios son:
# • Si el promedio es de 90 o más, el estudiante obtiene una "A".
# • Si el promedio es entre 80 y 89, el estudiante obtiene una "B".
# • Si el promedio es entre 70 y 79, el estudiante obtiene una "C".
# • Si el promedio es menor a 70, el estudiante obtiene una "F".

class evaluacion:
    def __init__(self, promedio):
        self.promedio = promedio
        self.evaluacion = ''

    def evaluar(self):
        if self.promedio >= 90:
            self.evaluacion = 'A'
        elif self.promedio >= 80 and self.promedio < 90:
            self.evaluacion = 'B'
        elif self.promedio >= 70 and self.promedio < 80:
            self.evaluacion = 'C'
        elif self.promedio < 70:
            self.evaluacion = 'F'
        return self.evaluacion

class pruebaCajaNegra(unittest.TestCase):
    def test_caso1(self):
        evaluador = evaluacion(95)
        esperado = 'A'
        self.assertEqual(evaluador.evaluar(), esperado)
    def test_caso2(self):
        evaluador = evaluacion(85)
        esperado = 'B'
        self.assertEqual(evaluador.evaluar(), esperado)
    def test_caso3(self):
        evaluador = evaluacion(75)
        esperado = 'C'
        self.assertEqual(evaluador.evaluar(), esperado)
    def test_caso4(self):
        evaluador = evaluacion(65)
        esperado = 'F'
        self.assertEqual(evaluador.evaluar(), esperado)

# Casos de Prueba:
# 1. Entrada: promedio = 95 → Salida esperada: "A".
# 2. Entrada: promedio = 85 → Salida esperada: "B".
# 3. Entrada: promedio = 75 → Salida esperada: "C".
# 4. Entrada: promedio = 65 → Salida esperada: "F".

if __name__ == '__main__':
    unittest.main()