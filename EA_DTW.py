from file_read import *
from slice_and_rebuild_list import sliceNrebuild
from cDTW import luo_dtw
from partial_dtw_dis import partial_dtw
from partition import partition
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
            return epsilon, jud
        elif dis < epsilon:
            ind[ind1] = -1
        else:
            jud = 0
            return epsilon,jud

# a = [2,6,4,7,1,5,2,4,9,4,3,5,7,6,4,9,5,6,7,8,4,2,3,4,1,2,3,4,5,6,9,5,6,7,8,4,8,4,2,3]
# b = [3,6,7,5,2,2,4,8,8,7,5,4,1,2,5,5,2,9,4,3,8,5,1,2,6,7,7,8,9,2,2,9,4,3,8,5,4,1,2,5]
# print(len(a))
# print(luo_dtw(a,b,3))
# e,j = EA_DTW(a,b,5,3,500)
# print(e,j)

# data_raw = txtinput_c(r'C:\Users\luoyu\OneDrive\桌面\Coffee.txt')
# data_c1 = []
# data_c2 = []
# for i in range(len(data_raw)):
#     if data_raw[i][0] == 0:
#         data_c1.append(data_raw[i][1:])
#         i += 1
#     else:
#         data_c2.append(data_raw[i][1:])
#         i += 1
#
# t1 = data_c1[1]
# t2 = data_c2[1]
# s = data_c1[0]
# d, p = luo_dtw(t2,s,28)
# print(d)
# print(EA_DTW(t2,s,9,28,3))





