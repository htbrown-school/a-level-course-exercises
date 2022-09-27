import random

throw1 = random.randrange(1, 6)
throw2 = random.randrange(1, 6)

if throw1 == throw2:
    print(f"You threw a double - you scored {(throw1 + throw2) * 2}.")
else:
    print(f"You scored {throw1 + throw2}.")