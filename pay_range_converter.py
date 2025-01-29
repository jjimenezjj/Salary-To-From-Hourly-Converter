# Converts hourly pay to annual salary
def hourly_pay(n):
    conversion_to_annual = float(n) * 8 * 5 * 52
    return conversion_to_annual


# Converts annual salary to hourly pay
def annual_salary(n):
    conversion_to_hourly = float(n) / 52 / 5 / 8
    return round(conversion_to_hourly, 2)


# Option menu that allows for looping using "while"
while True:
    user_choice = input("""
Here are your options...
            
1) Convert hourly rate to annual salary 
2) Convert annual salary to hourly rate 
            
Enter an input of 1 or 2 to choose: """)

    if user_choice == "1":
        hour_rate = input("Enter hourly rate amount: ")
        print(hourly_pay(hour_rate))
        break
    elif user_choice == "2":
        ann_sal = input("Enter annual salary amount: ")
        print(annual_salary(ann_sal))
        break
    else:
        print("Invalid input. Enter either 1 or 2 \n")
