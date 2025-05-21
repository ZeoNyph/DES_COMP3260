"""
DES module for COMP3260 Assessment 2.
This module contains the functions for DES, such as:

- Initial permutation (ip)
- Expansion permutation (exp)
- S boxes (sbox)
- Permutation P (perms)
- Round key generation (keygen)
"""

from .exp import expansion_permutation
from .keygen import key_generation
from .utils import xor
