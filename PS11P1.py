def displaynames(name):
  for i in name:
    print(i)

def displayr(name):
  l = len(name)
  print ("Number of array elements: ", l)
  print("")
  print("Names in order: ")
  print("")
  for y in range (0,l,1):
    print(name[y])
  print("")
  print("Names in reverse:")
  print("")
  for y in range (l-1, -1, -1):
    print(name[y])

#run file
f = open("lname.txt", "r")

#define arrays
name = []

lastname = f.readline()

while lastname != "":
  name.append(str(lastname).rstrip("\n"))
  lastname = f.readline()

#close file
f.close()

#call function

displayr(name)