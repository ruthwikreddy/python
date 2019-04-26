thislist = ["ruthwik", "deepak" , "sai" ,"anand"]
thislist.insert(1, "shashank")
if "shashank" in thislist:
    print("yes, 'shashank' is in the list")
print(len(thislist))
thislist.append("gaurav")
if "gaurav" in thislist:
    print("yes, 'gaurav' is added to the list")
print(len(thislist))
mylist = list(thislist)
print(mylist)
mylist.append("sandhya")
if "sandhya" in mylist:
    print("yes, 'sandhya' is added to my list")
print(mylist)
print(len(mylist))
print(thislist)
print(len(thislist))
if "das" in mylist:
    print("yes, 'das' is in the list")
else:
    print("no, das is not in the list" )

thislist.append("sandhy")
if "sandhya" in thislist:
    print(thislist)
else:
    print(len(thislist))
thistuple = ("karthik", "vishal", "vamshi")
print(thistuple)
if "vishal" in thistuple:
    print(len(thistuple))
else:
    print(len(thislist))
set = { "miracle", "oracle" ,"microsoft"}
print (set)
set.add("dell")
print(set)
set.update(["deloitte", "ola", "uber"])
print(set)
print(len(set))
x = set.pop()
print(x)
print(set)
print(len(x))
print(set)
