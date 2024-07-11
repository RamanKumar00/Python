name="python"
sl=name[0:6]   #accessing the word in the given string
print(sl)

sl=name[1:4]
print(sl)

word="amazing"
print(word[1:6:2]) #slicing with skip value

check="desktop"
print(check.endswith("top")) #its return true in the output

print(check.count("t")) #its counts same character

print(check.capitalize()) #its capitalize the first character of the string

print(check.find("o"))  #its find the character and returns its index

print(check.replace("o", "e"))  #its replace the old character with new one

print(check.lower())        #its convert all characters in to lower case

print(check.upper())         #its convert all characters in to upper case

print(check.replace("desktop","monitor"))  #its replace the old word with the new word

print(len(check))       #length of the variable

print(len(check.center(50))) #length of the variable after check()

print(check.center(50,"."))


