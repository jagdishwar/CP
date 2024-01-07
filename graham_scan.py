##graham scan
from collections import deque
import math
points=[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]


def fp_nxtpts(points):
    points.sort(key=lambda x: (x[0], x[1]))
    return points[0], points[1:]


def slope(p1, p2):
    return 1.0 * ((p2[1] - p1[1]) / (p2[0] - p1[0])) if p2[0] != p1[0] else float('inf')


def dist(p1, p2):
    return math.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)


def cross_product(x, y):
    ans = x[0] * y[1]
    ans -= y[0] * x[1]
    return ans


def isitleftrightturn(p1, p2, p3):
    vectx_p1p2 = p2[0] - p1[0]
    vecty_p1p2 = p2[1] - p1[1]
    vectx_p2p3 = p3[0] - p2[0]
    vecty_p2p3 = p3[1] - p2[1]
    if cross_product([vectx_p1p2, vecty_p1p2], [vectx_p2p3, vecty_p2p3]) >= 0:
        return False
    return True


p0, points = fp_nxtpts(points)
points = [(p, slope(p0, p)) for p in points]
points.sort(key=lambda x: x[1])
i = 0
graham_points = []
for j in range(1, len(points)):
    if points[j][1] != points[i][1]:
        if j - i == 1:
            graham_points.append(points[i])
        else:
            nxt_points = sorted(points[i:j], key=lambda x: dist(p0, x[0]))
            graham_points.extend(nxt_points)
        i = j

nxt_points = sorted(points[i:], key=lambda x: -dist(p0, x[0]))
graham_points.extend(nxt_points)
points = [p[0] for p in graham_points]

ans = [p0]
for i in range(len(points)):
    ans.append(points[i])
    while len(ans) > 2 and isitleftrightturn(ans[-3], ans[-2], ans[-1]):
        ans.pop(-2)

print(ans)



