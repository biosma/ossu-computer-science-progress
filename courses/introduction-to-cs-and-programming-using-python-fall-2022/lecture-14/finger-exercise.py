def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    list_of_keys = []
    for key in aDict:
        if aDict[key] == target:
            list_of_keys.append(key)
    return sorted(list_of_keys)

# Examples:
aDict = {5:2, 1:2, 2:4}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]

def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    list_of_keys = []
    for key in d:
        if sum(d[key]) > 0:
            list_of_keys.append(key)
    return sorted(list_of_keys)

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]