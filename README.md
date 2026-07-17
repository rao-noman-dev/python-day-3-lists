# Python Day 3 - Lists and Shopping List Manager

## Overview

This repository contains my Day 3 Python practice focused on Python lists and an interactive command-line Shopping List Manager.

It includes 20 list exercises and a practical project that allows users to display, add, remove, and update shopping-list items through a repeating menu.

## Topics Practiced

- Creating Python lists
- Positive and negative indexing
- List slicing
- Updating list items
- Adding items with `append()` and `insert()`
- Removing items with `remove()` and `pop()`
- Checking list membership
- Finding list length with `len()`
- Processing lists with `for` loops
- Manual item numbering
- Calculating totals manually
- Finding minimum and maximum values
- Counting values that meet a condition
- Printing even and odd numbers
- Cleaning user input with `strip()`
- Repeating a menu with `while True`
- Converting user-facing numbers into Python indexes
- Validating indexes and menu choices
- Handling invalid integer input with `try/except`

## Repository Files

### `day3_lists_basics.py`

Contains 20 practical exercises covering Python list fundamentals and list-processing techniques.

The exercises include:

1. Creating a list
2. Accessing the first item
3. Accessing the last item with negative indexing
4. Extracting items with slicing
5. Adding items to a list
6. Safely removing an item
7. Safely updating an item
8. Finding the length of a list
9. Processing items with a loop
10. Calculating a total manually
11. Finding the largest number
12. Finding the smallest number
13. Counting passing scores
14. Checking list membership
15. Adding, removing, and updating shopping items
16. Displaying items with manual numbering
17. Printing even numbers
18. Printing odd numbers
19. Taking multiple values from the user
20. Checking whether a list is empty

### `shopping_list_manager.py`

Contains an interactive command-line Shopping List Manager.

The program allows users to:

1. Display the current shopping list
2. Add a new item
3. Remove an existing item
4. Update an item using its displayed number
5. Exit the program

## Starting Shopping List

The program starts with:

```python
shopping_list = ["Milk", "Bread", "Eggs"]
```

## Program Menu

```text
--- Shopping List Manager ---
1. Show shopping list
2. Add item
3. Remove item
4. Update item
5. Exit
```

## Features

### Show Shopping List

Displays all items with manual numbering.

```text
Current Shopping List:
1 Milk
2 Bread
3 Eggs
```

If no items are available, the program displays:

```text
Shopping list is empty.
```

### Add an Item

The user can enter a new item, which is added using `append()`.

```text
Enter the name of the new item: Rice
Rice has been added successfully.
```

Blank values and inputs containing only spaces are rejected.

```text
Item name cannot be blank.
```

### Remove an Item

The user can remove an existing item by entering its name.

Removal is case-insensitive. For example, entering `milk` can remove `Milk`.

```text
Enter the item name to remove: milk
Milk has been removed successfully.
```

A missing item is handled safely:

```text
Sorry! Item does not exist in the shopping list.
```

### Update an Item

The program displays the current items with numbers. The user selects an item number and enters its new value.

```text
Current Shopping List:
1 Milk
2 Bread
3 Eggs

Enter the item number you want to update: 2
Enter the new item name: Butter
Bread has been updated to Butter.
```

The displayed item number is converted into a Python index:

```python
index = item_number - 1
```

This is required because displayed numbering starts from `1`, while Python list indexes start from `0`.

### Exit the Program

Selecting option `5` stops the program:

```text
Exiting Shopping List Manager.
```

## Input Validation

The program safely handles:

- Blank item names
- Inputs containing only spaces
- Missing items during removal
- Invalid menu choices
- Text entered instead of an item number
- Zero item numbers
- Negative item numbers
- Out-of-range item numbers
- Blank values during updates
- Case differences during item removal

## Error Handling

The program uses `try/except ValueError` while converting an item number into an integer.

```python
try:
    item_number = int(item_number_input)
except ValueError:
    print("Please enter a valid numeric item number.")
```

Without this handling, entering text such as `abc` instead of an integer would cause the program to crash.

## How to Run

Open a terminal inside the repository folder.

### Run the List Exercises

```bash
python day3_lists_basics.py
```

### Run the Shopping List Manager

```bash
python shopping_list_manager.py
```

### Check Python Syntax

```bash
python -m py_compile day3_lists_basics.py
python -m py_compile shopping_list_manager.py
```

## Tests Completed

The following behaviors were manually tested:

- Displaying the starting list
- Adding a valid item
- Rejecting a blank or spaces-only item
- Removing an existing item
- Case-insensitive item removal
- Handling a missing item
- Updating an item with a valid number
- Rejecting a blank update value
- Handling text instead of an item number
- Handling item number `0`
- Handling a negative item number
- Handling an out-of-range item number
- Handling an invalid menu choice
- Exiting the program safely

## Learning Outcomes

After completing Day 3, I can:

- Create and modify Python lists
- Access values with positive and negative indexes
- Extract list sections with slicing
- Add, remove, and update list items
- Process lists with loops
- Number items without using `enumerate()`
- Validate user input and list indexes
- Convert strings into integers
- Convert displayed numbering into Python indexes
- Handle `ValueError` with `try/except`
- Build a repeating command-line menu
- Create a small interactive Python application

## Current Limitation

The shopping list is stored only while the program is running.

After closing and restarting the program, the list resets to:

```python
["Milk", "Bread", "Eggs"]
```

Permanent storage using files or a database is outside the current Day 3 scope.
