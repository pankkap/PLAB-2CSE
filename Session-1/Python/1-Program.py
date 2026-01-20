# You are given an array of integers arr[]. You have to reverse the given array. 
class Solution:
    def reverseArray(self, arr):
        # return arr[::-1]          # One line Solution
        left, right = 0, len(arr) - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr
    

# ---- EXECUTION PART ----
obj = Solution()
arr = [1, 2, 3, 4]
result = obj.reverseArray(arr)
print("Reversed Array:", result)    