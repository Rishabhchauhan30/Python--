f = open('myfile.txt','w')
print('enter text(type $ when you are done)')
s = ' '
while s!='$':
    s=input()
    f.write(s+'\n')
    
f.close()