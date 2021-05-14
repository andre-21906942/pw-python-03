def main():
    print("")


def pede_nome():
    ciclo = True
    while ciclo:
        ficheiro = input("Ficheiro: ")
        extencao = ficheiro.split(".")[1]
        if extencao != "txt":
            continue
        return ficheiro.split(".")[0]


def gera_nome(ficheiro):
    nome = ficheiro.split(".")[0]
    return f"{nome}.json"


if __name__ == "__main__":
        main()