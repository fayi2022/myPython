def countnotvowel(str):
    count=0
    for i in str:
        if i not in 'aeiouAEIOU':
            count+=1
            print(i)
    print("Total number of characters which are not vowels=",count)

mystr='fayisA'
countnotvowel(mystr)
