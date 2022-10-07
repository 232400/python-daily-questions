n=int(input("enter the number:"))
x=n
while x>=10:
   sum=0
   while x>0:
      r=x%10
      sum=sum+(r*r)         
      x=x//10
   print("sum",sum)
   x=sum
if x==1:
    print(n,"x is a happy number")
else:
    print(n,"x is not a happy number")
