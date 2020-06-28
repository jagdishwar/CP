def dfspermutations(output,visitindex,str1,combination):
    if len(combination)==len(str1):
        output.append(''.join(combination[:]))
        return
    for i in range(len(str1)):
        if i not in visitindex:
            visitindex.add(i)
            combination.append(str1[i])
            dfspermutations(output,visitindex,str1,combination)
            visitindex.remove(i)
            combination.pop()

def checkindict(output,dictset,i):
    validcom=[]
    str12='valid words from dictornary'
    list1=['valid words from dictornary']
    validcom.append(str12)
    for i in output:
        if i in dictset:
            validcom.append(' '+ i)
    if validcom == list1:
        return
    else:
        validcom.append(' are combination from '+str(i)+' word from given list')
        result=''.join(validcom)
        print(result)


#enter the new words in this list1
list1=['tac','abc','vac','cad','atr']
#add a new dictionary words
dictset={'cat','dog','act','mad','rat'}
for i in range(len(list1)):
        output=[]
        str1=list1[i]
        visitindex=set()
        dfspermutations(output,visitindex,str1,[])
        checkindict(output,dictset,list1[i])
