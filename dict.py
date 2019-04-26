sdict  = {
           "name": "ruthwik ",
           "organization": "Miracle",
           "Position": "DevOps Engineer",
           "Income": "75k per annum"
         }
sdict["organization"] = "Oracle"

print(sdict)
z = sdict["organization"]
print(z)
sdict["organization"] = "Miracle"
print(z)
for x in sdict:
    print(x)
for x in sdict.values():
    print(x)
for x,y in sdict.items():
    print(x,y)
sdict["tools"] = "Docker"
for x,y in sdict.items():
    print(x,y)
sdict.pop("tools")
for x,y in sdict.items():
    print(x,y)
sdict["tools"] = "Azure"

print(sdict)
