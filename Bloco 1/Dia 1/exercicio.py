def media_aritmetica(num):
    soma = 0
    for index in num:
        soma += index
    return soma / len(num)


print(media_aritmetica([1, 2, 3, 4, 5]))
