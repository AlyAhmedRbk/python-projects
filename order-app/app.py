#Resturent Order App

menu = {
    "Pizza" : 250,
    "Burger" : 150,
    "Coffee" : 450,
    "Fries" : 100,
}

# print(menu);
# Grert 
print("=====================================================================");
print("Welcime to our Chill Grill Resturent");
print("Pizza   :  Rs250\nBurger  :  Rs150\nCoffee  :  Rs450\nFries   :  Rs100");
print("=====================================================================");

total_order = 0;
item_1 = input("Enter the name of item you want to order =");
if item_1 in menu:
    total_order += menu[item_1];
    print(f"Your item {item_1} is added to order list");
else:
    print(f"Please Order something that is prensent in menu.\n{item_1} is not available");
    
another_order =input("Do you want to order another item? (Yes/No)");

if (another_order == "yes" or another_order == "y"):
    item_2 = input("Enter your second order plz");
    if (item_2 in menu):
        total_order +=menu[item_2];
        print(f"Your item {item_2} is added to order list");
        print(f"Your Total bill is : {total_order}");    
    else:
        print(f"Please Order something that is prensent in menu.\n{item_2} is not available");
        print(f"Your Total bill is : {total_order}");    
        
print("Thanks For Using our App...")