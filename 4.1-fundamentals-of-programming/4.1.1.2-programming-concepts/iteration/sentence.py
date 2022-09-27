sentence = input("Enter a sentence: ")
count = 0

for i in sentence:
    if i.lower() == "e":
        count += 1

print(f"That sentence has {count} \"e\"s in.")

# Challenge & Further Challenge
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0
vowel_list = []

for i in sentence:
    if (i.lower() in vowels) and (i.lower() not in vowel_list):
        vowel_list.append(i.lower())
        vowel_count += 1

print(f"There are {vowel_count} unique vowels in that sentence.")
print("The list of vowels in that sentence is", vowel_list)
