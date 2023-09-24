#Input phase
name = input("Enter name of appliance: ")
cost = float(input("Enter the cost of the appliance: "))

#process phase
if cost > float(1000.00):
  warranty = float(cost * .10)
  
else: 
  warranty = float(cost * .05)

#total needs to be defined later so putting it here. Too early and python doesn't know what it is yet. 

total = cost + warranty

#output phase
print("Appliance name: ", name)
print("Cost of applaince: ", cost)
print("Warranty cost: ",warranty)
print("Total cost: ", total)