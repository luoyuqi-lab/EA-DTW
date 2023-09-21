from partition import partition
from partition import part_contri


a = [2,6,4,7,1,5,2,4,9,4,3,5,7,6,4,9,5,6,7,8,4,2,3,4,1,2,3,4,5,6]
b = [3,6,7,5,2,2,4,8,8,7,5,4,1,2,5,5,2,9,4,3,8,5,1,2,6,7,7,8,9,2]

def sliceNrebuild(a,b,n,r):
    x,y = partition(a,b,n)
    x1, y1= [],[]
    #ind = []
    for i in range(n):
        if i == 0:
            x1.append([part_contri(x[i], y[i])]+[0]+x[i]+x[i+1][0:r+2]) # reconstruct structure is part-contribution(x[0])
                                                                        # + sublist location(in location x[1], value 0 is front, 1 is middle,
                                                                        # 2 is end) + new list (r+2 + list + r+2)
            y1.append([part_contri(x[i], y[i])]+[0]+y[i] + y[i + 1][0:r +2])
            #ind.append(part_contri(x[i], y[i]))
            i += 1
        elif i == n-1:
            x1.append([part_contri(x[i], y[i])]+[2]+x[i - 1][-(r+2):]+x[i])
            y1.append([part_contri(x[i], y[i])]+[2]+y[i - 1][-(r+2):]+y[i])
            #ind.append(part_contri(x[i], y[i]))
            i += 1
        else:
            x1.append([part_contri(x[i], y[i])]+[1]+x[i - 1][-(r +2):]+x[i]+ x[i + 1][0:r+2])
            y1.append([part_contri(x[i], y[i])]+[1]+y[i - 1][-(r +2):]+y[i]+ y[i + 1][0:r +2])
            #ind.append(part_contri(x[i], y[i]))
            i += 1
    # ind = part_contri(a,b)
    # for i in range(n):
    #     x1[0].insert(0,ind[0])
    #     y1[0].insert(0,ind[0])
    return x1,y1,#ind

# print(a)
# print(b)
# print(partition(a, b, 4))
# rt,rs = sliceNrebuild(a,b,4,2)
# print(rt)
# print(rs)


