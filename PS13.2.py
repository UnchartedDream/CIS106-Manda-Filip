#define object
class Students:
  def __init__(self, first, last, DistCode, credits):
    self.first = first
    self.last = last
    self.DistCode = DistCode
    self.credits = credits

  def cost(self, DistCode):
    if DistCode == "I":
      rate = float(250)
    elif DistCode == "O":
      rate = float(500)
    else:
      print("Not a valid District Code")
    return rate
    
  def tuition(self, rate): 
    tuition = (float(rate) * float(self.credits))
    return tuition

#Back to Main - Instantiate the object
Student_1 = Students('Frank', 'Alvino', 'I', 10)

#use the object
print(Student_1.first)
print(Student_1.last)
print(Student_1.DistCode)
print(Student_1.credits)
print(Student_1.tuition(Student_1.cost(Student_1.DistCode)))
