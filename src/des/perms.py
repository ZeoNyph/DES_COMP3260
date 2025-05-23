# fmt: off
permutation_table = [16, 7, 20, 21, 29, 12, 28, 17,
                     1, 15, 23, 26, 5, 18, 31, 10,
                     2, 8, 24, 14, 32, 27, 3, 9,
                     19, 13, 30, 6, 22, 11, 4, 25]

#fmt : on
def permutation(input_string: str) -> list:
    """
    Permutation function that takes in a binary string and returns a permutated list.
    """
    output_list = []
    for i, value in enumerate(permutation_table):
        value = value - 1
        index_val = input_string[value]
        output_list.append(index_val)
    return output_list
