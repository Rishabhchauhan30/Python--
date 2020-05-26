import re 

str = 'we need 1 to be more 23 self aware of we 45 what we eat '

result = re.findall(r'w\w+',str)
print(result)

result = re.findall(r'w\w*',str)
print(result)

result = re.findall(r'w\w?',str)
print(result)

result = re.findall(r'w\w{2}',str)
print(result)

result = re.findall(r'w\w{1,2}',str)
print(result)
