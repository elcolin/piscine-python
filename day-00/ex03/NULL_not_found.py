def NULL_not_found(object: any) -> int:
    object_classes = (None, 0, "", False)
    type_name = ("Nothing:", "Zero:", "Empty:", "Fake:")
    for i, obj in enumerate(object_classes):
        if obj == object:
            print(type_name[i], object, type(obj))
            return 0
    if object != object and object:
        print("Cheese:", object, type(object))
    else:
        print("Type not found")
    return 1