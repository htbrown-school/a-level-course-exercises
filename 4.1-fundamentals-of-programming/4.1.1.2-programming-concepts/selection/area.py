width = int(input("Enter width: "))
length = int(input("Enter length: "))
unit = input("Enter unit: ")

if width == length:
    print(f"This is a square of area {width * length} squared {unit}.")
else:
    print(f"This is a rectangle of area {width * length} squared {unit}")
