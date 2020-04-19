# Source: "coderbyte.com/editor/Find%20Intersection:Python3"


# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
# Examples
# Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
# Output: 1,4,13
# Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
# Output: 1,9,10

 

# CODE

def FindIntersection(strArr):
  li = []
  a1 = strArr[0].split(',')
  a2 = strArr[1].split(',')
  arr1 = [int(a) for a in a1]
  arr2 = [int(a) for a in a2]
  for i in arr1:
      if i in arr2:
          li.append(i)
  
  if(len(li)==0):
    print("false")
  else:
    nli = [str(a) for a in li]
    print("," . join(nli))


# keep this function call here 
FindIntersection(input())
