name="Joseph"

print(name[0])
print(name.lower())
print(name.upper())

print(name.__len__())

##############################
#List
names=["Jake","Kofi", "Mensah"]
print(names[1])
print(names)

names.append("Joseph")
print(names)

names.sort()
print(names)

##################################
# Sets
s=set()
s.add(1)
s.add(3)
s.add(2)
s.add(4)
s.add(3)
print(s)
s.remove(2)
print(s)
print(len(s))
print(f"This set has {s.__len__()} elements")
