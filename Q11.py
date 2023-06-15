# 11. There is a game where you throw 3 die and get cash prize based on the following rules: 
# - If you get the same number for all 3 die, you get cash prize of $100+(that number)*$10. 
# - If you get the same number for 2 die, you get cash prize of $10+(that number)*$1. 
# - If you get different numbers for all 3 die, you get cash prize of (largest number you got)*$1. 
# For example, if you get 3, 3, 6 for 3 die, your cash prize will be 10 + 3*1 = $13. If you get 2, 2, 2, for 3 die, your cash prize will be 100 + 2*10 = $120. 
# If you get 6, 2, 5 for 3 die, your cash prize will be 6*1 = $6. 
# Write a program that input 3 integers and outputs the cash prize. [2 points]

# Input: list with positive integer
# Output: positive integer

def func(dies):
  result=0
  ####### add your code below #######
  
  if dies[0]==dies[1] and dies[1]==dies[2]:
    prize=100+dies[0]*10
    result=prize

  elif dies[0]==dies[1] or dies[0]==dies[2] or dies[1]==dies[2]:
      for i in dies:
        for j in dies:
          if i==j:
            
            prize=10+i*10
            result=prize
  else:
    largest=dies[0]
    for die in dies:
      if die>largest:
        largest=die
    prize=largest*1
    result=prize
  ####### add your code above #######
  return result  

# test case 1
# Input: 3,3,3
# Output: 130
print(func([3,3,3]))

# test case 2
# Input: 1,3,5
# Output: 5
print(func([1,3,5]))

print(func([5,4,5]))

print(func([3,4,2]))
