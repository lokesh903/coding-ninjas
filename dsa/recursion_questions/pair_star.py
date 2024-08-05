st = input()

def pairStar(pre,st):
    if len(st) == 1:
        print(st[0],end='')
        return
    if (pre == st[0]):
        print("*",end='')
        pairStar('',st)
    else:
        print(st[0],end='')
        pairStar(st[0],st[1::])
pairStar('',st)