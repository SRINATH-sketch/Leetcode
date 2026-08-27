class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        s=[]
        for i in tokens:
            if i not in "/*-+":
                s.append(int(i))
            else:
                right=s.pop()
                left=s.pop()
                if i=='+':
                    s.append(left+right)
                elif i=='-':
                    s.append(left-right)
                elif i=='*':
                    s.append(left*right)
                else:
                    s.append(int(left/right))
        return s.pop()