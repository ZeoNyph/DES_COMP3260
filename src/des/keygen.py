"""
Round key generation for the DES module.

Authors:
Mithun Sivanesan (c3403606)
Chanelle Velovski (c3431376)
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

    if len(input_key) != 64:
        raise ValueError("KEY LENGTH MUST BE 64 BITS")

    cd_pair = [[], []]
    for i in range(len(28)):
        cd_pair[0].append(input_key[c_table[i] - 1])
        cd_pair[1].append(input_key[d_table[i] - 1])
    return cd_pair


def key_rotate(cd_pair: list, round_no: int) -> list:
    """
    Performs left rotation of Ci and Di.

    Rotates by 1 bit if round 1, 2, 9, or 16, otherwise 2
    """
    shift_no = 1 if round_no in [1, 2, 9, 16] else 2
    new_cd_pair = [[], []]
    for i in range(28):
        if i < (shift_no - 1):
            new_cd_pair.append(cd_pair[0][i])
            new_cd_pair.append(cd_pair[1][i])
        else:
            new_cd_pair.insert(0, cd_pair[0][i])
            new_cd_pair.insert(0, cd_pair[1][i])
    return new_cd_pair


def round_key_permutation(cd_pair: list) -> str:
    """
    Performs PC2 (Permutation Choice 2) on Ci and Di to give out a round key.
    """
    # fmt: off
    rk_table = [14, 17, 11, 24, 1, 5, 3, 28,
                 15, 6, 21, 10, 23, 19, 12, 4,
                 26, 8, 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55, 30, 40,
                 51, 45, 33, 48, 44, 49, 39, 56,
                 34, 53, 46, 42, 50, 36, 29, 32]
    # fmt: on
    init_bits = cd_pair[0] + cd_pair[1]
    round_key = ""
    for i in range(48):
        round_key = round_key + str(init_bits[rk_table[i] - 1])
    return round_key


def key_generation(input_key: str) -> list:
    """
    Generates 16 round keys for use in DES.
    """
    cd_pair = key_init(input_key)
    keys = []
    for i in range(16):
        cd_pair = key_rotate(cd_pair, i)
        keys.append(round_key_permutation(cd_pair))
    return keys
