def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    for f in Lf:
        if not f(n):
            return False
    return True

# Examples:    
print(all_true(6, [lambda x: x % 2 == 0, lambda x: x > 0]))