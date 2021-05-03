import math

pi = float(3.14)
raio = float(0)

base = float(0)
altura = float(0)

units = ["milimetros", "centimetros", "metros"]
activeUnit = units[1]

resultList = []


def listCalc():
    print("Calculos realizados nesta sessao:")
    for i in range(len(resultList)):
        print(f"{i} - {resultList[i]}")


def chooseUnit():
    global units
    global activeUnit

    print("\nEscolha uma unidade de medida para calcular:")
    for i in range(len(units)):
        print(f"{i} - {units[i]}")

    unitIndex = int(input("\nUnidade: "))
    activeUnit = units[unitIndex]

    return activeUnit


def keepCalcFunction():
    keepCalc = str(input("\nDeseja fazer outro calculo? (S/N) ").upper())
    if keepCalc == "S":
        figure_list()
    elif keepCalc == "N":
        print("Bye!")
        exit
    else:
        print("Opcao invalida!")
        keepCalcFunction()


# ---------------------------------


def circumference():
    global pi
    global activeUnit

    raio = float(input(f"\nDigite o raio do circulo (em {activeUnit}): "))
    changePi = input("Deseja alterar o valor de pi? (S/N) ").upper()

    if (changePi == "S"):
        print(f"Valor atual de pi: {pi}")
        pi = float(input("Digite o novo valor para pi: "))
    else:
        print("valor de pi nao foi alterado")

    circumferenceValue = 2*pi*raio

    msg = f"Pi: {pi} | Raio: {raio} {activeUnit}\nCircunferencia: "
    return [circumferenceValue, msg]


def areaCircle():
    global pi
    global activeUnit

    raio = float(input(f"\nDigite o raio do circulo (em {activeUnit}): "))
    changePi = input("Deseja alterar o valor de pi? (S/N) ").upper()

    if (changePi == "S"):
        print(f"Valor atual de pi: {pi}")
        pi = float(input("Digite o novo valor para pi: "))
    else:
        print("valor de pi nao foi alterado")

    areaValue = pi*math.pow(raio, 2)
    msg = f"Pi: {pi} | Raio: {raio} {activeUnit}\nArea do circulo: "
    return [areaValue, msg]


def Circle():
    switcher = {
        1: {
            'name': 'Circunferencia',
            'function': circumference
        },
        2: {
            'name': 'Area',
            'function': areaCircle
        }
    }

    print("\nCalculos disponiveis:")
    for i, value in switcher.items():
        print(i, '-', value['name'])

    choiceCalc = int(input("Digite o indice do calculo desejado: "))
    function = switcher[choiceCalc]['function']
    result = function()

    return result


# ---------------------------------


def perimeter():
    global activeUnit

    base = float(
        input(f"\nAgora, digite a base do retangulo (em {activeUnit}): "))
    altura = float(input(f"E a altura do retangulo (em {activeUnit}): "))

    perimeterValue = (base*2)+(altura*2)
    msg = f"Base: {base} {activeUnit} | Altura: {altura} {activeUnit}\nPerimetro: "

    return [perimeterValue, msg]


def areaRectangle():
    global activeUnit

    base = float(
        input(f"\nAgora, digite a base do retangulo (em {activeUnit}): "))
    altura = float(input(f"E a altura do retangulo (em {activeUnit}): "))

    areaValue = base * altura
    msg = f"Base: {base} {activeUnit} | Altura: {altura} {activeUnit}\nArea do retangulo: "

    return [areaValue, msg]


def Rectangle():
    switcher = {
        1: {
            'name': 'Perimetro',
            'function': perimeter
        },
        2: {
            'name': 'Area',
            'function': areaRectangle
        }
    }

    print("\nCalculos disponiveis:")
    for i, value in switcher.items():
        print(i, '-', value['name'])

    choiceCalc = int(input("Digite o indice do cálculo desejado: "))
    function = switcher[choiceCalc]['function']
    result = function()

    return result


# ---------------------------------


def figure_list():
    switcher = {
        1: {
            'name': 'Circulo',
            'function': Circle
        },
        2: {
            'name': "Retangulo",
            'function': Rectangle
        },
    }

    print("Figuras disponiveis:")
    for i, value in switcher.items():
        print(i, '-', value['name'])

    print(f"{(len(switcher)+1)} - SAIR")
    choice = int(input("\nDigite o indice da figura desejada: "))

    if (choice > len(switcher) or choice < 1):
        print("Bye!")
        quit()

    activeUnit = chooseUnit()

    function = switcher[choice]['function']
    result, msg = function()
    formatResult = str(round(result, 2))

    print(
        f"\nResultado do cálculo do {switcher[choice]['name']} em {activeUnit}: \n"
    )
    resultMsg = msg, formatResult, activeUnit

    print(msg, formatResult, activeUnit)
    print("\n")

    # formatResultMsg = " | ".join(resultMsg)

    resultList.append(resultMsg)

    listCalc()

    keepCalcFunction()

    input("\npressione Enter para sair...")


figure_list()
