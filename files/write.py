#to write a file
f = open('myfile.txt','w')
s = input('enter text: ')
f.write(s)
f.close()