#input
principle = float(input("Enter principle: "))
rate = float(input("Enter rate: "))
total_interest = float(0)
print()
print("Year  Beginning Balance  End Balance")

#loop
for x in range (1,6,1):
  interest = principle * rate
  total_interest = total_interest + interest
  ending_balance = principle + interest
  print(x, "    ${:.2f}" .format(principle), "         ${:.2f}" .format(ending_balance))
  principle = ending_balance

#outside of loop/loop ending
print()
print("Total interest earned: ${:.2f}" .format(total_interest))