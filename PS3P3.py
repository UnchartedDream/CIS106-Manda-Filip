#input phase
totalmealcost = float(input("Please enter cost of the meal "))

#process phase
tip15 = (0.15 * totalmealcost)
tip18 = (0.18 * totalmealcost)
tip20 = (0.20 * totalmealcost)

#output phase
print("With at 15% tip:")
print("")
print("Total: ", totalmealcost)
print("Tip: ",tip15)
print("Total with Tip: ", (tip15+totalmealcost))
print("")
print("With at 18% tip:")
print("")
print("Total: ", totalmealcost)
print("Tip: ",tip18)
print("Total with Tip: ", (tip18 + totalmealcost))
print("")
print("With at 20% tip:")
print("")
print("Total: ", totalmealcost)
print("Tip: ",tip20)
print("Total with Tip: ", (tip20+totalmealcost))