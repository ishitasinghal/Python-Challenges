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
  nstr = ""
  res=0
  list1 = sen.split()
  for i in list1:
    for j in i:
      if(j.isalpha()):
        nstr = nstr+j
    res = max(res, len(nstr))
    print(res)
        

  return sen

# keep this function call here 
print(LongestWord(input()))
