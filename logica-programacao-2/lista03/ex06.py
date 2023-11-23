from functools import reduce


def ger_reduce(dictA):
    return reduce(lambda a, b: a + b, map(lambda x: x**2, dictA), 0)
