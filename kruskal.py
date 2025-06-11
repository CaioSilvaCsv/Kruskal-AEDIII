#A classe UninionFind

class UnionFind:
  def __init__(self, n):
    # A lista 'pai' armazena o pai de cada elemento.
    self.pai = list(range(n))
    # 'nivel' ajuda a otimizar as uniões.
    self.nivel = [0] * n

  # Busca o chefe do grupo de um elemento.
  def busca(self, i):
    if self.pai[i] != i:
      self.pai[i] = self.busca(self.pai[i])
    return self.pai[i]
  
  def unir(self, i, j):
    raiz_i = self.busca(i)
    raiz_j = self.busca(j)
    if raiz_i != raiz_j:
      if self.nivel[raiz_i]> self.nivel[raiz_j]:
        self.pai[raiz_j] = raiz_i
      else:
        self.pai[raiz_i] = raiz_j
        if self.nivel[raiz_i] == self.nivel[raiz_j]:
          self.nivel[raiz_j] += 1
      return True
    return False
  
def kruskal(vertices, lista_arestas):
  #Dicionario tradutor de nomes para indices
  mapa_indice = {nome: i for i, nome in enumerate(vertices)}

  # Pega o número total de vértices
  numero_vertices = len(vertices)

  #Ordena a lista de arestas pelo peso
  arestas_ordenadas = sorted(lista_arestas)

  #Inicia lista de resultados e peso
  mst = []
  peso_total = 0

  #Cria a ferramenta com numero de vertices.
  uf = UnionFind(numero_vertices)

  for peso, nome_u, nome_v in arestas_ordenadas:
    # Traduz para que a unionFind entenda.
    indice_u = mapa_indice[nome_u]
    indice_v = mapa_indice[nome_v]

    # Usa os indices para testar e unir os grupos
    if uf.unir(indice_u, indice_v):
      #Se não formou um ciclo, adiciona a AGM.
      mst.append((nome_u, nome_v, peso))
      peso_total += peso
  
  #Retorna o resultado com os nomes traduzidos
  return{
    'mst'         : mst,
    'peso_total'  : peso_total
  }

if __name__ == '__main__':
  print("Calculadora MST - Kruskal")

  entrada_vertices = input("Digite os nomes dos vértices, separados por espaço (ex: A B C...): ")
  nomes_vertices = sorted(list(set(entrada_vertices.split())))

  print(f"Vértices definidos: {', '.join(nomes_vertices)}")
  print("_"* 20)
  

  arestas = []
  print("Digite uma aresta por vez (ex: A D 5): ")
  
  while True:
    entrada_aresta = input(">")

    if not entrada_aresta:
      break

    partes = entrada_aresta.split()
    if len(partes) != 3:
      print("Formato inválido!")
      continue

    vertice_u, vertice_v, peso = partes[0].upper(), partes[1].upper(), partes[2]

    if vertice_u not in nomes_vertices or vertice_v not in nomes_vertices: 
      print(f"Error: Vertice '{vertice_u}' ou '{vertice_v}' não existe. Verifique: {','.join(nomes_vertices)}")
      continue
    try:
      peso_numerico = int(peso)
      arestas.append((peso_numerico, vertice_u, vertice_v))
      print(f"Aresta ({vertice_u} - {vertice_v}) com peso {peso_numerico} adicionado")
    except ValueError:
      print("Erro: O peso deve ser um numero inteiro.")

  print("_"*20)

  if not arestas:
    print("Nenhuma areasta foi inserida")
  else:
    resultado = kruskal(nomes_vertices, arestas)

    print("Arestas na Árvore Geradora Minima: ")
    for u,v, peso in resultado['mst']:
      print(f"({u} - {v}) com peso {peso}")
    
    print(f"\nPeso total da AGM (MST) : {resultado['peso_total']}")
