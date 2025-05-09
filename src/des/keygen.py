"""
Round key generation for the DES module.

Authors:
Mithun Sivanesan (c3403606)
"""


def key_init(input_key: str) -> list:
    """
    Initializes key for round key generation
    """
    # fmt: off
    c_table = [57, 49, 41, 33, 25, 17, 9,
               1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27,
               19, 11, 3, 60, 52, 44, 36]
    d_table = [63, 55, 47, 39, 31, 23, 15,
               7, 62, 54, 46, 38, 30, 22,
               14, 6, 61, 53, 45, 37, 29,
               21, 13, 5, 28, 20, 12, 4]
    # fmt: on

    cd_pair = [[], []]
    for i in range(len(28)):
        cd_pair[0].append(input_key[c_table[i] - 1])
        cd_pair[1].append(input_key[d_table[i] - 1])
    return cd_pair
