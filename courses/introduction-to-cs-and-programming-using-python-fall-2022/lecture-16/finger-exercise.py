def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    if len(L) == 0:
        return []
    else:
        if type(L[0]) is not list:
            return [L[0]] + flatten(L[1:])
        else:
            return flatten(L[0]) + flatten(L[1:])
# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]