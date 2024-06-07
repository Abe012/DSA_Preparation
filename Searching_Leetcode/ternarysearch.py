list1=[20,24,26,30,45,67,68,79,80,83,90]
def ternary_search(arr,start,end,target):
    mid1=start+(end-start)//3
    mid2=end-(end-start)//3
    while(start<=end):
        if arr[mid1]==target:
            return mid1
        elif arr[mid2]==target:
            return mid2
        elif target<arr[mid1]:
            return ternary_search(arr,start,mid1-1,target)
        elif target>arr[mid2]:
            return ternary_search(arr,mid2+1,end,target)
        else:
            return ternary_search(arr,mid1+1,mid2-1,target)
    return -1
start=0
end=len(list1)-1
print(end)
target=90
print(ternary_search(list1,start,end,target))