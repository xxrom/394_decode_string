class Solution:

  def calc(self, index=0) -> str:
    innerIndex = index
    resultStr = ''
    number = ''

    while innerIndex < len(self.fullString):
      char = self.fullString[innerIndex]
      innerIndex += 1

      # print('char %s, number %s, result %s' % (char, str(number), resultStr))

      if char == '[':
        # Go dipper inside
        newIndex, returnStr = self.calc(innerIndex)

        innerIndex = newIndex
        resultStr += int(number) * returnStr
        number = ''

      elif char == ']':
        # Return current index and state
        number = ''
        return innerIndex, resultStr

      else:
        if char.isalpha():
          # >aaa< 3[aaa]
          resultStr += char

        elif isinstance(int(char), int):
          # >3< [a]
          number += char

    return innerIndex, resultStr

  def decodeString(self, s: str) -> str:
    self.fullString = s
    index, ans = self.calc()
    return ans


my = Solution()
# n = "3[a]2[bc]"  # "aaabcbc"
# right = "aaabcbc"
# n = "3[a2[c]]"  # "accaccacc"
# right = "accaccacc"
# n = "2[abc]3[cd]ef"  # "accaccacc"
# right = "abcabccdcdcdef"

n = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
right = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
# ttttt = 'zzzyypqjkjkefefjkjkefefjkjkefefjkjkefefyypqjkjkefefjkjkefefjkjkefefjkjkefef'

ans = my.decodeString(n)
print("ans", ans)
print(ans == right)

# todo: tree with finding leaf and returning result from leafs to root
# should be simple asF

# 3[a2[c]]
# 3 - number
# [ - open
# a - string
# 2 - int => resultStr += number * string

# Runtime: 20 ms, faster than 98.30% of Python3 online submissions for Decode String.
# Memory Usage: 13.8 MB, less than 5.77% of Python3 online submissions for Decode String.
