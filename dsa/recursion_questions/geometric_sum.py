n = int(input())
sm = 0

def gp(sm,power):
    if power == 0:
        sm += 1
        print("%.5f"%(sm))
        return
    
    sm += 1/(2**power)
    gp(sm,power-1 )

gp(sm,n)