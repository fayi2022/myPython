#Function to swap the first half of the content in a list
def swapper(numstr):
    new1=[]
    new2=[]
    print(len(numstr))
    for i in range(0,len(numstr)):
        if i<len(numstr)/2:
            new1.append(numstr[i])
        else:
            new2.append(numstr[i])
    print("new1:",new1)
    print("new2:",new2)
    new2=new2+new1
    print("Swapped string is:",new2)

str=[10,20,30,40,50,60]
swapper(str)
