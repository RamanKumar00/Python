chai_types = {"Masala":"spicy","Ginger":"Zesty","Lemon":"Salty"}
print(chai_types)

print(chai_types.get("Ginger"))

chai_types["Milk Tea"] = 'Fresh'
print(chai_types)

for chai in chai_types:
    print(chai, chai_types[chai])

if "Masala" in chai_types:
    print("I have masala tea")

print(len(chai_types))

chai_types.pop("Ginger")
print(chai_types)

squared_num = {x:x**2 for x in  range(5)}
print(squared_num)