# User function Template for python3


class Solution:
    def compareFrac(self, str):

        # code here
        l = []
        m = []
        final = []
        l = str.split(',')
        for i in range(len(l)):
            l[i] = l[i].strip()

        for i in l:
            m = i.split('/')
            final.append(int(m[0]) / int(m[1]))

        if (final[0] == final[1]):
            return 'equal'
        else:
            return l[final.index(max(final))]


# {
# Driver Code Starts
# Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))
