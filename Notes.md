# NOTES

This file outlines the initial development of COMP3260 A2.

## Stuff to work on

- I/O handling (file parsing, arguments, printing output)
- DES F function (do for 16 rounds):
    - Expansion permutation
    - XOR with round key
    - S boxes
    - Permutation P
- IP (Initial Permutation) and its inverse
- Input padding (if needed)
- Parity bit selection (every 8th bit)
- Avalanche Effect (key and plaintext)
- Decryption
- Report
    - 250 word Avalanche discussion
    - 500 word reflection

## Structure 

- main.py (Stores the file and arg parse, as well as core DES method)
- des (module containing neccessary functions)
    - \_init_.py (inits module)
    - exp.py (expansion permutation and inverse of it)
    - sbox.py (S-boxes)
    - perms.py (permutations)