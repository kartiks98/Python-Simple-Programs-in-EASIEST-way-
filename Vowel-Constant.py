x = input("Enter a character : ")
if len(x) > 1 and (("a" <= x <= "z") or ("A" <= x <= "Z")):
    print("Please enter only one character")
elif x == "a" or x == "A" or x == "e" or x == "E" or x == "i" or x == "I" or x == "o" or x == "O"or x == "u" or x == "U":
    print("It's a Vowel")
else:
    print("It's a Consonant")
