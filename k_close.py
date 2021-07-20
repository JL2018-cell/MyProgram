def binary(nums, x):
 start = 0
 end = len(nums) - 1
 while start <= end:
  mid = start + ((end - start) // 2)
  if nums[mid] < x:
   start = mid + 1
  elif nums[mid] > x:
   end = mid - 1
  else:
   return mid
 return -1

def k_close(nums, x, k):
 no = binary(nums, x)
 if no == -1:
  return []
 else:
  lhs = no - 1
  rhs = no
  while k > 0:
   if lhs < 0 or (rhs < len(nums) and abs(nums[lhs] - x) > abs(nums[rhs] - x)):
    rhs = rhs + 1
   else:
    lhs = lhs - 1
   k = k - 1
  return nums[lhs + 1: rhs]

nums = [1,2,3,4,5,6,7,8,9,10]
print(k_close(nums, 100, 4))


