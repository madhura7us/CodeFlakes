# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

def findpos(arr, target):
    idx = 0
    for item in arr:
        if item <= target:
            idx +=1
    return idx

def searchInsert(arr, target):
    
        if target in arr:
            for i in range(len(arr)):
                if arr[i] == target:
                    print("Eq")
                    return i
                
        else:
            q = findpos(arr, target)
            return q
