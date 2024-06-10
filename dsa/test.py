a = [8, 6, 2, 5, 1]
for i in range (len(a)-1):
    mp = i
    for j in range(i+1,len(a)):
        if a[mp] < a[j]:
            mp = j
    a[mp],a[i] = a[i],a[mp]
print(a)

