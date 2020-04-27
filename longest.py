Source: "https://www.coderbyte.com/editor/Longest%20Word:Python3"

Problem Statement:
Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love

CODE

def LongestWord(sen):
  c = 0
  nstr = ""
  for i in sen:
    if(i.isalpha()==True):
      c = c+1
      nstr = nstr+i
  return sen

# keep this function call here 
print(LongestWord(input()))
