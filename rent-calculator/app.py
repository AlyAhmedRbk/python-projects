rent = int(input("Enter your flat rent : ")); 
food = int(input("Enter amount of food ordered : ")); 
electricity_consumed = int(input("Enter the total amount of electricity consumed  : ")); 
charge_per_unit = int(input("Enter the charge per unit of electricity : "));
total_persons = int(input("Total Persons living in room : "));

electricity  = int(electricity_consumed * charge_per_unit);

total_amount = float((rent + food + electricity + charge_per_unit))/3

print("Total Amount per head : ", total_amount);