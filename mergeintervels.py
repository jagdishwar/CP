def check_intervels_overlapping(i,merge_intervels):
    for i in range(i[0],i[1]+1):
        if i == merge_intervels[0] or i==merge_intervels[1]:
            return True
def mergeinterverls(intervels,merge_intervels):
                    output=[]
                    flag=False
                    for i in intervels:
                        for k in range(i[0], i[1]+ 1):
                            if k == merge_intervels[0] or k == merge_intervels[1]:
                                    flag=True
                                    merge_intervels=[min(i[0],merge_intervels[0]),max(i[1],merge_intervels[1])]
                        else:
                            if flag==False:
                                output.append(i)
                            else:
                                output.append(merge_intervels)
                                flag=False
                    return output

