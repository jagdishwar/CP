class Solution:
    def hotel(self, arrive, depart, K):
        events=[(t,1) for t in arrive]+[(t,0)for t in depart]
        events=sorted(events)
        active=0
        for event in events:
            if event[1]==1:
                active+=1
            else:
                active-=1
            if active>K:
                return 0
        return 1

"""Testing code """

s = Solution()
a = [1, 3 ,5]
d = [2 ,6 ,8]

print("####",s.hotel(a, d, 1))