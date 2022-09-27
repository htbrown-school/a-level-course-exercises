codes = []
codes_ab = []
codes_00 = []

while len(codes) < 5:
    code = input("Enter product code: ")

    if not code.startswith("AB") and not code.startswith("AS"):
        print("Invalid code.")
        continue

    codes.append(code)

    if code.startswith("AB"):
        codes_ab.append(code)
    if code.endswith("00"):
        codes_00.append(code)

print(f"There were {len(codes_ab)} codes starting in AB and {len(codes_00)} codes ending in 00.")