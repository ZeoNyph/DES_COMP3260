# COMP3260 Assessment 2

## Description
This is the repo for COMP3260 A2, implementation of DES encryption with avalanche effect and decryption. 

## How to Run
1. Prepare your input files. These can vary between encryption and decryption and the program can only do one at a time.
   
     - Encryption:
       ```
       plaintext
       bit-flipped plaintext
       key
       bit-flipped key
       ```
    - Decryption:
      ```
      ciphertext
      key
      ```
2. Run the program using the following command, making sure you are in the same directory as main.py:
     ```sh
     $ python main.py [OPTION] /path/to/input
     ```
     where [OPTION] can be `-e` for encryption and `-d` for decryption.
3. View the output in `./output.txt`.

## Authors
- Mithun Sivanesan
- Chanelle Velovski

## Start date 
- 22/04/2025

## End date
- 29/05/2025
