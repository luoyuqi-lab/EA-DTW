from partition import partition
from partition import part_contri

def sliceNrebuild(a,b,n,r):
    x,y = partition(a,b,n)
    x1, y1= [],[]
    #ind = []
    for i in range(n):
        if i == 0:
            x1.append([part_contri(x[i], y[i])]+[0]+x[i]+x[i+1][0:r+1]) # reconstruct structure is part-contribution(x[0])
                                                                        # + sublist location(in location x[1], value 0 is front, 1 is middle,
                                                                        # 2 is end) + new list (r+1 + list + r+1)
            y1.append([part_contri(x[i], y[i])]+[0]+y[i] + y[i + 1][0:r + 1])
            #ind.append(part_contri(x[i], y[i]))
            i += 1
        elif i == n-1:
            x1.append([part_contri(x[i], y[i])]+[2]+x[i - 1][-(r+1):]+x[i])
            y1.append([part_contri(x[i], y[i])]+[2]+y[i - 1][-(r+1):]+y[i])
            #ind.append(part_contri(x[i], y[i]))
            i += 1
        else:
            x1.append([part_contri(x[i], y[i])]+[1]+x[i - 1][-(r + 1):]+x[i]+ x[i + 1][0:r+1])
            y1.append([part_contri(x[i], y[i])]+[1]+y[i - 1][-(r + 1):]+y[i]+ y[i + 1][0:r + 1])
            i += 1
    return x1,y1
