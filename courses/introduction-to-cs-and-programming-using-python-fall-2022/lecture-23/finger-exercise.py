Finger Exercise Lecture 23
Question 1: Choose the worst case asymptotic order of growth (upper and lower bound) for the following function. Assume n = a.
Answer 1: Lower bound = Ω(a), Upper bound = O(a) then θ = Θ(a)
def running_product(a):
    """ a is an int """
    product = 1
    for i in range(5,a+5):
        product *= i
        if product == a:
            return True
    return False

Question 2: Choose the worst case asymptotic order of growth (upper and lower bound) for the following function. Assume n = len(L).
Answer 2: Lower bound = Ω(n**2), Upper bound = O(n**2) then θ = Θ(n**2)
def tricky_f(L, L2):
    """ L and L2 are lists of equal length """
    inL = False
    for e1 in L:
        if e1 in L2:
            inL = True
    inL2 = False
    for e2 in L2:
        if e2 in L:
            inL2 = True
    return inL and inL2

It could be better if the function was written as:
def tricky_f(L, L2):
    """ L and L2 are lists of equal length """
    inL = False
    setL2 = set(L2)
    for e1 in L:
        if e1 in setL2:
            inL = True
    return inL
This assures Θ(n) time complexity because setL2 = set(L2) is lineal time.

Question 3: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function.
Answer 3: Lower bound = Ω(log n), Upper bound = O(log n) then θ = Θ(log n), because n = int(n/10) removes the last element dividing it by 10.
def sum_f(n):
    """ n > 0 """
    answer = 0
    while n > 0:
        answer += n%10
        n = int(n/10)
    return answer
