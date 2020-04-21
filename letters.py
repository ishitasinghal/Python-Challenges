# Source : "https://www.coderbyte.com/editor/Letter%20Changes:Python3"

# Problem Statement:
# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
# Examples
# Input: "hello*3"
# Output: Ifmmp*3
# Input: "fun times!"
# Output: gvO Ujnft!

# CODE

def LetterChanges(str):
  nstr = ""
  nnstr = ""
  for i in str:
    if(i.isalpha()):
      nstr = nstr+chr(ord(i) + 1) 
    else:
      nstr = nstr+i
    
  vowels = ['a', 'e', 'i', 'o', 'u']
  nnstr = ''.join([c.upper() if c in vowels else c for c in nstr])
    
  
  return nnstr

# keep this function call here 
print(LetterChanges(input()))
