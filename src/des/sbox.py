"""
Substitution Box (S-Boxes) module for the DES package.

Authors:
Chanelle Velovski (c3431376)
Mithun Sivanesan (c3403606)
"""

S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
]

S2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
]

S3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
]

S4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
]

S5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
]

S6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
]

S7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
]

S8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]


def string_to_int(binary_value: str) -> int:
    """
    This function converts the binary value to decimal value
    """
    integer_value = int(binary_value, 2)
    return integer_value


def padding(value: str) -> str:
    """
    This function ensures the output bit length is 4
    """
    while len(value) < 4:
        value = "0" + value
    return value


def sbox_function(xor_output: str) -> str:
    """
    1. This function takes the input and splits it into 8 parts each including 6 bits.
    2. Each 6 bits have the first and last bits stored in a new variable, 
            and then the middle 4 bits are stored in a separate variable
    3. The stored 2 bit and 4 bit values are converted into their integer values.
    4. Both of the integer values are used to retreive the value at that 
            index in the corresponding s-box
    5. The index value is then converted back into its binary value.
    6. Goes through a padding checker to ensure the binary value is 4 bits long.
    7. Once points 2-6 are completed for all the 8 inputs we then add all the 
            bits together to make a 32 bit string output.
    """
    input1 = xor_output[0:6]
    input2 = xor_output[6:12]
    input3 = xor_output[12:18]
    input4 = xor_output[18:24]
    input5 = xor_output[24:30]
    input6 = xor_output[30:36]
    input7 = xor_output[36:42]
    input8 = xor_output[42:48]

    beginning = input1[0]
    end = input1[5]
    input1a = beginning + end  # taken the first and last bit and added them together
    input1b = input1[1:5]  # stored the middle four bits
    integer_input1a = string_to_int(input1a)
    integer_input1b = string_to_int(input1b)
    sbox_value1 = S1[integer_input1a][integer_input1b] # searched through s-box 1
    input1_binary = format(sbox_value1, "b")
    s1_bit = padding(input1_binary) 

    beginning = input2[0]
    end = input2[5]
    input2a = beginning + end
    input2b = input2[1:5]
    integer_input2a = string_to_int(input2a)
    integer_input2b = string_to_int(input2b)
    sbox_value2 = S2[integer_input2a][integer_input2b]# searched through s-box 2
    input2_binary = format(sbox_value2, "b")
    s2_bit = padding(input2_binary)

    beginning = input3[0]
    end = input3[5]
    input3a = beginning + end
    input3b = input3[1:5]
    integer_input3a = string_to_int(input3a)
    integer_input3b = string_to_int(input3b)
    sbox_value3 = S3[integer_input3a][integer_input3b] # searched through s-box 3
    input3_binary = format(sbox_value3, "b")
    s3_bit = padding(input3_binary)

    beginning = input4[0]
    end = input4[5]
    input4a = beginning + end
    input4b = input4[1:5]
    integer_input4a = string_to_int(input4a)
    integer_input4b = string_to_int(input4b)
    sbox_value4 = S4[integer_input4a][integer_input4b] # searched through s-box 4
    input4_binary = format(sbox_value4, "b")
    s4_bit = padding(input4_binary)

    beginning = input5[0]
    end = input5[5]
    input5a = beginning + end
    input5b = input5[1:5]
    integer_input5a = string_to_int(input5a)
    integer_input5b = string_to_int(input5b)
    sbox_value5 = S5[integer_input5a][integer_input5b] # searched through s-box 5
    input5_binary = format(sbox_value5, "b")
    s5_bit = padding(input5_binary)

    beginning = input6[0]
    end = input6[5]
    input6a = beginning + end
    input6b = input6[1:5]
    integer_input6a = string_to_int(input6a)
    integer_input6b = string_to_int(input6b)
    sbox_value6 = S6[integer_input6a][integer_input6b] # searched through s-box 6
    input6_binary = format(sbox_value6, "b")
    s6_bit = padding(input6_binary)

    beginning = input7[0]
    end = input7[5]
    input7a = beginning + end
    input7b = input7[1:5]
    integer_input7a = string_to_int(input7a)
    integer_input7b = string_to_int(input7b)
    sbox_value7 = S7[integer_input7a][integer_input7b] # searched through s-box 7
    input7_binary = format(sbox_value7, "b")
    s7_bit = padding(input7_binary)

    beginning = input8[0]
    end = input8[5]
    input8a = beginning + end
    input8b = input8[1:5]
    integer_input8a = string_to_int(input8a)
    integer_input8b = string_to_int(input8b)
    sbox_value8 = S8[integer_input8a][integer_input8b] # searched through s-box 8
    input8_binary = format(sbox_value8, "b")
    s8_bit = padding(input8_binary)

    output_bit = s1_bit + s2_bit + s3_bit + s4_bit + s5_bit + s6_bit + s7_bit + s8_bit
    return output_bit
