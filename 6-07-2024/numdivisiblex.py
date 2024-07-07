#Function to the number which is not divisible by x   
def numnotdivx(num,x):
    print("The number in the string which are  divisible by ",x,"are:")
    for i in num:
        if i%x==0:
            print(i)
mynum=[12,34,20]
a=3
numnotdivx(mynum,a)
