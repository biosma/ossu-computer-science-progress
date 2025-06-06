def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    count = 0
    for i in range(len(nums_list)):
        for j in range(len(nums_list)):
            if nums_list[i]**2 == nums_list[j]:
                count += 1
    return count
# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3