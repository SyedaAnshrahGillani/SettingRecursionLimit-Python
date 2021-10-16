import sys
def s(num):
    if num==1:
        return 1
    else:     
        return num+s(num-1)
print(s(4))
sys.setrecursionlimit(1)
def s(num):
    if num==1:
        return 1
    else:     
        return num+s(num-1)
print(s(4))


