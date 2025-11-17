nulls_tab = {None: "Nothing", 0: "Zero", "": "Empty", "false": "Fake", "nan": "Cheese"}


def NULL_not_found(object) -> int:
    kind = type(object)

    if kind is bool and object is False:
        object = "false"
    elif kind is float and object != object:
        object = "nan"

    if object in nulls_tab:
        print(f"{nulls_tab[object]}: {object} {kind}")
        return 0

    print("Type not Found")
    return 1
