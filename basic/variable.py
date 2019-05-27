a= 10
b= 5
print(a+b) #result will print 15 here
a =10.5
print(b+a) # now print 15.5 here
#and varial a is a float type variable
print(type(a)) #print <class 'float'>
print(type(b)) #print <class 'int'>
name = 'String type'
print(type(name)) # <class 'str'>

#if we want to find any variable class type then
#we use this type() methods and in type method we pass
#our desire variable

name = 'University'
print(name[1:5]) #print nive
#thats mean it will print name[1] to name[5] index number character
print(name[:3]) #print Uni

print(name[-3]) #print i

print(name[:-3]) #print Univers
#thats means it will minus index from the last and all of the index
#will print without the last
#it will print from Zero to (last_index-3)
# important things if any index is not found then it will show a IndexError: string out of range
# print(name[15])
#we also acces any string variable like this way   varname[index]
