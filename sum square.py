a=int(input("enter the number of elements:"))
b=int(input("enter the elements:"))
l=b
def sumsquare(l):
    even=0
    odd=0
    for i in l:
        if i%2==0:
         even=even+i**2
        else:
            odd=odd+i**2
    l=[odd,even]
    return(l)
print(sumsquare(l))
