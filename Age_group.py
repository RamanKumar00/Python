User_age = input("Enter the age of the person: ")

age_in_int = int(User_age)

if age_in_int < 13:
    print("you are a child")

elif age_in_int > 13 and age_in_int <20:
    print("you are a teenager")

elif age_in_int >20 and age_in_int < 60:
    print("you are a adult")

else:
    print("you are a senior")
