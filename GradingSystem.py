print("Welcome to the Grading System")

yourMark = int(input("Enter your mark to check your grade "))

if yourMark >= 90 and yourMark <= 100:
    print("Your grade is A")
elif yourMark >= 80 and yourMark <90:
        print("B")
elif yourMark >= 70 and yourMark <80:
        print("C")
elif yourMark >= 60 and yourMark < 70:
        print("D")
elif yourMark < 60 and yourMark >= 0:
        print("F")
else:
            print("Enter a valid mark")