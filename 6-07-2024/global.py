#Global variable
b=30
def display():
    b=999
    print("b inside display():",b)

display()
print("b outside display():",b)
