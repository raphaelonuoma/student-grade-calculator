print("Student Grade Calculator")

score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))

average = (score1 + score2 + score3) / 3

print(f"\nAverage Score: {average:.2f}")

if average >= 70:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
elif average >= 45:
    print("Grade: D")
else:
    print("Grade: F")
