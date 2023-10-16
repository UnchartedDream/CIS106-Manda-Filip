# code to read from the file goes here
f = open("dataPS7P3.txt", "r")
total_bonus = float(0)
lastname = f.readline()
while lastname != "":
  salary = float(f.readline())
  print("Employee Last Name: ", lastname)
  print("Employee Salary: ${:.2f}".format( salary))
  if salary >= 100000:
    bonus_rate = float(.2)
  elif salary == float(50000):
    bonus_rate = float(.15)
  else:
    bonus_rate = float(.1)
  bonus = float(salary * bonus_rate)
  total_bonus = bonus + total_bonus
  print("Employee Bonus: ${:.2f}" .format(bonus))
  print()
  lastname = f.readline()
f.close()

#output
print()
print("Total Bonus: ${:.2f}" .format(total_bonus))

  