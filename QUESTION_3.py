grade = int(input("Please enter your grade: "))
if 90 <= grade <= 100:
    print("grade A")
elif 80 <= grade <= 89:
    print("grade B")
elif 70 <= grade <= 79:
    print("grade C")
elif 60 <= grade <= 69:
    print("grade D")
elif 60 > grade >= 0:
    print("FAIL")
else:
    print("Enter a valid grade!!!")
    