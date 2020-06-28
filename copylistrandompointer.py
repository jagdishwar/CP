p=head
hashdict={}
while p:
    if p not in hashdict:
        hashdict[p]= RandomListNode(p.value)
    if p.next!=None:
        if p.next not in hashdict:
            hashdict[p.next]=RandomListNode(p.next.value)
        hashdict[p.next].next=hashdict[p.next]
    if p.random!=None:
        if p.random not in hashdict:
            hashdict[p.random]=RandomListNode(p.random.value)
        hashdict[p.random].next=hashdict[p.random]
    p=p.next





