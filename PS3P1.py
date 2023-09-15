#input phase
exam1 = float(input("Enter score for Exam 1 "))
exam2 = float(input("Enter score for Exam 2 "))

#processing phase
exam1weight = float(exam1 * .4)
exam2weight = float(exam2 * .6)
finalgrade = float(exam1weight + exam2weight)

#output phase
print("Your final score is a ", finalgrade, " out of 100.")