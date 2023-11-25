def displaynames (name, ave):
  for i in name, ave:
    print(i)

#search function
def seqsearch(name, ave):
  l = len(name)
  sindex = -1
  for y in range(0,l,1):
    if name[y] == sname:
      sindex = y
  return sindex
  
#run file
f = open("BattingAve.txt", "r")

#define arrays
name = []
ave = []

lastname = f.readline()

#While loop for knowing what line is what
while lastname != "":
  name.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  ave.append(s)
  lastname = f.readline()

#close file
f.close()

displaynames (name, ave)

#run program
ask = input("Do you want to run this program? y/n: ")

while ask =="Yes" or ask == "y":
  sname = input("What name would you like to look up?: ")
  i = seqsearch(name, sname)
  if i == -1:
    print(sname, "Name not found")
  else:
    print (name[i], "batting average of ", ave[i])
  ask = input("Do you want to run this program? y/n: ")

    



