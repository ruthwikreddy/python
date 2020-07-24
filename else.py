a = 440
b = 435
if b > a:
    print("b is greater than a")
elif b == a:
    print("a is equal than b")
else:
    print(" a is greater than b")
i = 1
while i < 6:
  i += 1
  if i == 3:
    continue
  if i == 4:
    break
  print(i)
    

people = ["deepu", "vineeth", "amit"]
for x in people:
  print(x)
  if  x ==  "amit":
    break
  if  x ==  "vineeth":
    continue
  print(x)

for y in range(100):
  print(y)
else:
  print("100") 

friends = ["ruth", "wik" , "reddy"]
enemies = ["sai" , "nadh" , "peruri"]
for x in friends:


#myhomeschool
  for y in enemies:
    print(x,y)

def my_function(fname):
  print("Hello from a function")
  people = ["deepu", "vineeth"]
  for x in people:
     print(x)
  print(fname + "reddy")
my_function("Ruthwik")
