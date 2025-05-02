import random
import copy
#This includs the DES function expansion permutation E and Inverse Expansion Permutation E^-1

IP_Table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

def initial_permutation(input):
    inputList = []
    # inputList = [[None for i in range (8)] for j in range(8)]
    # evenList = [[None for i in range (8)] for j in range(4)]
    # oddList = copy.deepcopy(evenList)
    # for i in range (64):
    #     inputList[i//8][i%8] = int(input[i])
    # for i in range (8):
    #     for j in range (8):
    #         bit = inputList[i][j]
    # return inputList
    print(input)
    for i in range(len(IP_Table)):
        value = IP_Table[i] - 1
        indexVal = input[value]
        inputList.append(indexVal)

    print(inputList)
        

        

if __name__ == "__main__":
    input = [random.choice('01') for _ in range(64)]  # Generate a 64-bit random binary array
    #print(input + "\n")
    out = initial_permutation(input)
   # for i in range (8):
    #    for j in range (8):
     #       print(out[i][j], end = '')