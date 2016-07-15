class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = {}
        max1 = 0
        for index, value in enumerate(s):
            if value in tmp.values():
                for i in xrange(index, len(s)):
                    index1 = None
                    max2 = 0
                    if index1 is None:
                        index1 = self.getIndex(tmp, value)
                    # print(index1)
                    if s[i] == s[index1]:
                        index1 += 1
                        max2 += 1
                        continue
                    else:
                        max1 = max2
                        break
            tmp[index] = value
            # print tmp

        return max1

    def getIndex(self, dict, value):
        '''
        :param dict:
        :param value:
        :return int:
        '''
        for i in xrange(len(dict)):
            if dict[i] == value:
                return i

str1 = "aaaa"
s = Solution()
print s.lengthOfLongestSubstring(str1)