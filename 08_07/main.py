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

def consultarMarca(marca):
    try:
        with open("carros.txt", "r") as file:
            carros = []
            for line in file:
                line = line.strip()
                if line:
                    infos = line.split(";")
                    if infos[1] == marca:
                        carroRead = carroReadCreate(infos)
                        carros.append(carroRead)

        return carros # Retorna um vetor com todos os carros de determinada marca  

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


# Testes
carro = Carro(31, "Fiat", "Uno", "Mille Way Economy", 2009, "Prata", 23200)

# # Inserção
if inserir(carro):
    print("Carro inserido.\n")
else:
    print("VIN já pertence a outro carro.\n")


# # Atualização
carro.valor = 23200
if atualizar(carro):
    print("Carro atualizado.\n")
else:
    print("VIN não encontrado.\n")


# # Deleção
if deletar(31):
    print("Carro deletado.")
    inserir(carro)
    print("Carro inserido novamente.\n")
else:
    print("VIN não encontrado ou arquivo inexistente.\n")


# # Consulta
carroConsultado = consulta(31)
if carroConsultado:
    printCarro(carroConsultado)
else:
    print("Nenhum carro encontrado.\n")


# # Mostrar Todos
mostrarTodos()


# # Consultar Marca
printList(consultarMarca("Toyota"))