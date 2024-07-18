def isPermutation(string1, string2) :
	#Your code goes here

    l1 = len(string1)
    l2 = len(string2)
    if(l1!=l2):
        return "false"
    dst1 = {}
    dst2 = {}
    for i in range(len(string1)):
        if string1[i] not in dst1:
            dst1[string1[i]] = 1
        else:
            dst1[string1[i]] +=1
        if string2[i] not in dst2:
            dst2[string2[i]] = 1
        else:
            dst2[string2[i]] +=1
    for i in dst1:
        if i not in dst2:
            return "false"
        if dst1[i] != dst2[i]:
            return "false"
    else:
        return "true"
print(isPermutation("race", "rate")) 

        