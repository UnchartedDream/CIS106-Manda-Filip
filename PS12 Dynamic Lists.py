def dl1 (mylist):
  n = int(input("Number of items for your list: "))
  for n in range(0,n,1): #each time we loop over we add (lists by default start at 0)
    s = int(input("Enter an integer: "))
    mylist.append(s) #to add value from user into list
  return mylist

def displaylist(mylist):
  for item in mylist:
    print(item)

#main
mylist = [] #defining an empty list
mylist = dl1(mylist)
displaylist(mylist) #display each item in the list
print(mylist) #Print the list

#Insert Element
#mylist.insert(1,99) #inserts number
#print("")
#print("Score of 99 inserted in position 1")
#print(mylist) #Print the list

#Replace Element
#mylist[1] = 100
#print("")
#print("Score of 99 replaced with 100 in position 1")
#print(mylist)

#Add a list to another list
print("")
mylist2 = [500, 600, 700, 800, 900]
print("Second list")
print(mylist2)
print("")
print("My List Extended with 2nd list")
mylist.extend(mylist2)
print(mylist)

#Remove my element/value in list
#mylist.remove(800)
#print("")
#print("My List Extended with 800 removed")
#print(mylist)

#remove 3rd item
#del mylist[2]
#print("")
#print("My List Extended with 3rd element removed")
#print(mylist)

#~~List of Grades Problem 7-10
#Grades = ["A", "B", "C", "A", "A", "C"]
##count_of_A = Grades.count("A")
#print("Count of A's in list is:", count_of_A)

#Grade_To_Find = "B"
#Position_of_1st_B = Grades.index(Grade_To_Find)
#print("")
#print("Postion of first B in list:", Position_of_1st_B)

#Grade_To_Find_F = "F"
#Position_of_1st_f = Grades.index(Grade_To_Find_F)
#if Position_of_1st_f >= 0:
  #print("Position of F is:", Position_of_1st_f )
#else:
  #print("No F's found in list")

#Part 11
print("")
mylist2.clear()
print("List after clearing 2nd list that was added to it", mylist )

#Part 12
#del mylist2
#print(mylist2)

#Part #13
players = ["WAQ", "Davis", "Baez", "Up", "Bryan"]

#14
print("")
players.sort()
print("Sorted players list:", players)

#15
print("")
players2 = players.copy()
print("Copy of players list (players2)", players2)

#16
print("")
players2.reverse()
print("Players List:", players)
print("Players2 list:", players2)
