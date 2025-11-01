x=4
# print(x=]
def hello():
    global x
    x=10
    y=5
    print(f"The local x is {y}")
    print("Mrutyunjay")
    
hello()
print(f"The global x is {x}")