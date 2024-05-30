# tuple is simary is list but is unmutable we can not change tuple element

name=("naseem",45,356,33)
print(name)
print(type(name))
print(name[2])

# sliceing use in tuple
print(name[1:2])
#when we find the index of value index of 45 
print(name.index(45))


# tuple ko hum coma ke sath use karte h

tup=(1,)   # if we print without coma so type will chane int thats why need to use coman in signle tuple
print(tup)
print(type(tup))

# how much time number come it will count
number=(3,4,5,6,6,6,7,8,9,99)
print(number.count(6))


