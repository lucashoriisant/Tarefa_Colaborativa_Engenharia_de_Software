import math

pi = float(3.14)
raio = float(0)

base = float(0)
altura = float(0)

unit = "cm"


def recebeDadosCirculo(pi, raio):
    raio = float(input("\nAgora, digite o raio do circulo: "))
    changePi = input("Deseja alterar o valor de pi? (S/N) ")

    if (changePi == "S"):
        print(f"Valor atual de pi: {pi}")
        pi = float(input("Digite o novo valor para pi: "))
    else:
        print("valor de pi não foi alterado")

    return [pi, raio]


def calculaCircunferenciaCirculo(pi, raio):
    return 2*pi*raio


def calculaAreaCirculo(pi, raio):
    return pi*math.pow(raio, 2)


def recebeDadosRetangulo(base, altura):
    base = float(input("\nAgora, digite a base do retangulo: "))
    altura = float(input("E a altura do retângulo: "))

    return [base, altura]


def calculaPerimetroRetangulo(base, altura):
    return (base*2)+(altura*2)


def calculaAreaRetangulo(base, altura):
    return base*altura


print("CALCULO DE AREA E PERIMETRO\n===============\n")
print("Figuras disponiveis:\n  1 - Circulo\n  2 - Retangulo")
chooseFigure = int(input("Digite o índice da figura desejada: "))

# Círculo
if (chooseFigure == 1):
    piCirculo, raioCirculo = recebeDadosCirculo(pi, raio)

    print("\nCalculos disponiveis em circulo:\n  1 - Perimetro\n  2 - Area")
    chooseCalc = int(input("Digite o índice do calculo desejado: "))
    if chooseCalc == 1:
        # Perímetro circunferência
        print(f"Pi: {piCirculo} | Raio: {raioCirculo}.")

        circunferenciaCirculo = calculaCircunferenciaCirculo(
            piCirculo, raioCirculo)
        print(f"Perímetro da circunferência: {circunferenciaCirculo}")
    elif chooseCalc == 2:
        # Área circunferência
        print(f"Pi: {piCirculo} | Raio: {raioCirculo}.")

        areaCirculo = calculaAreaCirculo(piCirculo, raioCirculo)
        print(f"Área da circunferência: {areaCirculo}")
    else:
        print("ERRO")
        exit
# Retângulo
elif (chooseFigure == 2):
    baseRet, alturaRet = recebeDadosRetangulo(base, altura)

    print("\nCalculos disponiveis em retangulo:\n  1 - Perimetro\n  2 - Area")
    chooseCalc = int(input("Digite o índice do calculo desejado: "))
    if chooseCalc == 1:
        # Perímetro retangulo
        perimetroRetangulo = calculaPerimetroRetangulo(baseRet, alturaRet)
        print(f"Perímetro do retângulo: {perimetroRetangulo}")
    elif chooseCalc == 2:
        # Área retângulo
        areaRetangulo = calculaAreaRetangulo(baseRet, alturaRet)
        print(f"Área do retângulo: {areaRetangulo}")
    else:
        print("ERRO")
        exit
# Error
else:
    print("ERRO")
    exit
