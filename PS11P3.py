def displayr(name, score):
  l = len(name)
  print("Number of array elements: ", l)
  print("")
  print("Arrays in Order:")
  print("")
  for y in range (0,l,1):
    print(name[y], score[y])
  print("")
  print("Arrays in Reverse:")
  print("")
  for y in range (l-1, -1, -1):
    print(name[y], score[y])
  #function to find highest and lowest score
def hilow(name, score):
  l = len(name)
  hiscore = -1.0
  lowscore = 999999.99
  for y in range (0,l,1):
    if float(score[y]) > float(hiscore):
      hiindex = y
      hiscore = score[y]     
    if float (score[y]) < float(lowscore):
      lowindex = y
      lowscore = score[y]
      print("")
  print("highest salary", name [hiindex], score [hiindex])
  print("lowest salary", name[lowindex], score [lowindex])

#open file
f = open("lnameP3.txt", "r")

lastname = f.readline()
name = []
score = []

while lastname!= '':
  name.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  score.append(s)
  lastname = f.readline()

  #close file
f.close()

#call function
displayr(name, score)
hilow(name, score)

      