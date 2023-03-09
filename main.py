def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return "Answer don't exist"

data = list(map(int,input("nums : ").split()))
val = int(input("target : "))
print(twoSum(data,val))
