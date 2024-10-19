import re
class Solution:
    def reverseWords(self, s: str) -> str:

        s = re.sub(' +', ' ', s)
        tempList = s.split(" ")
        tempList.reverse()
        return " ".join(tempList).strip()

solution = Solution()
# solution.reverseWords('the sky is blue')
# print(solution.reverseWords("  hello world  "))
print(solution.reverseWords('a good   example'))
