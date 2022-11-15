def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    new_phone = []
    for phone in list_phones:
        new_phone.append(sanitize_phone_number(phone))

    result = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }
    for phone in new_phone:
        if phone.startswith("81"):
            result["JP"].append(phone)
        elif phone.startswith("65"):
            result["SG"].append(phone)
        elif phone.startswith("886"):
            result["TW"].append(phone)
        elif phone.startswith("380"):
            result["UA"].append(phone)
        else:
            result["UA"].append(phone)

    return result


get_phone_numbers_for_countries(
    ['065-875-94-11', '(81)8765347', '8867658976', '657658976', '(65)765-89-77'])
