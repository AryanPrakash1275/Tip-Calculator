print("Welcome to Tip-Calculator")
print("Created by Aryan\n")

total_bill = float(input("What was the total bill?\n"))
tip_percent = float(input("How much would you like to tip? Please input in percentage.\n"))
number_of_people = int(input("How many people to split the bill?\n"))

#maths
calc1TIP = float((total_bill * tip_percent)/100)
calc2TB = float(total_bill + calc1TIP)
calc3FINAL = round(float(calc2TB/number_of_people),2)

print(f"Each person should pay:{calc3FINAL}")
