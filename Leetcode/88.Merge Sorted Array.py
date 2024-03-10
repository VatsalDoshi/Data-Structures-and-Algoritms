num1 = [1,2,3,0,0,0]
num2= [2,5,6]

num1.extend(num2)
num1.sort()
print(num1)

def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    
    # Set the pointer for the merged array (nums1) to the end
    p = m + n - 1
    
    # Merge the two arrays in reverse order
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If there are remaining elements in nums2, copy them to nums1
    nums1[:p2 + 1] = nums2[:p2 + 1]

# Example usage
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)
