        queue=[]
        error=[]
        s="(*))"
        for i in range(len(s)):
            if s[i] is "(":
                queue.append(i)
            if s[i] is "*":
                error.append(i)
            elif s[i] is ")":
                if len(queue)>0:
                    queue.pop()
                elif len(queue)==0 and len(error)>0 and error[-1]<i:
                    error.pop()
                else:
                    return False

        for i in reversed(queue):
            if len(error)>0 and i<error[-1]:
                error.pop()
                queue.pop()
list.re
        if queue==0:
            return True

        return False






