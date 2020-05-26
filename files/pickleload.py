import pickle

f=open('student.data','rb')
obj = pickle.load(f)
obj.display()