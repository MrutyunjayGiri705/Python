try:
    l = [1, 2.3]
    i = int(input("Enter the number: "))
    print(l[i])
except:
    print("Error occurred")
finally:
    print("I am always executed")
