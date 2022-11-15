def real_len(text):
    y = []
    y.append(text)
    while y[-1].find("\n") != -1:
        y.append(y[-1].replace("\n", ""))
    while y[-1].find("\f") != -1:
        y.append(y[-1].replace("\f", ""))
    while y[-1].find("\r") != -1:
        y.append(y[-1].replace("\r", ""))
    while y[-1].find("\t") != -1:
        y.append(y[-1].replace("\t", ""))
    while y[-1].find("\v") != -1:
        y.append(y[-1].replace("\v", ""))
    result = len(y[-1])
    return result


l = real_len('Alex\nKdfe23\t\f\v.\r')
print(l)
