import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph, banned):
        replaced_paragraph = re.sub('[^a-zA-Z\s]', ' ', paragraph)
        # [^a-zA-Z\s] -> [^\W]
        print(replaced_paragraph)
        preprocessing_paragraph = [word for word in replaced_paragraph.lower().split() if word not in banned]

        result = Counter(preprocessing_paragraph).most_common(1)
        return result[0][0]


if __name__ == "__main__":
    solution = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."; banned = ["hit"]
    res = solution.mostCommonWord(paragraph, banned)
    print(res)

