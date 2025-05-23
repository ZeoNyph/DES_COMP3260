"""
Utility functions used by the DES module.

Created by: Mithun Sivanesan (c3403606)
"""


def xor(block1: str, block2: str) -> str:
    """
    Returns the XOR output of two binary strings.
    """
    out = str()
    if len(block1) != len(block2):
        raise ValueError("Input blocks must have the same length")
    for b1, b2 in zip(block1, block2):
        out += "1" if b1 != b2 else "0"

    return out


def table_swap(table: list, input_str: str) -> list:
    """
    A function that creates an output based on a binary string input and a list table.
    """
    output_list = []
    for i, value in enumerate(table):
        value = value - 1
        index_val = input_str[value]
        output_list.append(index_val)
    return output_list
