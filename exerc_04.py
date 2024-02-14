
# Gerar um Conjunto 
def gerar_conjunto(tam_conjunto):
    conjunto = set()
    for i in range(tam_conjunto):
        item = input("Informe um item do conjunto: ")
        conjunto.add(item)
    
    return conjunto

# validar se subconjunto de 1 esta contido em 2
def verificar_se_subconjunto(conjunto_1, conjunto_2):
    return conjunto_1.issubset(conjunto_2)

def main():
    tam_conjunto1 = int(input("Informe o tamanho do conjunto 1: "))
    tam_conjunto2 = int(input("Informe o tamanho do conjunto 2: "))

    print("Informe os Itens para o Conjunto 1")
    conjunto_1 = gerar_conjunto(tam_conjunto1)

    print("Informe os Itens para o Conjunto 2")
    conjunto_2 = gerar_conjunto(tam_conjunto2)

    retorno_conj = verificar_se_subconjunto(conjunto_1, conjunto_2)
    if (retorno_conj):
        print("O conjunto 1 é um subconjunto de conjunto 2")
    else:
        print("O conjunto 1 NÂO é um subconjunto de conjunto 2")

if __name__ == "__main__":
    main()