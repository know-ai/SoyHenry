import unittest
import os
from HW01 import checkpoint as ch

class HenryHomeworks(unittest.TestCase):
    def test_numero_binario_01(self):
      valor_test = ch.numero_binario(12)
      valor_esperado = 1100
      self.assertEqual(valor_test, valor_esperado)

    def test_numero_binario_02(self):
      valor_test = ch.numero_binario(33.4)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_numero_binario_03(self):
      valor_test = ch.numero_binario(-30)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_numero_binario_04(self):
      valor_test = ch.numero_binario(256)
      valor_esperado = 100000000
      self.assertEqual(valor_test, valor_esperado)

    def test_binario_numero_01(self):
      valor_test = ch.binario_numero(1100)
      valor_esperado = 12
      self.assertEqual(valor_test, valor_esperado)

    def test_binario_numero_02(self):
      valor_test = ch.binario_numero(100000000)
      valor_esperado = 256
      self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))