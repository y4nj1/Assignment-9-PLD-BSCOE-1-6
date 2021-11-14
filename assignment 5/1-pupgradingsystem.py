# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropped

# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

def getLetter():
    prelimq = input("Is your grade INC, W, or D? Please enter Yes or No: ")
    if prelimq == "Yes":
        textgrade = input("Please enter if your grade is INC, W, or D: ") 
        return textgrade
    else:
        if prelimq == "No":
            _grade = float(input(("Enter your grade here: ")))
            grade = round(_grade)
            return grade

def mark():
    if inputGrade == "INC":
       print("Remarks: \x1b[38;5;207mIncomplete\x1b[0m")
       print("\033[1mYour grade has been recorded.\033[0m")
    elif inputGrade == "W":
       print("Remarks: \x1b[38;5;32mWithdrawn\x1b[0m")
       print("\033[1mYour grade has been recorded.\033[0m")
    elif inputGrade == "D":
        print("Remarks: \x1b[38;5;93mDropped\x1b[0m")
        print("\033[1mYour grade has been recorded.\033[0m")
    else:
        if inputGrade >= 97 and inputGrade <= 100:
            print("Grade:\x1b[38;5;46m 1.00 \x1b[0m")
            print("Remarks: \x1b[38;5;46mExcellent\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")
        elif inputGrade >= 94 and inputGrade <= 96:
            print("Grade:\x1b[38;5;46m 1.25 \x1b[0m")
            print("Remarks: \x1b[38;5;46mExcellent\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")
        elif inputGrade >= 91 and inputGrade <= 93:
            print("Grade:\x1b[38;5;83m 1.50 \x1b[0m")
            print("Remarks: \x1b[38;5;83mVery Good\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")
        elif inputGrade >= 88 and inputGrade <= 90:
            print("Grade:\x1b[38;5;83m 1.75 \x1b[0m")
            print("Remarks: \x1b[38;5;83mVery Good\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")
        elif inputGrade >= 85 and inputGrade <= 87:
            print("Grade:\x1b[38;5;81m 2.00 \x1b[0m")
            print("Remarks: \x1b[38;5;81mGood\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")
        elif inputGrade >= 82 and inputGrade <= 84:
            print("Grade:\x1b[38;5;81m 2.25 \x1b[0m")
            print("Remarks: \x1b[38;5;81mGood\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")
        elif inputGrade >= 79 and inputGrade <= 81:
            print("Grade:\x1b[38;5;20m 2.50 \x1b[0m")
            print("Remarks: \x1b[38;5;20mSatisfactory\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")
        elif inputGrade >= 76 and inputGrade <= 78:
            print("Grade:\x1b[38;5;20m 2.75 \x1b[0m")
            print("Remarks: \x1b[38;5;20mSatisfactory\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")
        elif inputGrade == 75:
            print("Grade:\x1b[38;5;226m 3.00 \x1b[0m")
            print("Remarks: \x1b[38;5;226mPassed\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")
        elif inputGrade >= 65 and inputGrade <= 74:
            print("Grade:\x1b[38;5;88m 5.00 \x1b[0m")
            print("Remarks: \x1b[38;5;88mFailed\x1b[0m")
            print("\033[1mYour grade has been recorded.\033[0m")


inputGrade = getLetter()
_Mark = mark()





