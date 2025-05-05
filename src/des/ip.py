"""
Initial permutation module for the DES package.

Authors:
Chanelle Velovski (c3431376)
Mithun Sivanesan (c3403606)
"""


def initial_permutation(input_string: str) -> list:
    """
    Given a binary string as input, performs initial permutation to give a permutated output.
    """
    input_list = []
    ip_table = [
        58,
        50,
        42,
        34,
        26,
        18,
        10,
        2,
        60,
        52,
        44,
        36,
        28,
        20,
        12,
        4,
        62,
        54,
        46,
        38,
        30,
        22,
        14,
        6,
        64,
        56,
        48,
        40,
        32,
        24,
        16,
        8,
        57,
        49,
        41,
        33,
        25,
        17,
        9,
        1,
        59,
        51,
        43,
        35,
        27,
        19,
        11,
        3,
        61,
        53,
        45,
        37,
        29,
        21,
        13,
        5,
        63,
        55,
        47,
        39,
        31,
        23,
        15,
        7,
    ]

    for i, value in enumerate(ip_table):
        value = value - 1
        index_val = input_string[value]
        input_list.append(index_val)
    return input_list
