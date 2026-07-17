# Python Day 3 - Lists and Shopping List Manager

## Overview

This repository contains my Day 3 Python practice focused on Python lists and an interactive command-line Shopping List Manager.

It includes exactly 20 numbered list exercises and a practical project that allows users to display, add, remove, and update shopping-list items through a repeating menu. The corrected project also demonstrates executable `insert()` and `pop()` operations and displays the current item count with `len()`.

## Topics Practiced

- Creating Python lists
- Starting with an empty list
- Positive and negative indexing
- List slicing
- Updating list items
- Adding items with `append()` and `insert()`
- Removing items with `remove()` and `pop()`
- Storing and printing the value returned by `pop()`
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

Contains exactly 20 practical exercises covering Python list fundamentals and list-processing techniques.

The exercises include:

1. Creating a list
2. Accessing the first item
3. Accessing the last item with negative indexing
4. Extracting items with slicing
5. Adding items to a list
6. Safely removing an item
7. Safely updating a list item
8. Finding the length of a list
9. Printing list items with a loop
10. Calculating a total manually
11. Finding the largest number manually
12. Finding the smallest number manually
13. Counting passing scores
14. Checking list membership
15. Practicing `append()`, `insert()`, `pop()`, `remove()`, and item updates
16. Displaying subjects with manual numbering
17. Printing even numbers
18. Printing odd numbers
19. Taking multiple values from the user
20. Checking whether a list is empty

Exercise 15 contains executable `insert()` and `pop()` demonstrations:

```python
shopping_items.insert(1, "butter")
print("After insert:", shopping_items)

popped_item = shopping_items.pop()
print("Popped item:", popped_item)
```

The list state after `insert()` is printed. The value returned by `pop()` is stored in `popped_item` and printed.

### `shopping_list_manager.py`

Contains an interactive command-line Shopping List Manager.

The program allows the user to:

1. Display the current shopping list and total item count
2. Add a new item
3. Remove an existing item
4. Update an item using its displayed number
5. Exit the program

## Empty Initialization and Five-Item Setup

The project initially creates an empty list:

```python
shopping_list = []
```

It then adds five sample items using list operations:

```python
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")
shopping_list.append("Rice")
shopping_list.append("Tea")
```

The setup visibly confirms both states:

```text
Shopping list starts empty.
Total items: 0
Five sample items were added using append().
Total items: 5
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

### 1. Show Shopping List

Displays all current shopping-list items with manual numbering and displays the current total using `len()`.

Example:

```text
Current Shopping List:
1 Milk
2 Bread
3 Eggs
4 Rice
5 Tea
Total items: 5
```

If the list is empty, the program displays:

```text
Shopping list is empty.
Total items: 0
```

### 2. Add an Item

The user can enter a new item, which is added to the list using `append()`.

Example:

```text
Enter the name of the new item: Butter
Butter has been added successfully.
Total items: 6
```

Blank values and inputs containing only spaces are rejected.

```text
Item name cannot be blank.
```

### 3. Remove an Item

The user can enter the name of an existing item to remove it from the list.

Removal is case-insensitive. For example, entering `milk` can remove `Milk`.

Example:

```text
Enter the item name to remove: milk
Milk has been removed successfully.
Total items: 4
```

If the item does not exist, the program displays:

```text
Sorry! Item does not exist in the shopping list.
```

If duplicate values exist, removal searches from the beginning and removes only the first case-insensitive matching occurrence. Any later duplicate remains in the list.

When the final remaining item is removed, the program displays:

```text
Total items: 0
```

### 4. Update an Item

The program first displays all items with numbers. The user selects an item number and enters a new value.

Example:

```text
Current Shopping List:
1 Milk
2 Bread
3 Eggs
4 Rice
5 Tea

