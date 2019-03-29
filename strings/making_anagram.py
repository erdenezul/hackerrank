from collections import Counter


def making_anagrams(s1, s2):
    """
    .. doctests::
       >>> making_anagrams('abc', 'cde')
       4
       >>> making_anagrams(
       ...     'absdjkvuahdakejfnfauhdsaavasdlkj',
       ...     'djfladfhiawasdkjvalskufhafablsdkashlahdfa')
       19
    """
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    total = 0
    for key in s1_counter:
        total += abs(s1_counter.get(key) - s2_counter.pop(key, 0))
    for _, value in s2_counter.items():
        total += value

    return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
