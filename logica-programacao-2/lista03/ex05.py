def reduceSub(listaA):
    from functools import reduce
    return reduce(lambda x, y: x - y, listaA, 3)