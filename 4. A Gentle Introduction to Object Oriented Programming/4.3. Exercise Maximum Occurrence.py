def maximum_occurrence(x):
    y=set(x)
    z=list(y)
    a=[0]*len(y)
    for i in range(len(z)):
        a[i]=x.count(z[i])
    return z[a.index(max(a))]