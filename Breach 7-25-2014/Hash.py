
def pad(result, mLength):

    multiple = int(size/512)

    print(len(result))

    #Add a 1 to the end.
    if len(result) < (512 * multiple + 448):
        result.extend([1])

    print(len(result))

    #Add 0's up to 448 over the multiple of 512.
    result.extend([0 for i in range(len(result), 512 * (multiple + 1) - len(mLength))])

    print(len(result))
    print(len(mLength))
          
    result.extend([int(bit) for bit in mLength])

    return result

plaintext = "Hicccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc";

result = []

messageLength = len(plaintext)

#Convert the plaintext into binary and store it in an array.
for char in plaintext:
    #Converts the character into a bit.
    bits = bin(ord(char))[2:]
    #Adds zeros to make the number 8 bits long.
    bits = '00000000'[len(bits):] + bits
    #Adds the bits to the array.
    result.extend([int(bit) for bit in bits])

#Get the size of the message converted to binary.
size = len(result)

#If the size is not a multiple of 512 then pad the message.
if size % 512 != 0:
    result = pad(result, bin(messageLength)[2:])

print(len(result))



