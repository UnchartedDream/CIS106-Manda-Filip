#open file
f = open("PS7P5data.txt", "r")

#input
student_count = 0
sum_tuition_owed = 0
cost_per_credit = float(0)
lastname = f.readline()
#loop
while lastname != "":
  dist_code = str(f.readline())
  credits = float(f.readline())
  if dist_code == str("I\n"):
    cost_per_credit = float(250)
  elif dist_code == str("O\n"):
    cost_per_credit = float(500)
  else:
    print("No valid district code entered.")
  print("Last name: ", lastname)
  print("Number of credits taken: ", credits)
  tuition = credits * cost_per_credit
  sum_tuition_owed = (sum_tuition_owed + tuition)
  print()
  print("Tuition owed: ${:.2f}".format(tuition))
  student_count = student_count +1
  print()
  lastname = f.readline()
f.close()
#output out of loop
print()
print()
print("Number of students: {:.0f}".format(student_count))
print()
print("Total tuition owed: ${:.2f}" .format(sum_tuition_owed))