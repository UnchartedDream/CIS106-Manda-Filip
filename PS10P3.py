def CompCom(Sales):
  if Sales > 100_000:
    Com = .1
  else:
    Com = .05
  Target = Sales *.05
  ComAmount = Sales * Com
  return Com, Target, ComAmount

#inputs
LastName = input("Please enter last name of sales person: ")
Sales = float(input("Please enter sales: "))

#Call
Com, Target, ComAmount = CompCom(Sales)

#Outputs
print("")
print(f"Sales Person: {LastName}")
print("")
print(f"Commission amount based on sales: {Com}")
print("")
print("Commisison in dollars: ${:.2f}".format (ComAmount))
print("")
print("Next years target: ${:.2f}".format (Target))