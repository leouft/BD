class Carro:
    def __init__(self, vin, marca, modelo, versao, ano, cor, valor):
        self.vin = vin
        self.marca = marca
        self.modelo = modelo
        self.versao = versao
        self.ano = ano
        self.cor = cor
        self.valor = valor

# Funções "SQL"

# Obs.: As funções possuem try pra caso não exista um arquivo "carros.txt", é só uma questão de refinamento que quis implementar

def inserir(carro):
    try:
        with open("carros.txt", "r") as file:
            for line in file: # Procurar se já existe um carro com esse VIN
                line = line.strip()
                if line:
                    infos = line.split(";")
                    if int(infos[0]) == carro.vin:
                        return False # Retorna false se encontrar um carro com o mesmo VIN

    except FileNotFoundError:
        pass

    with open("carros.txt", "a") as file:
        carroWrite(file, carro)

    return True # Retorna true se conseguir inserir

def atualizar(carro):
    try:
        with open("carros.txt", "r") as file:
            carros = []
            found = False
            for line in file:
                line = line.strip()
                if line:
                    infos = line.split(";")
                    if int(infos[0]) != carro.vin:
                        carroRead = carroReadCreate(infos)
                        carros.append(carroRead)
                    else:
                        found = True # Vira true se encontrar o carro com o mesmo VIN
                        carros.append(carro)
    except FileNotFoundError:
        return False

    with open("carros.txt", "w") as file:
        for carroTemp in carros:
            carroWrite(file, carroTemp)

    return found # Retorna true se tiver encontrado (que foi atulizado) e false se não tiver encontrado (então nada vai mudar)

def deletar(vin):
    try:
        with open("carros.txt", "r") as file:
            carros = []
            found = False
            for line in file:
                line = line.strip()
                if line:
                    infos = line.split(";")
                    carroRead = carroReadCreate(infos)
                    if int(infos[0]) == vin:
                        found = True # Se torna true ao encontrar o carro de mesmo VIN
                    else:
                        carros.append(carroRead)

    except FileNotFoundError:
        return False

    with open("carros.txt", "w") as file:
        for carroTemp in carros:
            carroWrite(file, carroTemp)

    return found # Retorna true se tiver encontrado o carro para ser deletado (que nesse caso já foi deletado), ou false se não encontrar (então nada muda)

def consulta(vin):
    try:
        with open("carros.txt", "r") as file:
            for line in file:
                line = line.strip()
                infos = line.split(";")
                if int(infos[0]) == vin:
                    carroRead = carroReadCreate(infos)
                    return carroRead # Retorna o carro consultado por VIN
    except FileNotFoundError:
        return None

    return None

def mostrarTodos():
    try:
        with open("carros.txt", "r") as file:
            print(f"{'VIN':<5} {'MARCA':<15} {'MODELO':<20} {'VERSÃO':<30} {'ANO':<5} {'COR':<15} {'VALOR':>10}")
            print("-" * 107)
            for line in file:
                line = line.strip()
                if line:
                    infos = line.split(";")
                    carroRead = carroReadCreate(infos)
                    print(f"{carroRead.vin:<5} {carroRead.marca:<15} {carroRead.modelo:<20} {carroRead.versao:<30} {carroRead.ano:<5} {carroRead.cor:<15} {carroRead.valor:>10.2f}") # Printa todas informações de cada carro
        print()

    except FileNotFoundError:
        print("Arquivo não encontrado.\n")

def consultarInfo(search):
    try:
        search = search.lower()
        with open("carros.txt", "r") as file:
            carros = []
            for line in file:
                line = line.strip()
                if line:
                    infos = line.split(";")
                    for info in infos:
                        info = info.lower()
                        if search in info:
                            carroRead = carroReadCreate(infos)
                            carros.append(carroRead)

        return carros

    except FileNotFoundError:
        return []

# Funções pra evitar repetição

def carroReadCreate(infos):
    return Carro(int(infos[0]), infos[1], infos[2], infos[3], int(infos[4]), infos[5], float(infos[6]))

def carroWrite(file, carro):
    file.write(f"{carro.vin};{carro.marca};{carro.modelo};{carro.versao};{carro.ano};{carro.cor};{carro.valor:g}\n")

# Funções extras

