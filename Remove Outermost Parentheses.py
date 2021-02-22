s="(()())(())"
box=[]
i=0
while i<len(s):
            stack=[s[i]]
            i+=1
            while stack:
                if i<len(s) and s[i]=='(':
                    stack.append(s[i])
                elif i<len(s) and s[i]==')':
                    stack.pop()
                print(i,s[i])
                i+=1
                print(stack)
            if len(stack)==0:
                box.append(i)
            i+=1