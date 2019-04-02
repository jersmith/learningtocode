# We have to convert the input to a number. Here we use an int, but we could use a float()
# so the user could enter things like 21.4
fahrenheit = int(input("Enter your Fahrenheit temperature: "))

# Notice that because there is division in this formula, that even if every other number in it
# is an integer, the answer will be a decimal (floating value). 
celcius = ((fahrenheit) - 32) * 5 / 9

# We have to convert the answer to string, since you can't concatenate numbers!
print("Celcius: " + str(celcius))