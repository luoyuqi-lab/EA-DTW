import math

from PDTW import *


def Full_DTW(a,b,N,r):
    dis = 0
    path = []
    a1, b1 = assemble_extra_data(a,b,N,r)
    l = math.floor(len(a) / N)
    for i in range(N):
        d, p = PDTW(a1[i],b1[i],r)
        p.reverse()
        if i == 0:
            path += p
        else:
            path += [[k+(l-r-1)+(i-1)*l, j+(l-r-1)+(i-1)*l] for [k,j] in p]
        i += 1
        dis += d
    path.reverse()
    return dis, path

if __name__ == '__main__':
    a = [2, 6, 4, 7, 1, 5, 2, 4, 9, 4, 3, 5, 7, 6, 4, 9, 5, 6, 7, 8, 4, 2, 3, 4, 1, 2, 3, 4, 5, 6]
    b = [3, 6, 7, 5, 2, 2, 4, 8, 8, 7, 5, 4, 1, 2, 5, 5, 2, 9, 4, 3, 8, 5, 1, 2, 6, 7, 7, 8, 9, 2]
    print(assemble_extra_data(a,b,5,3))
    print(Full_DTW(a,b,10,2))
    print(luo_dtw(a,b,2,exp=2))
# print(PDTW(a1[1],b1[1],3))
# d,p=PDTW(a1[1],b1[1],3)
# print([[1+(6)+(i-1)*l, j+(l-r-1)+(i-1)*l] for [i,j] in p])