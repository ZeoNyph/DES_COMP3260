"""
File: main.py
Authors: Mithun Sivanesan (C3403606), Chanelle Velovski (C3431376)
Description: This contains the main implementation of the DES algorithm.
"""

import os
import sys
import time
from des import ip, exp, perms, sbox, keygen
from des.utils import utils


p = []
k = []
# c[des_type][avalanche_type]
c = [[], [], [], []]
# round_c[des_type][avalanche_type][round-1]
round_c = [[[], [], []], [[], [], []], [[], [], []], [[], [], []]]
# avalanche[des_type][avalanche_comparison_type]
avalanche = [[[], []], [[], []], [[], []], [[], []]]


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
                start = time.perf_counter()
                for i in range(4):
                    encrypt(i, p[0], k[0], 0)
                    encrypt(i, p[1], k[0], 1)
                    encrypt(i, p[0], k[1], 2)
                # sets up avalanche array for output
                for i in range(4):
                    # round 0 plaintext comparison
                    avalanche[i][0].append(avalanche_comparison(p[0], p[1]))
                    avalanche[i][1].append(avalanche_comparison(p[0], p[0]))
                    # DES 16 round comparison
                    for j in range(16):
                        # comparing P with P' with the same K
                        avalanche[i][0].append(
                            avalanche_comparison(round_c[i][0][j], round_c[i][1][j])
                        )
                        # comparing K and K' with the same P
                        avalanche[i][1].append(
                            avalanche_comparison(round_c[i][0][j], round_c[i][2][j])
                        )
                end = time.perf_counter()
                output(end - start, True)
                print("Output saved to ./output.txt")
            case "-d":
                print(f"Decrypting {sys.argv[2]}")
                if file_parse(sys.argv[2], False) == -1:
                    sys.exit(1)
                for i in range(4):
                    decrypt(i, c[0][0], k[0])
                print(p[0])
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
            if len(p) != 2 or len(k) != 2:
                print("File does not contain all the required values. Exiting...")
                return -1
        else:
            c[0].append(file.readline().strip())
            k.append(file.readline().strip())
            if len(c[0]) != 1 or len(k) != 1:
                print("File does not contain all the required values. Exiting...")
                return -1
        file.close()
    return 0


def encrypt(des_type: int, plaintext: str, key: str, ciphertext_type: int) -> str:
    """
    This function performs DES encryption on a given 64-bit binary string using a 64 bit key.

    As per the assessment spec, the function can do four different types of DES:

    DES0: Standard Feistel function
        (Expansion permutation, XOR with round key, S-boxes, Permutation P)
    DES1: No round key XOR
    DES2: Inverse expansion permutation instead of S-boxes
    DES3: No permutation P

    Ciphertext type determines the type of avalanche effect being used:
    0 - regular inputs
    1 - bit-flipped plaintext
    2 - bit-flipped key
    """
    ciphertext = ip.initial_permutation(plaintext, True)
    keys = keygen.key_generation(key)
    for i in range(16):
        # separate into halves
        lh = "".join(ciphertext[:32])
        rh = "".join(ciphertext[32:])
        # separate instance of right half to keep original right half for next round
        f_rh = "".join(exp.expansion_permutation(ciphertext[32:]))
        if des_type != 1:  # skip xor with round key (DES1)
            f_rh = utils.xor(f_rh, keys[i])
        if des_type != 2:  # do inv exp if DES2
            f_rh = sbox.sbox_function(f_rh)
        else:
            f_rh = "".join(exp.inverse_expansion_permutation(f_rh))
        if des_type != 3:  # skip P (DES3)
            f_rh = "".join(perms.permutation(f_rh))
        f_rh = utils.xor(lh, f_rh)
        ciphertext = rh + f_rh
        round_c[des_type][ciphertext_type].append(
            ciphertext
        )  # for avalanche comparison later
    # 32-bit swap
    ciphertext = ciphertext[32:] + ciphertext[:32]
    ciphertext = "".join(
        ip.initial_permutation(ciphertext, False)
    )  # IP^-1 at end of round 16
    c[des_type].append(ciphertext)


