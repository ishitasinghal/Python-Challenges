# Source:  "https://www.coderbyte.com/editor/Binary%20Reversal:Python3"

# Problem Statement:
# Have the function BinaryReversal(str) take the str parameter being passed, which will be a positive integer, take its binary representation (padded to the nearest N * 8 bits), reverse that string of bits, and then finally return the new reversed string in decimal form. For example: if str is "47" then the binary version of this integer is 101111 but we pad it to be 00101111. Your program should reverse this binary string which then becomes: 11110100 and then finally return the decimal version of this string, which is 244.
# Examples
# Input: "213"
# Output: 171
# Input: "4567"
# Output: 60296

# CODE:
    
 def BinaryReversal(str):
  a= int(str)
  bin1 = bin(a)
  fin = format(bin1, '')
  return str

# keep this function call here 
print(BinaryReversal(input()))