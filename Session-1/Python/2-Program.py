# Given an array arr[]. Your task is to find the minimum and maximum elements in the array. 
class Solution:
    def findMinMax(self,arr):
        min = arr[0]
        max = arr[0]
        for num in arr:
            if num < min:
                min = num
            if num > max:
                max = num
        return [min, max]    
    

# Simple object creation and method call
obj = Solution()
arr = [1, 4, 3, 5, 8, 6,323,56,7,8,2,32,477,4,343,56,3,43,2,3,4,5,6,7,6,32,3,24]
result = obj.findMinMax(arr)

print("Minimum:", result[0])
print("Maximum:", result[1])    