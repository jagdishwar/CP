list1 = [ "-500", "-10", "/" ]
stack=[]
str1='-200'

for i in list1:
    if i not in ["*",'-','+','/']:
        stack.append(i)
    else:
        op1=int(stack.pop())
        op2=int(stack.pop())
        if i=="+":
            k=op2+op1
            stack.append(k)
        elif i=='-':
            k = op2 - op1
            stack.append(k)
        elif i=='*':
            k = op2 * op1
            stack.append(k)
        elif i=='/':
            k = op2 / op1
            stack.append(k)
print(stack)




