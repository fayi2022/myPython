#Program to understand the scope of a variable
a=10
c=45
print("The value of a :",a)
print("The value of c :",c)
def myfunction():
    global a
    c=33
    print("The value of c:",c)
    print("The value of a inside the function :",a)
    b=20
    print("Value of b inside the function:",b)
    a=a+20
    print("New value of a is:",a)
myfunction()
print("Value of a outside the function:",a)
print("The value of c:",c)

