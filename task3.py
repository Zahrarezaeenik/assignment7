
def is_sort_ascending(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
    return True

arr=[1,2,4,6,7]
if is_sort_ascending(arr):
    print("sorted")
else:
    print("not sorted")

arr=[8,5,4,1,6,7]
if is_sort_ascending(arr):
    print("sorted")
else:
    print("not sorted")
        
