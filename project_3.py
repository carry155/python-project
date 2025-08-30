nums = [10,30,40,333,44,56]

frist = max(nums)

while frist in nums:
    nums.remove(frist)

if nums:
    second = max(nums)
    print("Second largest number is:", second)
else:
    print("No second largest number")