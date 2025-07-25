print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age"))
    if age <= 12:
        bill=4
         print("7")
    elif age <= 18:
        bill=6
        print("Please pay ")
    else:

        print("12")

else:
    print("Sorry you have to grow taller before you can ride.")
