percent = float(input("Enter percentage: "))
if percent < 25:
    print("Grade: D")
elif percent < 45:
    print("Grade: C")
elif percent < 65:
    print("Grade: B")
elif percent < 85:
    print("Grade: A")
else:
    print("Grade: A+")