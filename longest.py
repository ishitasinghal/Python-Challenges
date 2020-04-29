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
  nsen=""
  for i in sen:
    if(i.isalpha() or i.isnumeric() or i==' '):
      nsen = nsen+i
  list1 = nsen.split()
  n = max(list1,key = lambda x:len(x))
  return n

# keep this function call here 
print(LongestWord(input()))