def decrypt(des_type: int, ciphertext: str, key: str):
    """
    This function performs DES decryption on a given 64-bit binary string using a 64 bit key.

    As per the assessment spec, the function can do four different types of DES:

    DES0: Standard Feistel function
        (Expansion permutation, XOR with round key, S-boxes, Permutation P)
    DES1: No round key XOR
    DES2: Inverse expansion permutation instead of S-boxes
    DES3: No permutation P
    """
    plaintext = ip.initial_permutation(ciphertext, True)
    keys = keygen.key_generation(key)
    for i in range(15, -1, -1):
        # separate into halves
        lh = "".join(plaintext[:32])
        rh = "".join(plaintext[32:])
        # separate instance of right half to keep original right half for next round
        f_rh = "".join(exp.expansion_permutation(plaintext[32:]))
        if des_type != 1:  # skip xor with round key (DES1)
            f_rh = utils.xor(f_rh, keys[i])
        if des_type != 2:  # do inv exp if DES2
            f_rh = sbox.sbox_function(f_rh)
        else:
            f_rh = "".join(exp.inverse_expansion_permutation(f_rh))
        if des_type != 3:  # skip P (DES3)
            f_rh = "".join(perms.permutation(f_rh))
        f_rh = utils.xor(lh, f_rh)
        plaintext = rh + f_rh
    # 32-bit swap
    plaintext = plaintext[32:] + plaintext[:32]
    plaintext = "".join(
        ip.initial_permutation(plaintext, False)
    )  # IP^-1 at end of round 16
    p.append(plaintext)


def output(running_time: float, is_encrypt: bool):
    """
    Creates output.txt, which contains the information as per the assesment spec.
    """

    if os.path.exists("output.txt"):
        os.remove("output.txt")

    with open("output.txt", "x", encoding="utf-8") as file:
        if is_encrypt:
            file.write(
                "Avalanche Demonstration\n"
                f"Plaintext P   : {p[0]}\n"
                f"Plaintext P'  : {p[1]}\n"
                f"Key K         : {k[0]}\n"
                f"Key K'        : {k[1]}\n"
                f"Total running time: {running_time:.3f} seconds\n\n"
                f"P and P` under K\n"
                f"Ciphertext C : {c[0][0]}\n"
                f"Ciphertext C`: {c[0][1]}\n\n"
                f"Round\t\t\tDES0\tDES1\tDES2\tDES3\n"
            )
            for i in range(17):
                file.write(
                    f"\t{i}\t\t\t {avalanche[0][0][i]}\t\t {avalanche[1][0][i]}\t\t {avalanche[2][0][i]}\t\t {avalanche[3][0][i]}\n"
                )
            file.write(
                f"\nP under K and K`\n"
                f"Ciphertext C : {c[0][0]}\n"
                f"Ciphertext C`: {c[0][2]}\n\n"
                f"Round\t\t\tDES0\tDES1\tDES2\tDES3\n"
            )
            for i in range(17):
                file.write(
                    f"\t{i}\t\t\t {avalanche[0][1][i]}\t\t {avalanche[1][1][i]}\t\t {avalanche[2][1][i]}\t\t {avalanche[3][1][i]}\n"
                )
        else:
            print("DO HERE")
        file.close()


def avalanche_comparison(p1: str, p2: str) -> int:
    """
    This method compares the original plaintext string with the
        cipherext string produced after each round.

    It converts the strings into lists, then loops through the length of the original plaintext.
    While looping to checks whether the current value in the plaintext and ciphertext does
        not match.
    If it doesn't then it adds one to the counter, otherwise it just continues.
    """
    counter = 0
    p1_list = list(p1)
    p2_list = list(p2)
    for i in range(64):
        if p1_list[i] != p2_list[i]:
            counter += 1
    return counter


if __name__ == "__main__":
    main()
