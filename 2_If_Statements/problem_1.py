guess = int(input("Enter a number"))

if guess / 2 - (guess // 2) == 0:
    print("Event")
else:
    print("Odd")