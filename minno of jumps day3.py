def minjump(arr,l,h):
     if(h==1):
        return 0
    if(arr[1] ==0):
        return float(inf)
    min=float('inf')
    for i in range(l+1,h+1):
        if(i<1+arr[l]+1):
           jump=minjump(arr,i,h)
           if(jump!=float(inf)&jump+1<min):
               min=jump+1
    return min
arr=[1,2,6,5,3,4,8,9,4,7,8,5,2,0,3]
n=len(arr)
print('minium number of jump to reach','ends is',minjump(arr,0,n-1))
   
