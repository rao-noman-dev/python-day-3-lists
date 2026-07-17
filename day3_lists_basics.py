# Day 3 - Python Lists
# Exercises 1-20


# Exercise 1 - Create and Print Five Student Names
students = ["Ali", "Raza", "Ahmad", "Atif", "Arif"]

print(students)


# Exercise 2 - Print the First Student
print(students[0])


# Exercise 3 - Print the Last Student Using Negative Indexing
print(students[-1])


# Exercise 4 - Print the First Three Students Using Slicing
print(students[0:3])


# Exercise 5 - Create an Empty Cities List and Add Items
cities = []

cities.append("Lahore")
cities.append("Karachi")
cities.append("Islamabad")

print(cities)


# Exercise 6 - Remove One City Safely
if "Karachi" in cities:
    cities.remove("Karachi")
else:
    print("City not found.")

print(cities)


# Exercise 7 - Update the Second City Safely
if len(cities) > 1:
    cities[1] = "Peshawar"
else:
    print("The second city cannot be updated.")

print(cities)


# Exercise 8 - Count the Total Number of Cities
print("Total cities:", len(cities))


# Exercise 9 - Print Every City Using a Loop
for city in cities:
    print(city)


# Exercise 10 - Calculate the Total Manually
numbers = [10, 20, 30, 40]
total = 0

for number in numbers:
    total += number

print("Manual total:", total)


# Exercise 11 - Find the Largest Number Manually
numbers_for_comparison = [12, 45, 7, 89, 34]
largest_number = numbers_for_comparison[0]

for number in numbers_for_comparison:
    if number > largest_number:
        largest_number = number

print("Largest number:", largest_number)


# Exercise 12 - Find the Smallest Number Manually
smallest_number = numbers_for_comparison[0]

for number in numbers_for_comparison:
    if number < smallest_number:
        smallest_number = number

print("Smallest number:", smallest_number)


# Exercise 13 - Count Passing Marks
marks = [40, 55, 80, 49, 50, 90]
passing_count = 0

for mark in marks:
    if mark >= 50:
        passing_count += 1

print("Passing students:", passing_count)


# Exercise 14 - Check Whether Ali Is in the List
names = ["Sara", "Ali", "Noman"]

if "Ali" in names:
    print("Ali was found.")
else:
    print("Ali was not found.")


# Exercise 15 - Add, Remove, and Update Shopping Items
shopping_items = ["milk", "bread", "eggs"]

shopping_items.append("tea")

if "bread" in shopping_items:
    shopping_items.remove("bread")
else:
    print("Bread was not found.")

if len(shopping_items) > 1:
    shopping_items[1] = "rice"
else:
    print("The second item cannot be updated.")

print("Final shopping items:", shopping_items)


# Exercise 16 - Print Items with Numbering
subjects = ["Python", "SQL", "Git"]
item_number = 1

for subject in subjects:
    print(item_number, subject)
    item_number += 1


# Exercise 17 - Print Even Numbers
numbers_for_filtering = [1, 2, 3, 4, 5, 6, 7, 8]

for number in numbers_for_filtering:
    if number % 2 == 0:
        print(number)


# Exercise 18 - Print Odd Numbers
for number in numbers_for_filtering:
    if number % 2 != 0:
        print(number)


# Exercise 19 - Take Three Inputs and Append Them to a List
user_items = []

first_item = input("Enter your first item: ").strip()
user_items.append(first_item)

second_item = input("Enter your second item: ").strip()
user_items.append(second_item)

third_item = input("Enter your third item: ").strip()
user_items.append(third_item)

print("User items:", user_items)


# Exercise 20 - Check Whether a List Is Empty
empty_items = []

if not empty_items:
    print("The list is empty.")
else:
    print("The list contains items.")