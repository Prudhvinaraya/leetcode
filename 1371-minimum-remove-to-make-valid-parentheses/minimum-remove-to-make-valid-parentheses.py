class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        i = 0
        count = 0
        list_ = []
        while(i < len(s)):
            if s[i] == '(':
                count+= 1
                list_.append(i)
            if s[i] == ')':
                if count > 0:
                    del list_[0]
                    count -= 1
                    #print(i,count)
                else:
                    del s[i]
                    i -= 1
        
            i += 1
            #print(s)
        for i in range(count):
            del s[list_[i]-i]
        #print("".join(s))
        return "".join(s)