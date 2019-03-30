def strong_password(s):
    """
    Its length is at least .
    It contains at least one digit.
    It contains at least one lowercase English character.
    It contains at least one uppercase English character.
    It contains at least one special character. The special characters are: !@#$%^&*()-+

    .. doctests::
       >>> strong_password('Ab1')
       3
       >>> strong_password('#Hackerrank')
       1
    """
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    map_requirements = {}
    extra = 0 if len(s)>=6 else 6 - len(s)
    for c in s:
        if c in numbers:
            map_requirements['n'] = 1
        elif c in lower_case:
            map_requirements['l'] = 1
        elif c in upper_case:
            map_requirements['u'] = 1
        elif c in special_characters:
            map_requirements['s'] = 1

    return max(extra, 4- len(map_requirements.keys()))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
