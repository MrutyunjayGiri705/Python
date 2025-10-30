dic={
    "Babulu":25,
    "Chintu":30,    
    "Dinku":35
}
print(dic["Babulu"])
# Dictionaries mathods
ep={123:12,154:25,155:30}
pe1={000:25,147:58}
ep.update(pe1)
print(ep)  
# ep.clear()
# print(ep)
emp={}
print(emp)

ep.popitem() #Deletes last item       
print(ep)
# del ep
# print(ep) #Deletes the dictionary entirely
o={1:"A",2:"B",3:"C"}
o.pop(2) #Deletes item with key 2
print(o)