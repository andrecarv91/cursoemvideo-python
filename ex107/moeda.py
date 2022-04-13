def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


def dobro(n):
    n *= 2
    return n


def metade(n):
    n *= 0.5
    return n

