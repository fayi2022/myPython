#Function to count the total number of vowels in a string  
def countvowel(str):
    count=0
    for i in str:
        if i in 'aeiouAEIOU':
            count+=1
            print(i)
    print("Total number of characters which are vowels=",count)

mystr='fayisA'
countvowel(mystr)
