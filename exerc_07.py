# Verifica se conjuntos são equivalentes
def conjuntos_equivalentes(conjunto1, conjunto2):
    # Verifica se ambos os conjuntos têm os mesmos elementos
    return conjunto1 == conjunto2


# Gerar um Conjunto 
def gerar_conjunto(tam_conjunto):
    conjunto = set()
    for i in range(tam_conjunto):
        item = input("Informe um item do conjunto: ")
        conjunto.add(item)
    
    return conjunto


def main():
    tam_conjuntoA = int(input("Informe o tamanho do conjunto A: "))
    tam_conjuntoB = int(input("Informe o tamanho do conjunto B: "))

    print("Informe os Itens para o Conjunto A")
    conjuntoA = gerar_conjunto(tam_conjuntoA)

    print("Informe os Itens para o Conjunto B")
    conjuntoB = gerar_conjunto(tam_conjuntoB)

    resultado = conjuntos_equivalentes(conjuntoA, conjuntoB)

    print("Saida: ",resultado)


if __name__ == "__main__":
    main()