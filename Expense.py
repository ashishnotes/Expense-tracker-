list = []
while True:

  choice = input("Want to add items (Yes/No)= ")

  if choice == "Yes" or choice == "yes":
    item = input("Enter the item name = ")
    category = input("Enter the category = ")
    price = int(input("Enter the price = "))

    expense = {"item":item,
               "Category" :category,
               "price": price
              }
    list.append(expense)

    print(list)
  else :
    print("Thanks")
    break
