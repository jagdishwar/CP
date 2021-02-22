stack=[1,2,3,4,5]
n=len(stack)
list1=[]
def deploy(i):
    if n<=i:
        return 0

    ele=stack.pop()

    k=max(deploy(i+1)-ele,ele)
    print(k)
    return k




deploy(0)
