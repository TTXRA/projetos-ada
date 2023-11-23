def cria_arquivo_json(chaves, valores):
    json_str = "{"

    for i in range(len(chaves)):
        json_str += f'"{chaves[i]}": {valores[i]}'
        if i != len(chaves) - 1:
            json_str += ", "

    json_str += "}"

    return json_str