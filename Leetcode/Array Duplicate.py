from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrSize = len(nums)

        for i in range(arrSize):
            for j in range(i + 1, arrSize):
                if nums[i] == nums[j]: 
                    return True
        return False

# ---- Test cases ----
if __name__ == "__main__":
    solution = Solution()

    test1 = [1, 2, 3, 4]
    test2 = [1, 2, 3, 1]
    test3 = [5, 5, 6, 7]

    print(solution.hasDuplicate(test1))  # False
    print(solution.hasDuplicate(test2))  # True
    print(solution.hasDuplicate(test3))  # True
