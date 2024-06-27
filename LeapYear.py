do_you_want_to_continue = "y"

def is_leap_year(year):
    if year % 4 != 0:
        print(f"{year}is not a leap year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")

while do_you_want_to_continue == "y":
    year = int(input("Enter a year: "))
    is_leap_year(year)

    #do_you_want_to_continue = input("Do you want to continue? (y/n): ")
do_you_want_to_continue = input("y")
if do_you_want_to_continue == "n":
   print("Thank you for using the leap year checker!")
else:
   print("Invalid option")