Enter the item number you want to update: 2
Enter the new item name: Butter
Bread has been updated to Butter.
Total items: 5
```

The user-facing item number is converted into a Python list index:

```python
index = item_number - 1
```

This conversion is required because displayed numbering starts from `1`, while Python list indexes start from `0`.

Updating replaces an existing value and does not change the total count.

### 5. Exit the Program

The user can select option `5` to stop the program.

```text
Exiting Shopping List Manager.
Final total items: 5
```

## Input Validation

The Shopping List Manager safely handles:

- Blank item names
- Inputs containing only spaces
- Missing items during removal
- Invalid menu choices
- Text entered instead of an item number
- First and last valid item numbers
- Zero item numbers
- Negative item numbers
- Item numbers outside the available list range
- Blank values during an update
- Case differences during item removal
- Empty-list display, removal, and update attempts

## Error Handling

The program uses `try/except ValueError` when converting an item number into an integer.

```python
try:
    item_number = int(item_number_input)
except ValueError:
    print("Please enter a valid numeric item number.")
```

Without this error handling, entering text such as `abc` instead of a number would cause the program to crash.

## Program Flow

```text
Start the program

Create an empty shopping list
Display its count as 0
Add five sample items using append()
Display the count as 5

Repeat:
    Display the menu
    Ask the user to enter a choice

    If choice is 1:
        Display all shopping-list items
        Display the total item count

    If choice is 2:
        Ask for a new item
        Validate the input
        Add the item
        Display the new count

    If choice is 3:
        Ask for an item name
        Search for the first case-insensitive match
        Remove it if found
        Display the new count
        Otherwise, display an error

    If choice is 4:
        Display numbered items
        Ask for an item number
        Validate and convert the number
        Ask for a new item value
        Update the selected item
        Display the unchanged count

    If choice is 5:
        Display the final count
        Exit the program

    Otherwise:
        Display an invalid-choice message
```

## How to Run

Make sure Python is installed on the system.

Open a terminal inside the repository folder.

### Run the List Exercises

Exercise 19 asks for three item inputs.

```bash
python day3_lists_basics.py
```

### Run the Shopping List Manager

```bash
python shopping_list_manager.py
```

### Check Python Syntax

```bash
python -m py_compile day3_lists_basics.py shopping_list_manager.py
```

## Tests Completed

The corrected project was executed and verified for:

1. Python syntax compilation
2. Executable `insert()` behavior
3. Executable `pop()` behavior
4. Printed value returned by `pop()`
5. Exactly 20 numbered exercises
6. Empty initial shopping list
7. Five sample items added using list operations
8. Initial total count
9. Count after adding an item
10. Unchanged count after updating an item
11. Count after removing an item
12. Count when the list becomes empty
13. First valid item number
14. Last valid item number
15. Item number `0`
16. Negative item number
17. Non-numeric item number
18. Out-of-range item number
19. Existing-item removal
20. Missing-item removal
21. Duplicate-item behavior
22. Blank add input
23. Blank update input
24. Complete integrated add-update-remove workflow
25. Regression of previously working display, case-insensitive removal, invalid-menu, and exit behavior

## Learning Outcomes

After completing Day 3, I can:

- Create and modify Python lists
- Start with an empty list and build it using list operations
- Access list items with positive and negative indexes
- Extract sections of a list with slicing
- Add items with `append()` and `insert()`
- Remove items with `remove()` and `pop()`
- Store and print the value returned by `pop()`
- Update list values safely
- Process list items with loops
- Number items without using `enumerate()`
- Display and verify list size using `len()`
- Check whether an item exists in a list
- Validate blank user input
- Convert strings into integers
- Convert user-facing numbering into Python indexes
- Handle invalid integer input with `try/except`
- Prevent invalid indexes from changing the list
- Build a repeating command-line menu
- Create a small interactive Python application

## Current Limitations

- The shopping list is stored only while the program is running.
- When the program restarts, it creates an empty list and adds the same five sample items again.
- Duplicate items are allowed.
- Removing an item by name removes only the first matching occurrence.
- File persistence, databases, APIs, classes, and external packages are outside the current Day 3 scope.
