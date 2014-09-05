import wave
import struct
import math
import array

convert_to_morse = [ '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
                      '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
                      '..-', '...-', '.--', '-..-', '-.--', '--..' ]

def writeSound(values, ticks):
  
  for i in range(ticks * 500):
    values.append(struct.pack('<h', 5 * int(math.sin(i/1000))))
  return values
  
  
def writeSilence(values, ticks):
  for i in range(ticks * 500):
    values.append(48)
  return values


input = input("Enter message:" )

converted_input = ""

for char in input:
  if char == ' ':
    converted_input += '/ '
  else:
    index = ord(char.upper()) - 65
    converted_input += convert_to_morse[index] + " "

print(converted_input)

output = wave.open('output.wav', 'w')
output.setparams((2, 2, 5000, 0, 'NONE', 'not compressed'))

values = []


for char in converted_input:
  
  if char == ' ':
    values = writeSilence(values, 2)
  elif char == '.':
    values = writeSound(values, 1)
    values = writeSilence(values, 1)
  elif char == '-':
    values = writeSound(values, 3)
    values = writeSilence(values, 1)
  else:
    values = writeSilence(values, 2)

s = "".join(str(v) for v in values)
output.writeframesraw(bytes(s, 'utf-8'))

output.close()