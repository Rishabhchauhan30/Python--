'''class student:
    def __init__(self):
        self.name='john'    #they are not hidden
        self.rollno=1234
        
s= student()
print(s.name)
print(s.rollno)'''
        
        
class student:
    def __init__(self):
        self.__id=123
        self.__name='John'
        
#now the things are private so to access them        
        
    '''def display(self):
        print(self.__id)
        print(self.__name)'''

s= student()
#s.display()     

print(s._student__id)  
print(s._student__name)          

#this is name mangling when the things are private you can access them by
# object._class name__field name