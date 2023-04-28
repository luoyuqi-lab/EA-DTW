from cDTW import luo_dtw
from slice_series import sliceNrebuild
from partial_DTW import partial_dtw

def EA_DTW(t,s,n,r,e):
    epsilon = e
    rt,rs = sliceNrebuild(t,s,n,r)
    ind = []
    dis = 0
    for i in range(n):
        ind.append(rt[i][0])
    for i in range(n):
        #print(ind)
        ind1 = ind.index(max(ind))
        #print(ind1)
        if ind1 == 0:
            # print(rt[ind1],rs[ind1])
            pd = partial_dtw(rt[ind1][2:],rs[ind1][2:],r,location='front')
            dis += pd
            i+=1
            #print('f')
        elif ind1 == n-1:
            pd = partial_dtw(rt[ind1][2:],rs[ind1][2:],r,location='back')
            dis += pd
            i += 1
            #print('b')
        else:
            pd = partial_dtw(rt[ind1][2:],rs[ind1][2:], r, location='middle')
            dis += pd
            i += 1
            #print('m')
        #print('i value:',i)
        #print(dis)
        if dis < epsilon and i == n:
            epsilon = dis
            jud = 1
            # jud = 1 means it is best-so-far and replace previous epsilon
            return epsilon, jud
        elif dis < epsilon:
            ind[ind1] = -1
        else:
            # jud = 0 means it is a unpromising candidate
            jud = 0
            return epsilon,jud
