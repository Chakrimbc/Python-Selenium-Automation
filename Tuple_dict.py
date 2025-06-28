#tup = (1,2,"chakri")
#print(tup[0])
#tup[2] = "gonthini" # Here tuple is immutable that means once created cannot be changed until it changes to List
#print(val)


#Dictionary
dcit = {"a":2,6:"bale",3:4}
print(dcit[6])
print(dcit["a"])
print(dcit[3])
dcit["me"] = "human"
print(dcit)
del dcit["me"]
print(dcit)
#print(dcit["me"])#If wanted to print only keys convert the variable into list and do that

print(dcit.values())
print(list(dcit.keys()))
