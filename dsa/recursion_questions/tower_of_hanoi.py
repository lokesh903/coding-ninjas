# def towerofhanoi(n, source, aux, dest):
#     # Please add your code here
#     pass

# n=int(input())
# towerofhanoi(n, 'a', 'b', 'c')
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# Driver code
N =int(input())

# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

# best refrence video https://youtu.be/YstLjLCGmgg
