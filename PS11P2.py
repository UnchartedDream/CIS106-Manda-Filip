def displaynames(name, score):
  for i in name:
    print(i)
  for y in score:
    print (y)

def displayr(name,score):
  l = len(name)
  print ("Number of array elements: ", l)
  print("")
  print("Names and scores in order: ")
  print("")
  for y in range (0,l,1):
    print(name[y], score[y])
  print("")
  print("Names and scores in reverse:")
  print("")
  for y in range (l-1, -1, -1):
    print(name[y], score[y])

#run file
f = open("lnames.txt", "r")

#define arrays
name = []
score = []

lastname = f.readline()

while lastname != "":
  name.append(str(lastname).rstrip("\n"))
  s= float(f.readline())
  score.append(s)
  lastname = f.readline()

#close file
f.close()

#call function

displayr(name, score)