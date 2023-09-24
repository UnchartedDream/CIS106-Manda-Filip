#input phase
LastName = str(input("Please enter last name: "))
NumberOfDependents = float(input("Please enter number of dependants: "))
GrossIncome = float(input("Please enter Gross Income: "))

#if defining/Processing phase
AdjGrossIncome = float(GrossIncome - (NumberOfDependents * 12000))

if AdjGrossIncome > 50000:
  TaxRate = .2
else: 
  TaxRate = .1

IncomeTaxAmount = float(AdjGrossIncome * TaxRate)

if IncomeTaxAmount < 0:
  IncomeTaxAmount = 100

#output phase
print("")
print("Last Name:",LastName)
print("")
print("Gross Income:", GrossIncome)
print("")
print("Number of dependants:", NumberOfDependents)
print("")
print("Adjusted Gross Income:", AdjGrossIncome)
print("")
print("Income Tax amount:", IncomeTaxAmount)