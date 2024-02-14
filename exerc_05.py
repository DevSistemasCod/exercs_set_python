
# Gerar um Conjunto 
def gerar_conjunto(tam_conjunto):

    conjunto = set()
    for i in range(tam_conjunto):
        item = input("Informe um item do conjunto: ")
        conjunto.add(item)
    
    return conjunto

# Gerar a união entre os conjuntos A e B 
def uniaoAB(conjuntoA, conjuntoB):
    # União dos dois conjuntos
    uniao = conjuntoA.union(conjuntoB)
    return uniao

# Gerar a interseção entre os conjuntos B e C 
def intersecaoBC(conjuntoB, conjuntoC):
    # Interseção dos dois conjuntos
    intersecao = conjuntoB.intersection(conjuntoC)
    return intersecao

# Gerar a diferença simétroca entre A e B
def diferenca_simetricaAB(conjuntoA, conjuntoB): 
    diferenca_simetrica = conjuntoA.symmetric_difference(conjuntoB)
    return diferenca_simetrica


def main():
    tam_conjuntoA = int(input("Informe o tamanho do conjunto A: "))
    tam_conjuntoB = int(input("Informe o tamanho do conjunto B: "))
    tam_conjuntoC = int(input("Informe o tamanho do conjunto C: "))

    print("Informe os Itens para o Conjunto A")
    conjuntoA = gerar_conjunto(tam_conjuntoA)

    print("Informe os Itens para o Conjunto B")
    conjuntoB = gerar_conjunto(tam_conjuntoB)

    print("Informe os Itens para o Conjunto C")
    conjuntoC = gerar_conjunto(tam_conjuntoC)

    uniao = uniaoAB(conjuntoA, conjuntoB)
    intersecao = intersecaoBC(conjuntoB, conjuntoC)
    diferenca_simetrica = diferenca_simetricaAB(conjuntoA, conjuntoB)

    print("União: ",uniao)
    print("Interseção: ",intersecao)
    print("Diferenca Simetrica: ",diferenca_simetrica)


if __name__ == "__main__":
    main()