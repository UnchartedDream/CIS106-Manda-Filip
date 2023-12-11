class Employee:
  #pass #can use pass to skip for now
  def __init__ (self, first, last, pay): # __init__ is like initilize. use self first!
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'
  #within class creating a method
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def bonus(self,rate):
    #for second question add if statment here!
    b = float(rate) * float(self.pay)
    return b


emp_1 = Employee('Corey', 'Schafer', 50_000)
emp_2 = Employee('Test', 'User', 60_000)


#print(emp_1)
#print(emp_2)

#Manual assignments
#emp_1.first = 'Corey'
#emp_1.last = 'Schafer'
#emp_1.email = 'Corey.Schafer@company.com'
#emp_1.pay = 50_000

#emp_2.first = 'Test'
#emp_2.last = 'User'
#emp_2.email = 'Test.User@company.com'
#emp_2.pay = 60_000

#print(emp_1.email)
#print(emp_2.email)

#print(emp_1.fullname()) #need () here sinc it is a method vs attribute

#print('{} {}'.format(emp_1.first, emp_1.last))

#print("")
#print("Employee 1 info:")
#print(emp_1.email)
#print(emp_1.first)
#print(emp_1.last)
#print(emp_1.pay)
#print(emp_1.bonus(0.10))
#print(emp_1.bonus(0.20))

class Manager:
    def __int__ (self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
    def fullname(self):
      return'{} {}'. format(self.first, self.last)
    def bonus (self,rate):
      ManB = float(rate) * float(self.pay)
      return ManB

Man_1 = Employee('John', 'Smith', 70_000)
Man_2 = Employee('Test', 'User', 80_000)

print("")
print("Manager 1 info:")
print("First Name:",Man_1.first)
print("Last Name",Man_1.last)
print("Base Pay", Man_1.pay)
print("Bonus", Man_1.bonus(0.40))
