class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        triplets = []
        for i in range(len(nums) - 1):
            if i > 0 and n[i] == n[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if n[l] + n[r] + n[i] > 0:
                    r -= 1
                elif n[l] + n[r] + n[i] < 0:
                    l += 1
                else:
                    triplets.append([n[i], n[l], n[r]])
                    l += 1
                    while l < r and n[l] == n[l - 1]:
                        l += 1
        return triplets

            
