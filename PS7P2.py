#input/define
a = 1
b = 0

#loop
for x in range(1,21,1):
  c = a+b
  print(x,")   ", c)
  a=b
  b=c