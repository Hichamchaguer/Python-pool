import math

def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing : None", type(object))
        return 0
    elif (isinstance(object, bool) and object == False):
        print("Fake: False", type(object))
        return 0
    elif (isinstance(object, float) and math.isnan(object)):
        print("Cheese: NaN", type(object))
        return 0
    elif (isinstance(object, int) and object == 0):
        print("Zero: 0", type(object))
        return 0
    elif (isinstance(object, str) and len(object) == 0):
        print("Empty:", type(object))
        return 0
    else:
        print("Type not found")
        return 1


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False


NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))