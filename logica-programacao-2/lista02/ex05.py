def encontraConsoantes(listaStrings):
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    return ''.join([c for c in listaStrings if c.lower() in consoantes])