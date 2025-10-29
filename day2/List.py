l=[3,5,6,7,"Babulu"]             #List is mmutable
print(type(l))
print(l)
print(l[0])
for item in l:
    print(item)



print(len(l)-3)



marks=[12,14,25,30,14,52]
if 6 in marks:
    print("Yes")
else:
    print("No")

print(marks[1:len(marks):2])

m=[11,21,3,4,5]
m.sort()
print(m)
m.reverse()
print(m)
m=l.copy()
print(m)
m.append(99)
print(m)
m.insert(2,100)
print(m)                
