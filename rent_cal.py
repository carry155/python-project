rent = int(input("enter your hostel/falt rent ="))

food = int(input("enter the ammount of food ordered ="))

electric = int(input("enter your electric city amount ="))

charge = int(input ("enter the charge  per unit = "))

person = int(input("enter the number of person room/flat = "))

total_bill = electric * charge

output = (food + rent + total_bill )/ person 

print("Each person will pay = ",output)