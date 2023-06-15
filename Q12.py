# 12. Write a program that inputs one string and outputs the alphabet that’s 
# used the most in the word, when an English word (might be mixed with upper 
# and lower cases) is given. Your output alphabet should be in uppercase. 
# If there are more than one alphabet that are used the most in the word, output ? [4 points] 

# Input: string with alphabet
# Output: string

def func(s):
   result = ''
  ####### add your code below #######
  
   txt=s.lower()
   count=s.count(s[0])
   for j in txt:
      if txt.count(j)>count:
         count=txt.count(j)
         biggest=j
         result=biggest.upper()
   #most_frequent=( max(set(s), key = s.count))
   for i in txt:
      if txt.count(i)==count and not i ==biggest:
         result="?"
      
   
   
     
      

      
  ####### add your code above #######
   return result

# test case 1
# Input: Mississippi
# Output: ?
print(func('Mississippi'))

# test case 2
# Input: zZa
# Output: Z
print(func('zZa'))
print(func('sadfggggmilllln'))

print(func('lmahgag'))

print(func('lmahmmgag'))