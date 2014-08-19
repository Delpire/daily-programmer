#Converts a string to binary and returns the result in an array.
def convertToBin(string):

    result = []

    for char in string:
        #Converts the character into a bit.
        bits = bin(ord(char))[2:]
        #Adds zeros to make the number 8 bits long.
        bits = '00000000'[len(bits):] + bits
        #Adds the bits to the array.
        result.extend([int(bit) for bit in bits])

    return result


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

#SHA-1 h0-h4. These are part of the SHA-1 algorithm's 
h0 = [0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1]
h1 = [1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1]
h2 = [1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0]
h3 = [0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0]
h4 = [1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0]
A = []
B = []
C = []
D = []
E = []
K = []

plaintext = "test"

#Convert the plaintext into binary
result = convertToBin(plaintext)

#Get the length of the message converted to binary.
binaryLength = len(result)

print(binaryLength)

result = pad(result, bin(binaryLength)[2:])

multiples = int(len(result) / 512)    

print(len(result))

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

    A = h0
    B = h1
    C = h2
    D = h3
    E = h4

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
        
    h0String = str(bin(int(''.join(str(i) for i in h0),2) + int(''.join(str(i) for i in A),2))[2:])
    h1String = str(bin(int(''.join(str(i) for i in h1),2) + int(''.join(str(i) for i in B),2))[2:])
    h2String = str(bin(int(''.join(str(i) for i in h2),2) + int(''.join(str(i) for i in C),2))[2:])
    h3String = str(bin(int(''.join(str(i) for i in h3),2) + int(''.join(str(i) for i in D),2))[2:])
    h4String = str(bin(int(''.join(str(i) for i in h4),2) + int(''.join(str(i) for i in E),2))[2:])

    h0 = []
    h1 = []
    h2 = []
    h3 = []
    h4 = []
    
    h0.extend([int(bit) for bit in h0String])
    h1.extend([int(bit) for bit in h1String])
    h2.extend([int(bit) for bit in h2String])
    h3.extend([int(bit) for bit in h3String])
    h4.extend([int(bit) for bit in h4String])

    while len(h0) < 32: h0.insert(0,0)
    while len(h1) < 32: h1.insert(0,0)
    while len(h2) < 32: h2.insert(0,0)
    while len(h3) < 32: h3.insert(0,0)
    while len(h4) < 32: h4.insert(0,0)

    diff = len(h0) - 32
    if diff > 0: h0 = h0[diff:]
    diff = len(h1) - 32
    if diff > 0: h1 = h1[diff:]
    diff = len(h2) - 32
    if diff > 0: h2 = h2[diff:]
    diff = len(h3) - 32
    if diff > 0: h3 = h3[diff:]
    diff = len(h4) - 32
    if diff > 0: h4 = h4[diff:]

h0String = str(hex(int(''.join(str(i) for i in h0),2))[2:])
h1String = str(hex(int(''.join(str(i) for i in h1),2))[2:])
h2String = str(hex(int(''.join(str(i) for i in h2),2))[2:])
h3String = str(hex(int(''.join(str(i) for i in h3),2))[2:])
h4String = str(hex(int(''.join(str(i) for i in h4),2))[2:])

h0String = '00000000'[len(h0String):] + h0String
h1String = '00000000'[len(h1String):] + h1String
h2String = '00000000'[len(h2String):] + h2String
h3String = '00000000'[len(h3String):] + h3String
h4String = '00000000'[len(h4String):] + h4String

print(h0String + h1String + h2String + h3String + h4String)




