fprw=open('myfile.txt','r+')
data=fprw.read()
print(data)
fprw.write('Checking')
data1=fprw.read()
print(data1)
fprw.close()