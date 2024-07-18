class Solution:
    def reverseVowels(self, s: str) -> str:
        head = 0
        tail = len(s)-1
        res = [0]*len(s)
        i=0
        '''
        while i < len(s):
            # print(f"value of i:{i}")
            print(f"Value of head:{head} tail: {tail} s[head]:{s[head]} s[tail]: {s[tail]} res:{res}")
            if s[head] in 'aeiou' or s[head] in 'AEIOU':
                if s[tail] in 'aeiou' or s[tail] in 'AEIOU':
                    res[head]=s[tail]
                    res[tail]=s[head]
                    head+=1
                    tail-=1
                else:

                    tail-=1

            else:
                # print(f"At 1: Value of i:{i}")
                res[i]=s[i]
                head+=1


            i+=1
        '''
        while tail>=head:
            if s[head] in 'aeiou' or s[head] in 'AEIOU':
                if s[tail] in 'aeiou' or s[tail] in 'AEIOU':
                    res[head]=s[tail]
                    res[tail]=s[head]
                    head+=1
                    tail-=1
                else:
                    res[tail]=s[tail]
                    tail-=1
            else:
                res[head] = s[head]
                head+=1



        return "".join(str(res))

solution = Solution()
temp = solution.reverseVowels('hello')
