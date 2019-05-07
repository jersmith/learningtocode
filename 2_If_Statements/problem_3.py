day_of_week = int(input("Enter a day of week (0 - 6): "))
days_to_add = int(input("Enter days to add: "))

# how many days later
next_day = day_of_week + days_to_add

# which day of the week is this? Hint, it's the remainder of the total number of days
# later if you divide by a week (7 days)
next_day_of_week = next_day % 7
print("Next day is: " + str(next_day_of_week))