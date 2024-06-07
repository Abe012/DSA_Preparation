a=[1,2,3,4,5,6,6,6,6,6,6,6,6]
l=0
r=len(a)-1
print('r',r)
t=6

def b_search(a,l,r,t):
    while(l<=r):
        mid = (l+r)//2
        print('m',mid)
        if(a[mid]==t and a[mid]!=a[mid-1]):
            return mid
        elif (a[mid]<t):
            l=mid+1
        elif (a[mid]>=t and a[mid-1]==t ):
            r=mid-1
    return -1
print(b_search(a,l,r,t))

