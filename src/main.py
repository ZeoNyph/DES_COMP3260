"""
File: main.py
Authors: Mithun Sivanesan (C3403606), Chanelle Velovski (C3431376)
Description: This contains the main implementation of the DES algorithm.
"""

import os
import sys
from des import ip, exp, perms, sbox


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
        exp.expansion_permutation()
        perms.permutation()
        sbox.sboxFunction()
        sys.exit(1)
    else:
        match sys.argv[1]:
            case "-e":
                print(f"Encrypting {sys.argv[2]}")
                if file_parse(sys.argv[2], True) == -1:
                    sys.exit(1)
                print(f"{p}{k}")
                out = ip.initial_permutation(p[0])
                string = ""
                for i, value in out:
                    string = string + value
                print(f"{string}")
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


if __name__ == "__main__":
    main()
