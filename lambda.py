#Lambda is a single expression anonymous function often used as an inline function. 
#it is a function that has only one line in its body. 

#A list on a single line containing the cubes of the first N fibonacci numbers.
cube = lambda x: pow(x,3)
def fibonacci(n):
     res = [0,1]
     for i in range(2,n):
         res.append(res[i-2] + res[i-1])
     return(res[0:n])
  
#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

#cube = lambda x: pow(x,3)
# def fibonacci(n):
#      res = [0,1]
#      for i in range(2,n):
#          res.append(res[i-2] + res[i-1])
#      return(res[0:n])
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))

