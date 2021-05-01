import math

pi = float(3.14)
raio = float(0)

base = float(0)
altura = float(0)


def recebeDadosCirculo(pi, raio):
    raio = float(input("Digite o raio da circunferência:"))
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
    base = float(input("Digite a base do retangulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    return [base, altura]


def calculaPerimetroRetangulo(base, altura):
    return (base*2)+(altura*2)


def calculaAreaRetangulo(base, altura):
    return base*altura


print("CALCULO DE ÁREA E PERÍMETRO\n===============\n")

# Perímetro circunferência
print("\nPerímetro da circunferência\n")

piCirculo, raioCirculo = recebeDadosCirculo(pi, raio)
print(f"Pi: {piCirculo} | Raio: {raioCirculo}.")
circunferenciaCirculo = calculaCircunferenciaCirculo(piCirculo, raioCirculo)
print(f"Perímetro da circunferência: {circunferenciaCirculo}")


# Área circunferência
print("\nÁrea da circunferência\n")

piCirculo, raioCirculo = recebeDadosCirculo(pi, raio)
areaCirculo = calculaAreaCirculo(piCirculo, raioCirculo)
print(f"Área da circunferência: {areaCirculo}")

# Perímetro retangulo
print("\nPerímetro do retangulo\n")

baseRet, alturaRet = recebeDadosRetangulo(base, altura)
perimetroRetangulo = calculaPerimetroRetangulo(baseRet, alturaRet)
print(f"Perímetro do retângulo: {perimetroRetangulo}")


# Área retângulo
print("\nÁrea do retângulo\n")
baseRet, alturaRet = recebeDadosRetangulo(base, altura)
areaRetangulo = calculaAreaRetangulo(baseRet, alturaRet)
print(f"Área do retângulo: {areaRetangulo}")
