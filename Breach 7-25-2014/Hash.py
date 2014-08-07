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
print(result[0:512])
words = [[] for y in range(80)]

#Break the binary up into 512 blocks.
for i in range(0, multiples):

    #Break each block up into sixteen 32-bit words.
    for j in range(0, 16):
        words[j] = result[i*512 + j*32:(i*512 + j*32) + 32]
        print(words[j])

    for j in range(16,80):
        words[j-3]
        words[j-8]
        words[j-14]
        words[j-16]

print(len(result))



