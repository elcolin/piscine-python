def all_thing_is_obj(object: any) -> int:
    object_classes = (list, tuple, set, dict)
    type_name = ("List", "Tuple", "Set", "Dict")
    for i, obj in enumerate(object_classes):
        if (isinstance(object, obj)):
            print(type_name[i], ":", obj)
            return 42
    if (isinstance(object, str)):
        print(object, "is in the kitchen :", str)
    else:
        print("Type not found")
    return 42