'''
# take01 5%
class Solution:
    def twoSum(self, nums, target):
        seq2 = -1
        for seq, one_num in enumerate(nums):
            try:
                seq2 = nums[seq+1:].index(target-one_num) + seq + 1
            except:
                pass 
            if seq2>-1:
                break 
        return [seq, seq2]
'''

# take02 使用 hashtable 做到了80%以上
class Solution:
    def twoSum(self, nums, target):
        tmp = {}
        for seq, one_num in enumerate(nums):
            target_num = target - one_num
            if target_num in tmp: 
                return [tmp[target_num], seq]

            if one_num not in tmp:
                tmp[one_num] = seq 

if __name__ == '__main__':
    test_sol = Solution()
    print(test_sol.twoSum([1,2,3,4,5],6) )
