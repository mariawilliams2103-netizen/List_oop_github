students = ["Maria" ,"Praise", "Ameynor"]
print(students)
# Accessing items in list by their index
print(f"My best friend is {students[0]}")
print(f"My best friend is {students[1]}")
print(f"My best friend is {students[2]}")


# Get the index of an item in a list
print(students.index("Maria"))
print(students.index("Praise"))
print(students.index("Ameynor"))

# Know the number of items in a list
print(f"The total items in the list is: {len(students)}")

# Add items to a list
students.append("Brian")
print(students)
students += ["Benjamin", "Preston", "Gladys"]
print(students)

students.insert(4, "Leonard")
print(students)

# Extending a list
fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)
print(students)

# Removing an items from a list
fruits.remove("Mango")

students.pop()
students.pop()
thirdItem = students.pop()
print(students)
print(thirdItem)