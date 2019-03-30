def construction(s):
    """
    Append a character to the end of string p at a cost of 1 dollar
    Choose any substring of p and append it to the end of p at no charge.
    .. doctests::
       >>> construction('abcd')
       4
       >>> construction('abab')
       2
       >>> construction('bccb')
       2
    """
    char_map = {}
    cost = 0
    for _, value in enumerate(s):
        if value not in char_map:
            char_map[value] = 1
            cost += 1
    return cost


if __name__ == '__main__':
    import doctest
    doctest.testmod()
