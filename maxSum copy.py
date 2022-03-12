import math
f = open("pyramid.txt", "r")
arr = []   #to store the input
for line in f:
    line_strip = line.strip()
    row_list = list(map(int, line_strip.split()))
    arr.append(row_list)

n = len(arr)
"""
    modified_array
      [0]
      [0,0]
      [0,0,0]
      ...
"""
# modified_arr[i][j] represents the max sum fromm (i, j) to the bottom level to the up
modified_arr = [[0] * (i+1) for i in range(n)]
"""
    modified_array
      [0]
      [0,0]
      [2,6,9] <-  filling the last row so that we can continue with bottom-up approach from pre last row of the 2D array
 """
for i in range(n):
    modified_arr[n-1][i] = arr[n-1][i]


def isPrime(n):
    fx = math.floor(math.sqrt(n))
    if(n == 1):
        return False
    else:
        for i in range(2, fx + 1):
            if (n % i == 0):
                return False
        return True


def maxSum(arr):
    for row in range(n - 2, -1, -1):
        for col in range(row + 1):
            if(isPrime( arr[row][col]) == False):
                if(modified_arr[row+1][col] > modified_arr[row+1][col+1]):
                    if(isPrime(arr[row+1][col]) == False):
                        modified_arr[row][col] = modified_arr[row + 1][col] + arr[row][col]
                    else:
                        if(isPrime(arr[row+1][col+1]) == False):
                            modified_arr[row][col] = modified_arr[row + 1][col+1] + arr[row][col]
                else:
                    if (isPrime(arr[row + 1][col+1]) == False):
                        modified_arr[row][col] = modified_arr[row + 1][col+1] + arr[row][col]
                    else:
                        if (isPrime(arr[row + 1][col + 1]) == False):
                            modified_arr[row][col] = modified_arr[row + 1][col + 1] + arr[row][col]


    return modified_arr[0][0]   #starting from bottom and going up by choosing the max choice which is not the prime number. Thus, gives us the max sum at the end at the top.


print(maxSum(arr))

#print(arr);
#print(modified_arr)


