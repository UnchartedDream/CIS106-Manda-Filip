class Car:
  def __init__ (self, make, model, price):
    self.make = make
    self.model = model
    self.price = price
    self.discount_price = (.9* price)
  
  def Print_Car(self):
    return print("Car:",self.make,"\t", self.model,"\t","$",self.price,\
    "\t","$",self.discount_price)

class Sport(Car):
  def __init__(self, make, model, price):
    super().__init__(make, model, price)
    self.option_price= 0

  def add_sport_wheels(self, option):
    if option == "Y":
     self.option_price = self.option_price + 1000.00
    else:
     pass

  def add_sport_engine(self, option):
    if option == "Y":
      self.option_price = self.option_price + 3000.00
    else:
      pass

  def add_sport_interior(self, option):
    if option =="Y":
       self.option_price = self.option_price + 2000.00
    else:
      pass

  def price_with_options(self):
    total_price = self.discount_price + self.option_price
    return print("Total Price with Options: $" , total_price)

#Instantiate
Car_1 = Sport("Subaru", "WRX", 40_000)

#display before options
print("Car selection before optional addons:")
print("\t Make \t Model \t\t Price \t\t Discount Price")

Car_1.Print_Car()

#add options
Car_1.add_sport_wheels(option = "Y")
Car_1.add_sport_engine(option = "Y")
Car_1.add_sport_interior(option = "Y")

#After adding options
print("")
Car_1.price_with_options()