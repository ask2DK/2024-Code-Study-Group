
'''
투 포인터로 합 계산


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        # i가 최대 값일 때 left, right가 존재하기 위해서 -2
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results
        

'''

'''

Time Limit Exceeded
- O(n^3)...

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <=3 : return [nums] if sum(nums)==0 else []
        ans = {}

        for target_idx in range(len(nums)-2):

            for left in range(target_idx+1,len(nums)-1):

                for right in range(left+1,len(nums)):
                    if nums[target_idx]+nums[left]+nums[right] ==0 :
                        key = str(sorted([nums[target_idx],nums[left],nums[right]]))
                        if key in ans : continue
                        ans[key]=[nums[target_idx],nums[left],nums[right]]
        
        return ans.values()        
'''