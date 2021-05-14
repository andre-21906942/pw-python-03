def main():
    print("")


def calcula_linhas(ficheiro):
    file = open(ficheiro, "r")
    nLinhas = 0
    for linha in file:
        if linha != "\n":
            nLinhas += 1
    return nLinhas


def calcula_caracteres(ficheiro):
    file = open(ficheiro, "r")
    caracteres = file.read()
    return len(caracteres)


def calcula_palavra_comprida(ficheiro):
    file = open(ficheiro, "r")
    palavras = file.read().split()
    maior_palavra = max(palavras, key=len)
    return f"A maior palavra é : {maior_palavra}"


def calcula_ocorrencia_de_letras(ficheiro):
    file = open(ficheiro, "r")
    texto = file.read()
    letras = {}
    for i in texto:
        if i.lower() in letras:
            letras[i.lower()] += 1
        else:
            letras[i.lower()] = 1


if __name__ == "__main__":
    main()
