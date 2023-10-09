#input phase
StartValue = float(input("Please enter the Start Value: "))
StopValue = float(input("Please enter the Stop Value: "))
IncrementValue = float(input("Please enter the Increment Value: "))

#Output before Startvalue is changed
print("")
print("Start Value entered is: ", StartValue)
print("")
print("Stop Value entered is: ", StopValue )
print("")
print("The Increment Value equels", IncrementValue)
print("The Increment Value will be added to the Start Value untill it equals the Stop Value")

#Processing phase
while StartValue < StopValue:
  StartValue = (StartValue + IncrementValue)

#Output once stopvalue reached
print("The Stop Value ", StopValue, "has been reached")