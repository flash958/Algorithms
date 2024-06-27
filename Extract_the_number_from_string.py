class Solution:
    def ExtractNumber(self, sentence):
        # code here
        l = sentence.split(' ')

        number = []
        for i in l:
            try:
                s = int(i)
            except:
                pass
            else:
                number.append(i)

        final = []
        for i in number:
            if '9' not in i:
                final.append(int(i))

        if (len(final) == 0):
            return -1
        else:
            return max(final)


# {
# Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)
