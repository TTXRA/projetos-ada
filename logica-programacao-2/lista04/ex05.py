def converte_para_json(json_string, chave):
    import json
    json_dic = json.loads(json_string)

    return json_dic[chave]