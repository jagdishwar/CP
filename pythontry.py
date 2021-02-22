set1=set()
strx=input()
for i in strx:
      if i in set1:
          return False
      set1.add(i)

return True


