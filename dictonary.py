
#  dictionary are used to data value in key:value pair 
#  they are unorderd mutable changeable dont allow duplicate keys

# we are making info name dictonary
info={
   "name" : "Naseem",
   "age"  :  23,
   "learning" : "coding",

}

print(info)


# we can use in tuple and list inside the dictionar

details={
    "name" : "naseem",
    "sublect": ["hinid","english","math","computer"],     # this list
    "topics" :  ("story","managemern","welldone"),
    "age" :455,
    12 : "nasem"  # key ko value bhi bana sakte h but list or dictionary nhi bana sakte key ko
}                 # tuple ko hum key bana sakte because in inmutable change nhi hota  
                  # duplicate key nhi ho sakti in dictionary age age do bar key nhi bana sakte 
print(details)

# all key value print
print(details.keys())
# print all vaues
print(details.values())


# how to access or print the value of dictionary

print(details["age"])
print(details["sublect"])
print(details[12])


# we can change the dictionary balue
details["name"]="choudhary"
print(details)

# we can add new value

details["username"]="naseemchoudhary18"





