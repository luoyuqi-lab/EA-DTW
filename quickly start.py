from cDTW import luo_dtw
from EA_DTW import EA_DTW
from slice_series import sliceNrebuild

a = [2,6,4,7,1,5,2,4,9,4,3,5,7,6,4,9,5,6,7,8,4,2,3,4,1,2,3,4,5,6]
b = [3,6,7,5,2,2,4,8,8,7,5,4,1,2,5,5,2,9,4,3,8,5,1,2,6,7,7,8,9,2]

# dis,path =luo_dtw(b, a, 5)
# print(dis,path)

# ep, suc = EA_DTW(a,b,2,5,91)
# print(ep)
# print(suc)

# ep, suc = EA_DTW(a,b,2,5,88)
# print(ep)
# print(suc)

# print(sliceNrebuild(a,b,3,5))