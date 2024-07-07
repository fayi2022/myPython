msg='Save Water-2024'
txt=''
for i in range(0,len(msg)):
    if msg[i]>='a'and msg[i]<='w':
        txt=txt+msg[i]
    elif msg[i]>='A' and msg[i]<='T':
        txt=txt+msg[i-1]
    elif msg[i].isupper():
        txt=txt+msg[i].lower()
    elif msg[i]>='1' and msg[i]<='3':
        txt=txt+str(int(msg[i])+1)
    else:
        txt=txt+'*'
print(txt)
