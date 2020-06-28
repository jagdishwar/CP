import functools
@functools.lru_cache()
def fibonaciiseries(n):
    if n==1 or n==2:
        return 1
    return fibonaciiseries(n-1)+fibonaciiseries(n-2)
print(fibonaciiseries(90))