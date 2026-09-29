from datetime import date

test = input("Enter a date (DD-MM-YYYY): ")
split_date = test.split("-")

day = int(split_date[0])
month = int(split_date[1])
year = int(split_date[2])

today = date.today()
age = today.year - year

if (today.month, today.day) < (month, day):
    age -= 1

print(age)