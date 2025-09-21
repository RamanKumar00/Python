# list ia also know as array in python 
myList = [1, 3, "raman", 9]
print(myList)

# We can perform all the same method like as string

print(myList[0] )

myList[0] = "Virat"

print(myList[0] )

tea_varities = ["lemon","oolong","black","red"]
print(tea_varities)

print(tea_varities[0])

tea_varities[3] = "Milk Tea"
print(tea_varities)

tea_varities[1:3] = ["Masala", "green"]
print(tea_varities)

for tea in tea_varities:
    print(tea, end="-")
