import re 

str = 'we need 1 to 20-10-2020 be more 23 self aware of we 45 what we eat 30-03-2020'

result = re.search(r'w\w\w',str)
print(result.group())

result = re.findall(r'w\w\w',str)
print(result)

result = re.match(r'w\w\w',str)
print(result)

result = re.sub(r'more','less',str)
print(result)

result = re.findall(r'w\w{1,2}',str)
print(result)

result = re.split(r'\d+',str)
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)



