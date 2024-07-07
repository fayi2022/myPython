#Program to input elements in tuple and to count and display number of even and odd numbers present in it using a function

def evenOddcount(tup):
    counteve=0
    countodd=0
    for i in tup:
        if i%2==0:
            counteve+=1
        else:
            countodd+=1
    return counteve,countodd

tupSample=()
n=int(input("Enter the number of elements in the tuple:"))
for i in range(n):
    print("Enter the th element ",i+1,":")
    num=int(input())
    tupSample=tupSample+(num,)
evencount,oddcount=evenOddcount(tupSample)
print("Number of Even digit:",evencount)
print("Number of Odd digit:",oddcount)
