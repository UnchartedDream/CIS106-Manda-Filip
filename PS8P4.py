def DeterminePayRt(JobCode):
  if JobCode == "L":
    PayRt = 25
  elif JobCode == "A":
    PayRt = 30
  elif JobCode == "J":
    PayRt = 50
  else:
    PayRt = 0
  return PayRt

TotalPay = 0

Run = input("Do you want to run this program y/n: ")
print("")

while Run == "y":
  LastName = input("Please enter last name: ")
  JobCode = input("Please enter Job Code: ")
  HrsWorked = float(input("Please enter hours worked: "))
  PayRt = DeterminePayRt(JobCode)
  if HrsWorked > 40:
    GrossPay = (PayRt*40) + (PayRt * ((HrsWorked - 40)*1.5))
  else:
    GrossPay = (PayRt * HrsWorked)
  print("")
  print(LastName)
  print("Gross pay is: ${:.2f}" .format(GrossPay))
  TotalPay = TotalPay + GrossPay
  print("")
  Run = input("Do you want to run this program again? y/n: ")
  print("")

print ("Total of all gross pay is ${:.2f}" .format(TotalPay))