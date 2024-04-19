def gerar_conjunto(tamanho_conjunto):
    conjunto = set()

    for i in range(tamanho_conjunto):
        item = int(input("Informe o item: ")) #se quiser para letra tirar o int
        conjunto.add(item)
   
    return conjunto


def diferenca_conjunto(conjA , conjB):
    return (conjA.difference(conjB))


def main():
    tam_conj1 = int(input("Informe o tamanho do primeiro conjunto: "))
    conjunto1 = gerar_conjunto(tam_conj1)
    tam_conj2 = int(input("Informe o tamanho do segundo conjunto: "))
    conjunto2 = gerar_conjunto(tam_conj2)

    # Diferença
    print("Diferença 1 dos conjuntos: ")
    diferenca = diferenca_conjunto(conjunto1,conjunto2)
    diferenca2 = diferenca_conjunto(conjunto2,conjunto1)
    uniao = diferenca.union(diferenca2)
    print(f"A diferença entre 1º e o 2º conjunto: ",uniao)


if __name__ == "__main__":
    main()