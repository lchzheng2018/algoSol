
def maxNoadjSum(nums):
  """
  :type nums: List[int]
  """
  
  n = len(nums)
  if n == 0:
    return -1

  if n == 1:
    return nums[0]
  
  maxs = [0] * n
  maxs[0] = nums[0]
  maxs[1] = max(nums[0], nums[1]) 
  for i in range(2, n):
    maxs[i] = max(nums[i] + maxs[i - 2], maxs[i - 1])

  print maxs
  return maxs[n - 1]


"""
quick unit test
"""
nums = [1, 0, 3, 9, 2]
print nums
print maxNoadjSum(nums)

"""
Console output:
[1, 0, 3, 9, 2]
[1, 1, 4, 10, 10]
10
"""
