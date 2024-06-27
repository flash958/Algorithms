l=[50,10,40,30,70]

def selection_sort(l):

    for i in range(len(l)):
        min = l[i]
        ind = i
        for j in range(i,len(l)):
            if(l[j]<=min):
                min,ind=l[j],j  # Selecting Minimum element from the subarrray
        l[i],l[ind]=l[ind],l[i]


    return l

print(selection_sort(l))

