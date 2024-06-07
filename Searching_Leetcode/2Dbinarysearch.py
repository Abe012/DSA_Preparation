arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def twod_bs(arr,target):
    lm=len(arr)
    if lm==0:
        return False
    ln=len(arr[0])
    l,r=0,lm*ln-1
    while(l<=r):
        m=l+(r-l)//2
        mid=arr[m//ln][m%ln]
        if mid==target:
            return True
        elif target < mid:
            r=m-1
        else:
            l=m+1
    return False

x=twod_bs(arr,100)
y=twod_bs(arr,10)
print(x,y)