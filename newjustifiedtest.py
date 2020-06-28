words=["This", "is", "an", "example", "of", "text", "justification."]
maxwidth=16
result=[]
cur=[]
lenwords=0
for w in words:
    if lenwords+len(cur)+len(w)>maxwidth:
        if len(cur)==1:
            result.append(cur[0]+' '*(maxwidth-lenwords))
        else:
            num_spaces=maxwidth - lenwords
            space_between_words,extra=divmod(num_spaces,len(cur)-1)

            for i in range(extra):
                cur[i]+=' '
            result.append((' '*space_between_words).join(cur))
        cur=[]
        lenwords=0
    cur.append(w)
    lenwords+=len(w)
print (result)