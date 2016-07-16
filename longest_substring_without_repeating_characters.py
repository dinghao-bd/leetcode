# coding=utf-8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ''
        max_len = []
        if len(s) == 0:
            return 0
        else:
            for index, value in enumerate(s):
                if value not in tmp:
                    tmp += value
                    max_len.append(len(tmp))
                    continue
                else:
                    index1 = tmp.find(value)
                    tmp = tmp[index1+1:]
                    tmp += value
                    max_len.append(len(tmp))
                    continue

            return max(max_len)
