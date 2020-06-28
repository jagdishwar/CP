s="abc"
shift=[[0,1],[1,2]]
def operation(shift,s):
    string=s
    for i in shift:
        string=shiftby(i[0],i[1],string)
    print(string)

def shiftby(shift,by,s):
    le=len(s)
    div=0
    if shift==1:
        div=le-by
    else:
        div=by
    left_part=s[:div][::-1]
    right_part=s[div:][::-1]
    s=(left_part+right_part)[::-1]
    return s

operation(shift,s)
