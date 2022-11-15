def sanitize_phone_number(phone):
    phone_list = []
    for i in phone:
        if (i != ' ') and (i != '(') and (i != ")") and (i != '-') and (i != '+'):
            phone_list.append(i)
    result = ''.join(phone_list)
    return result


sanitize_phone_number(" 38 086 888 88 88 ")
