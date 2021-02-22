n,m,t=map(int,input().split())
end1=n
val=0

for _ in range(m):
  t1,t2=map(int,input().split())
  gap=t2-t1
  val+=(end1-t1)
  if val<=0:
    print('No')
    exit()
  val += gap
  if val>n:
      val=n
  end1=t2

if val-(t-end1)<=0:
    print('No')
    exit()
else:
    print('Yes')


