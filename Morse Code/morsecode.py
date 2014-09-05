#!/usr/bin/env python3

import wave
import struct
import math

convert_to_morse = [ '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
                      '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
                      '..-', '...-', '.--', '-..-', '-.--', '--..' ]

def convert_to_morse_code(plaintext):
  """Converts a plaintext string into morse code.
  
  :param plaintext: a plaintext string to convert.
  :returns: a string containing morse code.
  """
  converted_input = ""

  for char in plaintext:
    if char == ' ':
      converted_input += '/ '
    else:
      index = ord(char.upper()) - 65
      converted_input += convert_to_morse[index] + " "

  return converted_input
  
def output_morse_code(morse_code):
  """Writes a .wav file that will play the morse code in audio.
  
  :param morse_code: morse code to write out to .wav.
  :returns: nothing
  """
  output = wave.open('output.wav', 'w')
  output.setparams((2, 2, 5000, 0, 'NONE', 'not compressed'))

  values = []


  for char in morse_code:
  
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
  
def writeSound(values, ticks):
  """Writes a tone a specific length for the amount of ticks entered.
  
  :param values: an array of value the tone will be written to.
  :param ticks: the number of times the tone will be written.
  :returns: an array of values the method added to.
  """
  for i in range(ticks * 500):
    values.append(struct.pack('<h', 5 * int(math.sin(i/1000))))
  return values
  
  
def writeSilence(values, ticks):
  """Writes silence a specific length for the amount of ticks entered.
  
  :param values: an array of value the silence will be written to.
  :param ticks: the number of times the silence will be written.
  :returns: an array of values the method added to.
  """
  for i in range(ticks * 500):
    values.append(48)
  return values


input = input("Enter message:" )

converted_input = convert_to_morse_code(input)

print(converted_input)

output_morse_code(converted_input)

