import random

#This includs the DES function expansion permutation E and Inverse Expansion Permutation E^-1

def expansion_permutation(input: str):
    inputList = [[None for i in range (8)] for j in range(8)]
    evenList = [[None for i in range (8)] for j in range(4)]
    oddList = evenList.deepcopy()
    for i in range (64):
        inputList[i//8][i%8] = int(input[i])
    for i in range (8):
        for j in range (8):
            bit = inputList[i][j]
    return inputList
        

if __name__ == "__main__":
    input = ''.join(random.choice('01') for _ in range(64))  # Generate a 64-bit random binary string
    print(input + "\n")
    out = expansion_permutation(input)
    for i in range (8):
        for j in range (8):
            print(out[i][j], end = '')