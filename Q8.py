# 8. January 1st 2024 is Monday. Write a program that input month and date and prints out what day it is.[2 points]
# * 1 <= Month <= 12         1<= Day <= 31 
# * There are 31 days in January, March, May, July, August, October, and December, 30 days in April, June, 
#   September, and November, and 29 days in February, in 2024. 
# * The output should be like this: MON, TUE, WED, THU, FRI, SAT, SUN 


# Input: number
# Output: string
from datetime import date as date2

def func(month, date):
  result = ''
    ####### add your code below #######  
  weeks = {1:'MON',2:'TUE',3:'WED',4:'THU',5:'FRI',6:'SAT',7:'SUN'}
  w = date2.isoweekday(date2(2024, month, date))
  result=(weeks[w])
      
    ####### add your code above #######
  return result

# test case 1
# Input: 1, 1
# Output: MON
print(func(1,1))

# test case 2
# Input: 2, 27
# Output: TUE

print(func(2, 27))

