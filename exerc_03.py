
#obter apenas as letras únicas da frase
def obter_letras_unicas(frase):
    #converter frase para minusculo
    minha_string = frase.lower()
    #substituir " " por ""
    minha_string = minha_string.replace(" ","")
    #converter string para set
    conjunto = set (minha_string)
    return conjunto

def main():
    frase = input("Escreva uma frase: ")
    conjunto = obter_letras_unicas(frase)
    print(conjunto) 

if __name__ == "__main__":
    main()