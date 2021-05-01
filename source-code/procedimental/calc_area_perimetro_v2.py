import math

pi = float(3.14)
raio = float(0)

base = float(0)
altura = float(0)


def circumference():
    global pi

    raio = float(input("\nDigite o raio do circulo: "))
    changePi = input("Deseja alterar o valor de pi? (S/N) ").upper()

    if (changePi == "S"):
        print(f"Valor atual de pi: {pi}")
        pi = float(input("Digite o novo valor para pi: "))
    else:
        print("valor de pi nao foi alterado")

    circumferenceValue = 2*pi*raio
    msg = f"Pi: {pi} | Raio: {raio}\nCircunferencia: "
    return [circumferenceValue, msg]


def areaCircle():
    global pi

    raio = float(input("\nDigite o raio do circulo: "))
    changePi = input("Deseja alterar o valor de pi? (S/N) ").upper()

    if (changePi == "S"):
        print(f"Valor atual de pi: {pi}")
        pi = float(input("Digite o novo valor para pi: "))
    else:
        print("valor de pi nao foi alterado")

    areaValue = pi*math.pow(raio, 2)
    msg = f"Pi: {pi} | Raio: {raio}\nArea do circulo: "
    return [areaValue, msg]


def Circle():
    switcher = {
        1: circumference,
        2: areaCircle,
    }
    choiceCalc = int(input("Digite o calculo desejado: "))
    func = switcher.get(choiceCalc, lambda: "Escolha invalida")
    result = func()

    return result


#############################


def perimeter():
    base = float(input("\nAgora, digite a base do retangulo: "))
    altura = float(input("E a altura do retangulo: "))

    perimeterValue = (base*2)+(altura*2)
    msg = f"Base: {base} | Altura: {altura}\nPerimetro: "

    return [perimeterValue, msg]


def areaRectangle():
    base = float(input("\nAgora, digite a base do retangulo: "))
    altura = float(input("E a altura do retangulo: "))

    areaValue = base * altura
    msg = f"Base: {base} | Altura: {altura}\nArea do retangulo: "

    return [areaValue, msg]


def Rectangle():
    switcher = {
        1: perimeter,
        2: areaRectangle,
    }
    choiceCalc = int(input("Digite o cálculo desejado: "))
    func = switcher.get(choiceCalc, lambda: "Escolha invalida")
    result = func()

    return result


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
        # 1: circle,
        # 2: rectangle,
    }

    print("Figuras disponíveis:\n")

    # for key, value in switcher.items():
    #     print(key, ' : ', value)

    choice = int(input("Digite o indice da figura desejada: "))

    # func = switcher.get(choice, lambda: "Escolha invalida")
    function = switcher[choice]['function']
    result, msg = function()
    formatResult = round(result, 2)

    print(
        f"Resultado do cálculo em {switcher[choice]['name']}: \n"
    )
    print(msg, formatResult)

    input("\npressione Enter para sair...")


figure_list()