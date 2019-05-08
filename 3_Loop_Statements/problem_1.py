# we have to import random to use this command
import random

phone_number = ""

# The len() command tells us how long a string is
while len(phone_number) < 12:
  # The randint function takes a start and stop range, and
  # returns a random integer in that range

  phone_len = len(phone_number)
  if phone_len == 3 or phone_len == 7:
    phone_number = phone_number + "-"

  phone_number = phone_number + str(random.randint(0, 9))

print(phone_number)
