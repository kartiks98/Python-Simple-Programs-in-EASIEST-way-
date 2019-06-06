print("Enter marks in DATA STRUCTURES, COMPUTER NETWORKS, DIGITAL ELECTRONICS, MICROPROCESSOR, OPERATING SYSTEM respectively (out of 50 each) : ")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

percentage = ((a+b+c+d+e)/250)*100

if a < 50 or b < 50 or c < 50 or d < 50 or e < 50:
    print("Please enter valid marks")

elif percentage == 100:
    print("Are you a Robot???")

elif percentage >= 80:
    print("Impressive!!! That's an A grade with", percentage, "%")

elif 60 <= percentage < 80:
    print("Good!!! That's a B grade with", percentage, "%")

elif 40 <= percentage < 60:
    print("Poor!!! That's a C grade with", percentage, "%")

else:
    print("Sorry!!! You failed...Better luck next time!!!")
