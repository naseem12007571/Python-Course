

# we make a list of student marks 
marks=[94.5,87.5,95.2,66.4,45.1]
print(marks)
print(type(marks))  # we can check type

print(marks[3]);  # we can do indexing
print(len(marks))  # we can show the length 


# example we can store the value of different data type or we can store different type of value

student=["Naseem",50,56.4,23, "moradabad"]
print(student)


# list is mutable we can change it 
name=["Naseem","choudhary"] # here is indexing we 0 index naseem and 1 index choudary
print(name[0])
name[0]= "virat"
print(name)   

# slicing use in list

studentMarks=[133,1233,222,333,444,5666,7788,444]
print(studentMarks)

print(studentMarks[1:4])   #slicing use 
print(studentMarks[-5:-2])   #slicing use negative index

# value fined which index it will return index we find 50 where is
number=[10,20,30,40,50,60,233]
print(number.index(50))


# list method just like short,append,reverse,insert
# make a list valuess

valuess=[23,11,10,2,6,122]
valuess.append(100)          # last mein value add kardega 200
valuess.sort()               # sort kardega
print(valuess)             

print(valuess.sort(reverse=True))  # it will sort decending order
print(valuess)

valuess.insert(3,11)    # insert value first we have to give index which index insert value and what value insert 

valuess.remove(1)    # 5 index value remove
valuess.pop(1)      # its alo remove





