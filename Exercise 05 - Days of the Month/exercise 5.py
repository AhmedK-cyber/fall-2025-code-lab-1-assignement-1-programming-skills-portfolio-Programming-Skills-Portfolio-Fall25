month_days = {
    1: 31,
    2: 28,  
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = int(input("Enter month number between 1 to 12: "))

if month < 1 or month > 12:
    print("Invalid month number! Please enter a number between 1 to 12.")
else:
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()
        if leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"The month number {month} has {month_days[month]} days.")
