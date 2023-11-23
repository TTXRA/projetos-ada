def min_max_temperatura(temperaturas):
    temp_max = max(temperaturas, key=lambda x: x[1])
    data_max = temp_max[0]

    temp_min = min(temperaturas, key=lambda x: x[1])
    data_min = temp_min[0]

    return [data_max, data_min]
