"""
Expansion Permutation module for the DES package.

Authors:
Chanelle Velovski (c3431376)
Mithun Sivanesan (c3403606)
"""

from .utils import table_swap

# fmt: off
expansion_table = [32,  1,  2,  3,  4,  5,
                    4,  5,  6,  7,  8,  9,
                    8,  9, 10, 11, 12, 13,
                   12, 13, 14, 15, 16, 17,
                   16, 17, 18, 19, 20, 21,
                   20, 21, 22, 23, 24, 25,
                   24, 25, 26, 27, 28, 29,
                   28, 29, 30, 31, 32,  1]


# fmt: on
def expansion_permutation(right_half_input: str) -> list:
    """
    Expansion permutation adds extra values into the list. 
    It gets the value in the expansion table and matches it with the corresponding 
    index in right half input list. Then it stores that value in a new expansion list.
    """
    return table_swap(expansion_table, right_half_input)

def inverse_expansion_permutation(xor_output: str) -> list:
    """
    Inverse expansion permutation discards all the values at the index which is 
    divisible by 6 and where the modulo is equal to 5.
    """
    output_list = []
    for i in range(48):
        if i % 6 == 0 or i % 6 == 5:
            continue
        output_list.append(xor_output[i])
    return output_list
