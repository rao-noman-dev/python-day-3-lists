# Day 3 Project - Shopping List Manager

shopping_list = []

print("Shopping list starts empty.")
print("Total items:", len(shopping_list))

shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")
shopping_list.append("Rice")
shopping_list.append("Tea")

print("Five sample items were added using append().")
print("Total items:", len(shopping_list))

while True:
    print("\n--- Shopping List Manager ---")
    print("1. Show shopping list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Update item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    # Choice 1 - Show shopping list
    if choice == "1":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            print("\nCurrent Shopping List:")

            number = 1

            for item in shopping_list:
                print(number, item)
                number += 1

        print("Total items:", len(shopping_list))

    # Choice 2 - Add item
    elif choice == "2":
        new_item = input("Enter the name of the new item: ").strip()

        if new_item:
            shopping_list.append(new_item)
            print(new_item, "has been added successfully.")
            print("Total items:", len(shopping_list))
        else:
            print("Item name cannot be blank.")

    # Choice 3 - Remove item
    elif choice == "3":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
            print("Total items:", len(shopping_list))
        else:
            item_name = input("Enter the item name to remove: ").strip()

            matched_item = None

            for item in shopping_list:
                if item.lower() == item_name.lower():
                    matched_item = item
                    break

            if matched_item is not None:
                shopping_list.remove(matched_item)
                print(matched_item, "has been removed successfully.")
                print("Total items:", len(shopping_list))
            else:
                print("Sorry! Item does not exist in the shopping list.")

    # Choice 4 - Update item
    elif choice == "4":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
            print("Total items:", len(shopping_list))
        else:
            print("\nCurrent Shopping List:")

            number = 1

            for item in shopping_list:
                print(number, item)
                number += 1

            item_number_input = input(
                "Enter the item number you want to update: "
            ).strip()

            try:
                item_number = int(item_number_input)

                if item_number >= 1 and item_number <= len(shopping_list):
                    index = item_number - 1

                    new_item = input("Enter the new item name: ").strip()

                    if new_item:
                        old_item = shopping_list[index]
                        shopping_list[index] = new_item

                        print(
                            old_item,
                            "has been updated to",
                            new_item + "."
                        )
                        print("Total items:", len(shopping_list))
                    else:
                        print("New item name cannot be blank.")
                else:
                    print("Invalid item number.")

            except ValueError:
                print("Please enter a valid numeric item number.")

    # Choice 5 - Exit
    elif choice == "5":
        print("Exiting Shopping List Manager.")
        print("Final total items:", len(shopping_list))
        break

    # Invalid menu choice
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
