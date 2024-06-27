l=[50,10,40,30,70]

def bubble_sort(l):
    for j in range(len(l)-1):
        swap = 0
        for i in range(len(l) - j -1):
            if (l[i] > l[i + 1]):
                l[i], l[i + 1] = l[i + 1], l[i]
                #print(l[i])
                #print(l[i + 1])
                swap = 1
        if(swap==0):  #Swap check (To optimize this algorithm)
            break

    return l

print(bubble_sort(l))


