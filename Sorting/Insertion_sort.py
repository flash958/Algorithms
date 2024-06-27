#l=[50,10,40,-1,100,30,70,0]
l=[6,5,4,3,2,1]
def insertion_sort(l):
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if(l[j]<l[j-1]):
                l[j],l[j-1]=l[j-1],l[j]
            else:
                break
    return


print(insertion_sort(l))




