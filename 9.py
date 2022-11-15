def formatted_numbers():
    result_list = []
    result_list.append('|{:^10}|{:^10}|{:^10}|'.format(
        "decimal", "hex", "binary"))
    for i in range(16):
        result_list.append('|{:<10d}|{:^10x}|{:>10b}|'.format(i, i, i))
    return result_list


print(formatted_numbers())
