print("informe a distância percorrida em km")
distancia = float(input())
print("informe o combustível gasto em litros")
combustivel = float(input())
consumo = distancia / combustivel
print("nessa viagem, a distância percorrida foi de",distancia, "km o gasto de combustível foi de", combustivel,"L o consumo foi de", round(consumo, 2), "km/l")