def printCarro(carro):
    if carro:
        print(f"{'VIN':<5} {'MARCA':<15} {'MODELO':<20} {'VERSÃO':<30} {'ANO':<5} {'COR':<15} {'VALOR':>10}")
        print("-" * 107)
        print(f"{carro.vin:<5} {carro.marca:<15} {carro.modelo:<20} {carro.versao:<30} {carro.ano:<5} {carro.cor:<15} {carro.valor:>10.2f}\n")

def printList(carros):
    if carros:
        print(f"{'VIN':<5} {'MARCA':<15} {'MODELO':<20} {'VERSÃO':<30} {'ANO':<5} {'COR':<15} {'VALOR':>10}")
        print("-" * 107)
        for carro in carros:
            print(f"{carro.vin:<5} {carro.marca:<15} {carro.modelo:<20} {carro.versao:<30} {carro.ano:<5} {carro.cor:<15} {carro.valor:>10.2f}")
        print()
    else:
        print("Nenhum carro na lista.\n")


# Execução

while True:
    print("======= MENU =======\n1 - Inserir carro\n2 - Atualizar carro\n3 - Deletar carro\n4 - Mostrar todos\n5 - Consultar\n6 - Sair")
    entrada = int(input("Opção (1 - 6): "))
    match entrada:
        case 1:
            print("\nInsira as informações.")
            vin = int(input("VIN: "))
            carSearch = consulta(vin)
            if carSearch:
                print("\nJá existe um veículo com esse VIN.\n")
                continue
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            version = input("Versão: ")
            ano = int(input("Ano: "))
            cor = input("Cor: ")
            valor = float(input("Valor: "))
            carro = Carro(vin, marca, modelo, version, ano, cor, valor)
            inserir(carro)
            print("\nCarro inserido.\n")
        case 2:
            vin = int(input("\nInsira o VIN do carro: "))
            carSearch = consulta(vin)
            if carSearch:
                print("\nO que deseja atualizar?\n1 - Marca\n2 - Modelo\n3 - Versão\n4 - Ano\n5 - Cor\n6 - Valor\n7 - Atualizar tudo")
                entrada2 = int(input("Opção (1 - 7): "))
                if entrada2 != 7:
                    match entrada2:
                        case 1:
                            carSearch.marca = input("\nDigite a marca: ")
                        case 2:
                            carSearch.modelo = input("\nDigite o modelo: ")
                        case 3:
                            carSearch.versao = input("\nDigite a versão: ")
                        case 4:
                            carSearch.ano = int(input("\nDigite o ano: "))
                        case 5:
                            carSearch.cor = input("\nDigite a cor: ")
                        case 6:
                            carSearch.valor = float(input("\nDigite o valor: "))
                        case _:
                            print("\nOpção inválida.\n")
                            continue
                else:        
                    carSearch.marca = input("Marca: ")
                    carSearch.modelo = input("Modelo: ")
                    carSearch.versao = input("Versão: ")
                    carSearch.ano = int(input("Ano: "))
                    carSearch.cor = input("Cor: ")
                    carSearch.valor = float(input("Valor: "))
                atualizar(carSearch)
                print("\nCarro atualizado.\n")
            else:
                print("\nCarro inexistente.\n")
        case 3:
            vin = int(input("\nInsira o VIN do carro: "))
            if deletar(vin):
                print("\nCarro deletado.\n")
            else:
                print("\nCarro não encontrado.\n")
        case 4:
            mostrarTodos()
        case 5:
            print("\nQual modo de consulta deseja?\n1 - VIN\n2 - Informação")
            entrada2 = int(input("Opção (1 - 2): "))
            if entrada2 == 1:
                vin = int(input("\nInsira o VIN: "))
                carro = consulta(vin)
                if carro:
                    print()
                    printCarro(carro)
                else:
                    print("\nCarro não encontrado.\n")
            else:
                search = input("\nInsira a palavra de busca: ")
                print()
                if not search:
                    print("nNenhuma entrada.\n")
                    continue
                carros = consultarInfo(search)
                if carros:
                    printList(carros)
                else:
                    print("\nNenhum carro encontrado.\n")
        case 6:
            print("\nSaindo...")
            break
        case _:
            print("\nOpção inválida.\n")