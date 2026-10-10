def NULL_not_found(object: any) -> int:
    """Print the kind of "Null" value given and its type.

    Return 0 if the object is a known "Null" value, 1 otherwise.
    """
    obj_type = type(object)
    if object is None:
        print(f"Nothing: {object} {obj_type}")
    elif obj_type is float and object != object:
        print(f"Cheese: {object} {obj_type}")
    elif obj_type is int and object == 0:
        print(f"Zero: {object} {obj_type}")
    elif obj_type is str and object == "":
        print(f"Empty: {obj_type}")
    elif obj_type is bool and object is False:
        print(f"Fake: {object} {obj_type}")
    else:
        print("Type not Found")
        return 1
    return 0
