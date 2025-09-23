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

tea_varities.append("Oolong") # it add in the last of the list 

if "Oolong" in tea_varities:
    print('I have Oolong Tea')

tea_varities.pop() # it remove the last string from the list
print(tea_varities)

tea_varities.remove("Masala") #it removes the specific tring from the list
print(tea_varities)

tea_varities.insert(1,"Red")
print(tea_varities)

tea_varities_copy = tea_varities.copy() #it copy two variable with same reference point 
tea_varities_copy.append("Lemon Tea")
print(tea_varities_copy)
print(tea_varities)

tea_varities_copy = tea_varities #it copy same thing in both variable
tea_varities_copy.append("Lemon Tea")
print(tea_varities)
