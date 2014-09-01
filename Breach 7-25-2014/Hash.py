#!/usr/bin/env python3

# SHA-1 H0-H4 variables. These are part of the SHA-1 algorithm's 
H0 = [0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1]
H1 = [1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1]
H2 = [1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0]
H3 = [0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0]
H4 = [1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0]

def convert_to_bin(plaintext):
    """Converts a string to binary and returns the result in an array.

    :param plaintext: a plaintext string
    :returns: an array of int representing a bit string.
    """

    bit_array = []

    # Converts the string to binary, pads it to an 8 bit string, and converts to an array.
    for char in plaintext:
        bit_string = bin(ord(char))[2:]
        bit_string = '00000000'[len(bit_string):] + bit_string
        bit_array.extend([int(bit) for bit in bit_string])

    return bit_array


#Pads array of bits up to a multiple of 512.
def pad(result, messageLength):

    #Determine how many times 512 fits into the length of the bit array.
    multiples = int(binaryLength / 512)

    #Add one to the end.
    result.extend([1])

    while len(result) % 512 != 448: result.extend([0])

    while (len(result) + len(messageLength)) % 512 != 0: result.extend([0])

    #Add the length of the message in bits to the end of the array.      
    result.extend([int(bit) for bit in messageLength])

    return result


A = []
B = []
C = []
D = []
E = []
K = []

plaintext = "test"

#Convert the plaintext into binary
result = convert_to_bin(plaintext)

#Get the length of the message converted to binary.
binaryLength = len(result)

#Pad the result up to a multiple of 512 while adding the length of the string to the end.
result = pad(result, bin(binaryLength)[2:])

#Determine how many times 512 goes into the result. The result will be broken into chunks of 512.
multiples = int(len(result) / 512)    

#Break the binary up into 512 blocks.
for chunkIndex in range(0, multiples):

    words = [[] for y in range(16)]

    #Break each block up into sixteen 32-bit words.
    for x in range(0, 16):
        words[x] = result[chunkIndex*512 + x*32:(chunkIndex*512 + x*32) + 32]

    for x in range(16,80):

        xorResult = []

        #XOR the x-3 word with the x-8 word. 
        for i in range(0,32): xorResult.append(words[x-3][i] ^ words[x-8][i])
    
        #XOR the resulting word with the x-14 word.
        for i in range(0,32): xorResult[i] = xorResult[i] ^ words[x-14][i]

        #XOR the resulting word with the x-16 word.
        for i in range(0,32): xorResult[i] = xorResult[i] ^ words[x-16][i]

        #Rotate left
        overflow = xorResult[0]
        xorResult = xorResult[1:]
        xorResult.append(overflow)

        #Add new work to the end of the list of words.
        words.append(xorResult)

    A = H0
    B = H1
    C = H2
    D = H3
    E = H4

    for x in range(0,80):

        F = []
        
        if x < 20:
            for i in range(0,32): F.append((B[i] & C[i]) | (~B[i] & D[i]))
            K = [0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1]
        elif x < 40:
            for i in range(0,32): F.append(B[i] ^ C[i] ^ D[i])
            K = [0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,0,1]
        elif x < 60:
            for i in range(0,32): F.append((B[i] & C[i]) | (B[i] & D[i]) | (C[i] & D[i]))
            K = [1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0]
        else:
            for i in range(0,32): F.append(B[i] ^ C[i] ^ D[i])
            K = [1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0]

        rotA = A
        temp = []

        for r in range(0, 5):
            overflow = rotA[0]
            rotA = rotA[1:]
            rotA.append(overflow)

        tempString = str(bin(int(''.join(str(i) for i in rotA),2) + int(''.join(str(i) for i in F),2) + int(''.join(str(i) for i in E),2) + int(''.join(str(i) for i in K),2) + int(''.join(str(i) for i in words[x]),2))[2:])
        temp.extend([int(bit) for bit in tempString])

        diff = len(temp) - 32
        if diff > 0: temp = temp[diff:]

        rotB = B

        for r in range(0, 30):
            overflow = rotB[0]
            rotB = rotB[1:]
            rotB.append(overflow)

        E = D
        D = C
        C = rotB
        B = A
        A = temp
        
    H0String = str(bin(int(''.join(str(i) for i in H0),2) + int(''.join(str(i) for i in A),2))[2:])
    H1String = str(bin(int(''.join(str(i) for i in H1),2) + int(''.join(str(i) for i in B),2))[2:])
    H2String = str(bin(int(''.join(str(i) for i in H2),2) + int(''.join(str(i) for i in C),2))[2:])
    H3String = str(bin(int(''.join(str(i) for i in H3),2) + int(''.join(str(i) for i in D),2))[2:])
    H4String = str(bin(int(''.join(str(i) for i in H4),2) + int(''.join(str(i) for i in E),2))[2:])

    H0 = []
    H1 = []
    H2 = []
    H3 = []
    H4 = []
    
    H0.extend([int(bit) for bit in H0String])
    H1.extend([int(bit) for bit in H1String])
    H2.extend([int(bit) for bit in H2String])
    H3.extend([int(bit) for bit in H3String])
    H4.extend([int(bit) for bit in H4String])

    while len(H0) < 32: H0.insert(0,0)
    while len(H1) < 32: H1.insert(0,0)
    while len(H2) < 32: H2.insert(0,0)
    while len(H3) < 32: H3.insert(0,0)
    while len(H4) < 32: H4.insert(0,0)

    diff = len(H0) - 32
    if diff > 0: H0 = H0[diff:]
    diff = len(H1) - 32
    if diff > 0: H1 = H1[diff:]
    diff = len(H2) - 32
    if diff > 0: H2 = H2[diff:]
    diff = len(H3) - 32
    if diff > 0: H3 = H3[diff:]
    diff = len(H4) - 32
    if diff > 0: H4 = H4[diff:]

H0String = str(hex(int(''.join(str(i) for i in H0),2))[2:])
H1String = str(hex(int(''.join(str(i) for i in H1),2))[2:])
H2String = str(hex(int(''.join(str(i) for i in H2),2))[2:])
H3String = str(hex(int(''.join(str(i) for i in H3),2))[2:])
H4String = str(hex(int(''.join(str(i) for i in H4),2))[2:])

H0String = '00000000'[len(H0String):] + H0String
H1String = '00000000'[len(H1String):] + H1String
H2String = '00000000'[len(H2String):] + H2String
H3String = '00000000'[len(H3String):] + H3String
H4String = '00000000'[len(H4String):] + H4String

print(H0String + H1String + H2String + H3String + H4String)




