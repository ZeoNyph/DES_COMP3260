"""
File: main.py
Authors: Mithun Sivanesan (C3403606), Chanelle Velovski (C3431376)
Description: This contains the main implementation of the DES algorithm.
"""

import os
import sys
from des import ip, exp, perms, sbox, keygen
from des.utils import utils


p = []
k = []
c = []


def main():
    """
    Main method for the DES encryption program.
    Handles argument parsing and uses file_parse() to handle file parsing.
    """
    if len(sys.argv) <= 2:
        print("Usage: main.py [OPTIONS] [FILEPATH]\nOptions:\n-e: Encrypt\n-d: Decrypt")
        sys.exit(1)
    else:
        match sys.argv[1]:
            case "-e":
                print(f"Encrypting {sys.argv[2]}")
                if file_parse(sys.argv[2], True) == -1:
                    sys.exit(1)
                print(p[0])
                print(encrypt(0, p[0], k[0]))
            case "-d":
                print(f"Decrypting {sys.argv[2]}")
                if file_parse(sys.argv[2], False) == -1:
                    sys.exit(1)
                print(f"{c}{k}")
            case _:
                print(f"Unknown command {sys.argv[1]}. Exiting...")
                sys.exit(1)
    sys.exit(0)


def file_parse(filepath: str, is_encrypt: bool) -> int:
    """
    Parses file for gathering input for DES encryption and/or decryption.

    Encryption input:
    PLAINTEXT
    AVALANCHE PLAINTEXT
    KEY
    AVALANCHE KEY

    Decryption input:
    CIPHERTEXT
    KEY
    """
    if not os.path.exists(filepath):
        print("File not found. Exiting...")
        return -1
    with open(file=filepath, encoding="utf-8") as file:
        if is_encrypt:
            p.append(file.readline().strip())
            p.append(file.readline().strip())
            k.append(file.readline().strip())
            k.append(file.readline().strip())
            for x in p[:]:
                if not x.strip():
                    p.remove(x)
            for x in k[:]:
                if not x.strip():
                    k.remove(x)
            if len(p) != 2 or len(k) != 2:
                print("File does not contain all the required values. Exiting...")
                return -1
        else:
            c.append(file.readline().strip())
            k.append(file.readline().strip())
            for x in c[:]:
                if not x.strip():
                    c.remove(x)
            for x in k[:]:
                if not x.strip():
                    k.remove(x)
            if len(c) != 1 or len(k) != 1:
                print("File does not contain all the required values. Exiting...")
                return -1
        file.close()
    return 0


def encrypt(des_type: int, plaintext: str, key: str) -> str:
    ciphertext = ip.initial_permutation(plaintext, True)
    keys = keygen.key_generation(key)
    for i in range(16):
        lh = "".join(ciphertext[:32])
        rh = "".join(ciphertext[32:])
        f_rh = "".join(exp.expansion_permutation(ciphertext[32:]))
        if des_type != 1:
            f_rh = utils.xor(f_rh, keys[i])
        if des_type != 2:
            f_rh = sbox.sbox_function(f_rh)
        else:
            f_rh = "".join(exp.inverse_expansion_permutation(f_rh))
        if des_type != 3:
            f_rh = "".join(perms.permutation(f_rh))
        f_rh = utils.xor(lh, f_rh)
        ciphertext = rh + f_rh
    ciphertext = ciphertext[32:] + ciphertext[:32]
    ciphertext = "".join(ip.initial_permutation(ciphertext, False))
    return ciphertext


if __name__ == "__main__":
    main()
