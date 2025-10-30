s={2,4,2,6}      #set is unorder and unchangeable
print(s)
print(type(s))
s1={1}
print(type(s1))
s3 = set()
print(type(s3))
# Set methods
m={1,2,3}
n={4,5,6,1}
print(m.union(n))   #union
print(m.intersection(n))  #intersection
print(m,n)
print(m.difference(n))   #difference
print(n.difference(m))
m.update(n)
print(m)  # Output: {1, 2, 3, 4, 5, 6} #update
