def startEnd(Names):
    for i in Names:
        if i.startswith('A') and i.endswith('a'):
            print(i)
#na=['aassdd','sseerr','jhg','Ahhha']
n=int(input("Enter the limit:"))
lis=[]
for i in range(n):
    x=input("Enter the name:")
    lis.append(x)
print("Names starting with 'A' and ending with a are:")
startEnd(lis)
