
list = []
list2 = []
total = 0

while True:

    try:
        choice = input("Want to add items (Yes/No)= ")

        if choice == "Yes" or choice == "yes":
            item = input("Enter the item name = ")
            category = input("Enter the category = ")

            while True:
                try:
                    price = int(input("Enter the price = "))
                    break

                except ValueError:
                    print("Invalid price! Please enter numbers only.")

            expense = {"item": item,
                       "Category": category,
                       "price": price
                       }

            list.append(expense)
            k = expense["price"]
            list2.append(k)
            total = total + k

        else:
            print("Thanks")
            print("Your purchased details are here = ")
            print(list)
            print("Your total amount spent = ", total)
            break

    except ValueError:
        print("Please enter valid input.")
