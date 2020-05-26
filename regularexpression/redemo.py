import re 
str = 'you are the the greatest'

result = re.search(r't\w\w',str)
print(result.group()) 

result = re.findall(r't\w\w',str)
print(result) 

result = re.match(r'y\w\w',str)
print(result.group())