def binarysearch(length,des):
    i=0
    l=len(length)-1
    while i<=l:
        mid= (l+i)//2
        if length[mid]==des:
            print(mid)
            break
        elif des > length[mid]: i=mid+1
        elif des < length[mid]: l=mid-1

def mergesort(lisst):
    if len(lisst)>1:
        mid = len(lisst)/2
        l= lisst[:mid]
        r=lisst[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                lisst[k]=l[i]
                i+=1
            else:
                lisst[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            lisst[k]=l[i]
            i+=1
            k+=1
        while j < len(r):
            lisst[k]=r[j]
            j+=1
            k+=1
    print(lisst)



tt=[23,44,22,33,45,324,32,234,34,22]
mergesort(tt)
