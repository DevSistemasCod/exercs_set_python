
#Adiciona elementos em uma lista
def adicionar_em_lista(tam_lista):
    lista = []
    for i in range(tam_lista):
        elemento = int(input("Informe um número: "))
        lista.append(elemento)
    
    return lista

#Verifica elementos comuns entre duas listas
def criar_set_elementos_comuns(lista1, lista2):
    conjunto = set ()

    #validar se ambas as listas não estão vazias
    if not lista1 and not lista2:
        print("Listas vazias")
    else:
        # convernte para conjunto e combina as duas listas  
        conjunto = set(lista1).intersection(lista2)

    return conjunto  


def main():
    tam_lista1 =int(input("Informe o tamanho da 1ª lista: "))
    tam_lista2 =int(input("Informe o tamanho da 2ª lista: "))

    print("Informe os elementos da 1ª lista: ")
    lista1 = adicionar_em_lista(tam_lista1)    
    print("Informe os elementos da 2ª lista: ")
    lista2 = adicionar_em_lista(tam_lista2)    

    conjunto = criar_set_elementos_comuns(lista1, lista2)
    if not conjunto:
        print("Conjunto Vazio! \n Não existem elementos comuns")
    else:
        print("Elementos comuns: ",conjunto)


if __name__ == "__main__":
    main()