from file_read import txtinput
from partition import partition
from slice_and_rebuild_list import part_contri
import timeit
from cDTW import luo_dtw
from slice_and_rebuild_list import sliceNrebuild

def partial_dtw(a,b,r,location=''):
    """
    :param a: full template series
    :param b: full sample series
    :param r: max warping window / extra window size
    :param location: the location of the sub-series in the full series
    :return:
    DO NOT MAKE extra window out of full time series! Like full series is [0:30], warping window is r = 5
    calculate partial_dtw [20:26] is not supported, because 26+5+1 over the size of full time series length，30 !
    By this way, [4:10] is also can not be calculate, because 4 - 5 - 1 less than 0 !
    """
    d, p = luo_dtw(a, b, r)
    E = []
    dis = d
    #print(d,p)
    if location == 'front':
        #print('f')
        for i in range(len(p)):
            if p[i][0]> len(a)-r-3:
                E.append(p[i])
                #print(a[p[i][0]],b[p[i][1]])
                #print(E)
                Euclidean_d = (a[p[i][0]]-b[p[i][1]])
                #print(Euclidean_d)
                dis = dis - (Euclidean_d*Euclidean_d)
                #print(dis)
    elif location == 'middle':
        #print('m')
        for i in range(len(p)):
            if p[i][0] < r+2 or p[i][0]> len(a)-r-3:
                E.append(p[i])
                # print(a[p[i][0]],b[p[i][1]])
                #print(E)
                Euclidean_d = (a[p[i][0]]-b[p[i][1]])
                #print(Euclidean_d)
                dis = dis - (Euclidean_d*Euclidean_d)
                #print(dis)
    else: # if location == 'back'
        #print('b')
        for i in range(len(p)):
            if p[i][0] < r+2:
                E.append(p[i])
                # print(a[p[i][0]],b[p[i][1]])
                Euclidean_d = (a[p[i][0]]-b[p[i][1]])
                #print(Euclidean_d)
                dis = dis - (Euclidean_d*Euclidean_d)
                #print(dis)
    #print(E)
    return dis

# a = [2,6,4,7,1,5,2,4,9,4,3,5,7,6,4,9,5,6,7,8,4,2,3,4,1,2,3,4,5,6]
# b = [3,6,7,5,2,2,4,8,8,7,5,4,1,2,5,5,2,9,4,3,8,5,1,2,6,7,7,8,9,2]
# a = [2,6,4,7,1,5,2,4,9,4,3,5,7,6,4,9,5,6,7,8,4,2,3,4, 1,2,3,4,5,6,9,5, 6,7,8,4,8,4,2,3]
# b = [3,6,7,5,2,2,4,8,8,7,5,4,1,2,5,5,2,9,4,3,8,5,1,2, 6,7,7,8,9,2,2,9, 4,3,8,5,4,1,2,5]
# x,y = sliceNrebuild(a,b,5,6)
# # # print(len(x),len(y))
# # # print(x[3])
# a1 = x[0][2:]
# b1 = y[0][2:]
# a2 = x[1][2:]
# b2 = y[1][2:]
# a3 = x[2][2:]
# b3 = y[2][2:]
# a4 = x[3][2:]
# b4 = y[3][2:]
# a5 = x[4][2:]
# b5 = y[4][2:]
# # # # a6 = x[5][2:]
# # # # b6 = x[5][2:]
# print("++++++++++++++++++++++++++++++++++++++++")
# d,p = luo_dtw(a,b,6)
# print(d,p)
# print("++++++++++++++++++++++++++++++++++++++++")
# # #print(a,b)
# r1 = partial_dtw(a1,b1,6,location='front')
# r2 = partial_dtw(a2,b2,6,location='middle')
# r3 = partial_dtw(a3,b3,6,location='middle')
# r4 = partial_dtw(a4,b4,6,location='middle')
# r5 = partial_dtw(a5,b5,6,location='end')
# print(r1,r2,r3,r4,r5,"result=",(r1+r2+r3+r4+r5) )
# print("++++++++++++++++++++++++++++++++++++++++")

# c = [4,2,3,4, 1,2,3,4,5,6,9,5, 6,7,8,4,8,4,2,3]
# d = [8,5,1,2, 6,7,7,8,9,2,2,9, 4,3,8,5,4,1,2,5]
# print(luo_dtw(c, d, 3))
# print(partial_dtw(c,d,3,location='end'))
# a1 = a[0:20]
# b1 = b[0:20]
# a2 = a[10:30]
# b2 = b[10:30]
#
# print(partial_dtw(b1,a1,5,location='front'))
# print(partial_dtw(b2,a2,5,location='back'))
# print(partial_dtw(b[5:25],a[5:25],5,location='middle'))
# print(len(b[5:25]))

# a1 = a[0:12]
# b1 = b[0:12]
#
# a2 = a[0:15]
# b2 = b[0:15]
#
# a3 = a[3:18]
# b3 = b[3:18]
#
# a4 = a[7:19]
# b4 = b[7:19]
#
#
# a5 = a[6:23]
# b5 = b[6:23]
#
# a6 = a[11:29]
# b6 = b[11:29]
#
# a7 = a[17:30]
# b7 = b[17:30]
# print(len(a3))
# start = timeit.default_timer()
# print(partial_dtw(b1,a1,5,location='front'))
# print(partial_dtw(b2,a2,5,location='middle'))
# print(partial_dtw(b3,a3,5,location='middle'))
# print(partial_dtw(b4,a4,5,location='middle'))
# print(partial_dtw(b5,a5,5,location='middle'))
# print(partial_dtw(b6,a6,5,location='middle'))
# print(partial_dtw(b7,a7,5,location='back'))
# end = timeit.default_timer()
# print((end-start),'second','value:')

# start = timeit.default_timer()
# luo_dtw(a,b,5)
# end = timeit.default_timer()
# print((end-start),'second','value:')

