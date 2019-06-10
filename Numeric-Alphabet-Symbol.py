x = input("Enter an alphabet, number or any symbol : ")
if len(x) > 1:
    print("Please enter only one character, number or any symbol")
elif ("a" <= x <= "z") or ("A" <= x <= "Z"):
    print("It's an alphabet")
elif "0" <= x <= "9":
    print("It's a number")
else:
    print("It's a symbol")
