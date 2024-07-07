#Function accepting a list and displaying the sum of elements ending with the digit 6

def sum3(L):
    sumnum=0
    for i in L:
        if i%10==6:
            sumnum+=i
    print("List:",L)
    print("Sum of elements ending with the digit 6:",sumnum)

L=[26,18,256,12,6]
sum3(L)
            
