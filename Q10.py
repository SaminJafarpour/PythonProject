# 10. Here is a list about the scores(integers) of each student. 
# Using the statistics module, write a program that outputs the percentage of 
# the number of students whose scores are higher than the average of the class. 
# (Output should be three decimal places and % at the end.) [4 points] 

# Input: list with positive integers
# Output: string

import statistics as stat
def func(scores):
    result = ''
    ####### add your code below #######
    mean= stat.mean(scores)
    j=0
    for i in scores:
        
        if i>mean:
            j+=1
    percentage= (j/len(scores))*100

    txt = "{:.3f}%"
    
    result=txt.format(percentage)
    

    ####### add your code above #######
    return result

# test case 1
# Input: 50, 50, 70, 80, 100
# Output: 40.000%
print(func([50, 50, 70, 80, 100]))

# test case 2
# Input: 100, 95, 90, 80, 70, 60, 50
# Output: 57.143%
print(func([100, 95, 90, 80, 70, 60, 50]))

print(func([2,2,2,4]))





