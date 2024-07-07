text='UNIT TEST1'
String,i='',0
while i<len(text):
    if text[i]>='0' and text[i]<='9':
        n=int(text[i])
        n=n+1
        String=String+str(n)
    elif text[i].isalpha():
        String=String+(text[i+1])
    else:
        String=String+'#'
    i=i+1
    print(String)
