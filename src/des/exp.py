"""
Expansion Permutation module for the DES package.

Authors:
Chanelle Velovski (c3431376)
Mithun Sivanesan (c3403606)
"""

expansion_table = [32,  1,  2,  3,  4,  5,
                    4,  5,  6,  7,  8,  9,
                    8,  9, 10, 11, 12, 13,
                   12, 13, 14, 15, 16, 17,
                   16, 17, 18, 19, 20, 21,
                   20, 21, 22, 23, 24, 25,
                   24, 25, 26, 27, 28, 29,
                   28, 29, 30, 31, 32,  1]

def expansion_permutation(right_half_input: str) -> list :
    """
    Expansion permutation views the value in the expansion 
    table and matches it with the corresponding index in right half input list.
    Then it stores that value in a new expansion list.
    """
    # for i in range(len(right_half_input),0, 4):
    #     first_eight_bits = []
    #     first_eight_bits.append(right_half_input[i])
    #     # for i in range(len(right_half_input),3, 4):
    #     last_eight_bits = []
    #     last_eight_bits.append(right_half_input[i])
    # first_element = first_eight_bits[1:]
    # first_eight_bits.pop(0)

    # last_element = last_eight_bits[:-1]
    # last_eight_bits.pop()

    expansion_output = []
    for i, value in enumerate(expansion_table):
        value = value - 1
        index_val = right_half_input[value]
        expansion_output.append(index_val)
    return expansion_output
