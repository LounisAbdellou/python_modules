container_names = {
    list: "List",
    tuple: "Tuple",
    set: "Set",
    dict: "Dict",
}


def all_thing_is_obj(object) -> int:
    kind = type(object)

    if isinstance(object, str):
        print(f"{object} is in the kitchen: {kind}")
    elif kind in container_names:
        print(f"{container_names[kind]}: {kind}")
    else:
        print("Type not found")
    return 42
