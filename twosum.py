class Solution(object):
    def twoSum(self, nums, target):
        storage = {}

        for i in range(len(nums)):
            if target - nums[i] in storage:
                return [storage[target - nums[i]], i]
                
            else:
                storage[nums[i]] = i

            print(storage)

            
# nums = [2,7,11,15] 
# target = 9

nums = [3,2,4]
target = 6

# nums = [3,3]
# target = 6

sum = Solution()
sum.twoSum(nums ,target)

print(sum)

        