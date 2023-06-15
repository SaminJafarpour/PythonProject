
# 3. Write a program to calculate the perimeter of the triangle, 
# based on the three points given by user. [2 points]

# Input: tuple
# Output: number
import math
def func(a,b,c):
    result = 0
    ####### add your code below #######
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    x3 = c[0]
    y3 = c[1]

    line1=math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    line2=math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    line3=math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    
    result=line1+line2+line3


    ####### add your code above #######
    return result

# test case 1
# Input: (5, 1), (5, 4), (1, 1)
# Output: 12
print(func((5, 1), (5, 4), (1, 1)))

# test case 2
# Input: (0, 0), (3, 0), (0, 4)
# Output: 12
print(func((0, 0), (3, 0), (0, 4)))
