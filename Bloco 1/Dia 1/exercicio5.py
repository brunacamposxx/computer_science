# def preço_total(metro):
#     custo_lata = 80
#     cobertura = metro / 3
#     quantidade_latas = int(cobertura / 18)
#     if cobertura % 18:
#         quantidade_latas += 1
#     return quantidade_latas, quantidade_latas * custo_lata


# print(preço_total(100))

import math


def preço_total(metro):
    custo_lata = 80
    cobertura = metro / 3
    quantidade_latas = math.ceil(cobertura / 18)
    return quantidade_latas, quantidade_latas * custo_lata


print(preço_total(100))
