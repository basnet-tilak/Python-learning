age = 29
price = 19.34
print("My Age", age)
print("Price of the book", price)

def myFunc():
    global x
    x = "`This is Global Variable value`"
    print("Price : ", price)
    print(x)
    
myFunc()
print("Global variable ouside the methods", x)

