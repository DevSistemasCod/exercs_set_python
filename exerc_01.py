
def manipular_conjunto(tam_conjunto):
    conjunto = set()
    meus_nros = {100,33,60,5}

    for i in range(tam_conjunto):
        item = int(input("Informe o item: "))
        conjunto.add(item)

    print("1: Conjunto: ",conjunto) 
    
    #validar se o set esta vazio
    if(len(conjunto) == 0):
        print("O conjunto está vazio.")
    else:
        # removendo um item aleatório do conjunto
        conjunto.pop()
    
    print("2: Conjunto: ",conjunto) 

    #usando o update
    #conjunto.update(meus_nros)
    #print("3: Conjunto: ",conjunto) 

    #usando o union
    conjunto_final = conjunto.union(meus_nros)
    print("3: Conjunto: ",conjunto_final) 


def main():
    tam_conjunto = int(input("Informe o tamanho do conjunto: "))
    manipular_conjunto(tam_conjunto)


if __name__ == "__main__":
    main()