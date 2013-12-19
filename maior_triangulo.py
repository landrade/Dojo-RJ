import re

def monta_maior_triangulo_possivel(qtdLinha, qtdCaracteresPorLinha):
  triangulo = []
  for i in range(qtdLinha):
    linha = '#' * i
    linha += '-' * (2 * (qtdLinha - i) - 1)
    faltaQuantosCaracteres = qtdCaracteresPorLinha - len(linha)
    linha += '#' * faltaQuantosCaracteres
    triangulo.append(linha)

  return triangulo

def adiciona_espacos_em_branco_em_um_triangulo(triangulo):
  novoTriangulo = []
  for i in range(len(triangulo)):
    novoTriangulo.append(('#' * i) + triangulo[i] + ('#' * i))
  return novoTriangulo

def monta_regex(triangulo):
  expressao = triangulo.replace('#', ' ')
  expressao = expressao.rstrip()
  expressao = expressao.replace(' ', '.')
  return re.compile(expressao)


def acha_maior_triangulo(triangulo):
  for i in range(len(triangulo)):
    expressaoMaiorTrianguloParaBaixo = monta_regex(''.join(monta_maior_triangulo_possivel(len(triangulo)-i, len(triangulo[0]))))
    expressaoMaiorTrianguloParaCima = monta_regex(''.join(monta_maior_triangulo_possivel(len(triangulo)-i, len(triangulo[0]))[::-1]))
    representacaoTriangulo = ''.join(adiciona_espacos_em_branco_em_um_triangulo(triangulo))
    if expressaoMaiorTrianguloParaBaixo.search(representacaoTriangulo):
      return (len(triangulo)-i) * (len(triangulo)-i)

    if expressaoMaiorTrianguloParaCima.search(representacaoTriangulo):
      return (len(triangulo)-i) * (len(triangulo)-i)

  return 0
    
