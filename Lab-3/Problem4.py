character = input("Enter a character: ").lower()

if len(character) != 1 or not character.isalpha():
    print("Enter one alphabetic character")
elif character in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")