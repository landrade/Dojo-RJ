#!/usr/bin/env python
 
import unittest

from maior_triangulo import monta_maior_triangulo_possivel
from maior_triangulo import adiciona_espacos_em_branco_em_um_triangulo
from maior_triangulo import acha_maior_triangulo

class test_maior_triangulo(unittest.TestCase):

  def test_monta_maior_triangulo_possivel_1(self):
    self.assertEqual(monta_maior_triangulo_possivel(1, 2), ['-#'])

  def test_monta_maior_triangulo_possivel_2(self):
    self.assertEqual(monta_maior_triangulo_possivel(2, 5), ['---##', 
                                                            '#-###'])

  def test_monta_maior_triangulo_possivel_3(self):
    self.assertEqual(monta_maior_triangulo_possivel(3, 10), ['-----#####', 
                                                             '#---######',
                                                             '##-#######'])


  def test_adiciona_espacos_em_branco_em_um_triangulo_1(self):
    self.assertEqual(adiciona_espacos_em_branco_em_um_triangulo(['---', '-']),['---', '#-#'])

  def test_adiciona_espacos_em_branco_em_um_triangulo_2(self):
    self.assertEqual(adiciona_espacos_em_branco_em_um_triangulo(['-----', '---', '-']),['-----', '#---#', '##-##'])


  def test_acha_maior_triangulo_1(self):
    self.assertEqual(acha_maior_triangulo(['#-##----#', '-----#-', '---#-', '-#-', '-']), 9)

  def test_acha_maior_triangulo_2(self):
    self.assertEqual(acha_maior_triangulo(['#-#-#--', '#---#', '##-', '-']), 4)

  def test_acha_maior_triangulo_3(self):
    self.assertEqual(acha_maior_triangulo(['#']), 0)


 
if __name__ == '__main__':
  unittest.main()