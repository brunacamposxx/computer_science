arr = ['João', 'Maria', 'José', 'Pedro', 'Ana', 'Paulo', 'Fernanda']


def procura_maior_nome(arr):
    maior_nome = arr[0]
    for index in arr:
        if len(index) > len(maior_nome):
            maior_nome = index
    return maior_nome


print(procura_maior_nome(arr))
