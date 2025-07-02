No finger exercise for lecture 24

But i want to write merge sort:

def merge_sort(L):
    """ L is a list of ints """
    if len(L) <= 1:
        return L
    else:
        mid = len(L)//2
        L1 = merge_sort(L[:mid])
        L2 = merge_sort(L[mid:])
        return merge(L1, L2)

def merge(L1, L2):
    """ L1 and L2 are lists of ints """
    merged = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    while i < len(L1):
        merged.append(L1[i])
        i += 1
    while j < len(L2):
        merged.append(L2[j])
        j += 1
    return merged