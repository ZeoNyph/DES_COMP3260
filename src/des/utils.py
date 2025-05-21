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
