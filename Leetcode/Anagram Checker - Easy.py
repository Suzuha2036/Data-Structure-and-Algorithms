class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        for i in range(len(s)):
            if s_sorted != t_sorted:
                return False
        
        return True
        


# ---- Test cases ----
if __name__ == "__main__":
    solution = Solution()

    s1, t1 = "racecar", "carrace"
    s2, t2 = "jar", "jam"
    s3, t3 = "nice", "nicer"

    print(solution.isAnagram(s1, t1))  # True
    print(solution.isAnagram(s2, t2))  # False
    print(solution.isAnagram(s3, t3))  # False
