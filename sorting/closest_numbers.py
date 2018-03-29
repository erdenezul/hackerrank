from collections import defaultdict


def closest_numbers(array):
    # Complete this function
    array = sorted(array)
    current_max = array[-1]
    pair_map = defaultdict(list)
    for i in range(n-1):
        diff = array[i + 1] - array[i]
        pair_map[diff].extend([array[i], array[i + 1]])
        if current_max > diff:
            current_max = array[i + 1] - array[i]
    return pair_map.get(current_max)

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = closest_numbers(arr)
    print " ".join(map(str, result))
