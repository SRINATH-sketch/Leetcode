class Solution:
    def interpret(self, command: str) -> str:
        final=""
        for i in range(len(command)):
            if((command[i]=='(' and command[i+1]==')')):
                final+='o'
            elif(command[i]=='(' and command[i+1]!=')'):
                continue
            elif((command[i]==')' and command[i-1]=='(')):
                continue
            elif(command[i]==')' and command[i-1]!='('):
                continue
            else:
                final+=command[i]
        return final