# Source: "https://www.coderbyte.com/editor/First%20Reverse:Python3"

# Problem Statement:

# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.
# Examples
# Input: "coderbyte"
# Output: etybredoc
# Input: "I Love Code"
# Output: edoC evoL I

# CODE

def FirstReverse(str):
  return str[::-1]

# keep this function call here 
print(FirstReverse(input()))
