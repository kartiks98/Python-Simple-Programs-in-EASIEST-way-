x = input("Enter an alphabet, number or any symbol : ")
if len(x) > 1:
    print("Please enter only one character, number or any symbol")
elif x >= "a" and x <= "z":
    print("It's an alphabet")
elif x >= "0" and x <= "9":
    print("It's a number")
else:
    print("It's a symbol")
