#Returns an array of a binary converted from a string.
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


#Return original message padded up to the next multiple of 512.
def pad(result, messageLength):

    multiple = int(binaryLength/512)

    #Add a 1 to the end.
    if len(result) < (512 * multiple + 448):
        result.extend([1])

    #Add 0's up to the size of the original message in bits under the next multiple of 512.
    result.extend([0 for i in range(len(result), 512 * (multiple + 1) - len(messageLength))])
          
    result.extend([int(bit) for bit in messageLength])

    return result

def functionOne():

    for i in range(0,32): F.append((B[i] & C[i]) | (~B[i] & D[i]))
    K = [0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,10,1,1,1,0,1,0,0,0,0,1]


h0 = [0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1]
h1 = [1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1]
h2 = [1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0]
h3 = [0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0]
h4 = [1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0]
A = []
B = []
C = []
D = []
F = []
K = []
print(h0)

plaintext = "A Test";

#Convert the plaintext into binary.
result = convertToBin(plaintext)

#Get the length of the message converted to binary.
binaryLength = len(result)

#If the length is not a multiple of 512 then pad the message.
if binaryLength % 512 != 0:
    result = pad(result, bin(binaryLength)[2:])

multiples = int(len(result) / 512)

print(multiples)
words = [[] for y in range(16)]

#Break the binary up into 512 blocks.
for chunkIndex in range(0, multiples):

    #Break each block up into sixteen 32-bit words.
    for j in range(0, 16):
        words[j] = result[chunkIndex*512 + j*32:(chunkIndex*512 + j*32) + 32]

    for x in range(16,80):

        xorResult = []

        #XOR the x-3 word with the x-8 word. 
        for i in range(0,32): xorResult.append(words[x-3][i] ^ words[x-8][i])
    
        #XOR the resulting word with the x-14 word.
        for i in range(0,32): xorResult[i] = xorResult[i] ^ words[x-14][i]

        #XOR the resulting word with the x-16 word.
        for i in range(0,32): xorResult[i] = xorResult[i] ^ words[x-16][i]

        #Rotate left
        xorResult = xorResult[1:]
        xorResult.append(0)

        #Add new work to the end of the list of words.
        words.append(xorResult)

    A = h0
    B = h1
    C = h2
    D = h3
    E = h4

    for x in range(0,80):
        if(x < 20):
            functionOne()
        elif(x < 39):
            functionTwo()
        elif(x < 59):
            functionThree()
        else:
            functionFour()

        for r in range(0, 5)   
            A = A[1:]
            A.append(0)

    
        
            
    print(len(words))    

print(len(result))



