


# 6. Tim wakes up with an alarm every morning. But he does not always wake up right after 
# he hears his alarm going off and he sometimes is late for work. He decided to 
# set his alarm 35 minutes before the time he needs to wake up. Write a program that 
# outputs the time for Tim to set the alarm according to the input time he needs to wake up. [4 points] 

# * 24-hour system, likes 23:35, 00:01, the output should have 2 digits for hour and 2 digits for minute
# * 0 <= Hour <= 23          0 <= Minute <= 59


# Input: string
# Output: string
from datetime import datetime, timedelta
def func(t):
    result=''
    ####### add your code below #######
    date_str = t
    date_format = '%H:%M'

    date_obj = datetime.strptime(date_str, date_format)
    result=(date_obj)
    minus_35 = date_obj - timedelta(minutes = 35)
    str_minus_35=str(minus_35)
    result=str_minus_35[11:16]

    
    ####### add your code above #######
    return result

# test case 1
# Input: 23:35
# Output: 23:00
print(func('23:35'))

# test case 2
# Input: 09:40
# Output: 09:05
print(func('09:40'))
#print(func('12:05'))

print(func('08:30'))
