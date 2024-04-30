import timeit
import math
import numpy as np


def luo_dtw(a, b, r, exp):
    """ Compute the DTW distance between 2 time series with a globel window constraint (max warping degree)
    :param a: the time series array 1, template, in x-axis direction
    :param b: the time series array 2, sample, in y-axis direction
    :param r: the size of Sakoe-Chiba warping band
    :return: the DTW distance cost_prev[k]
             path: the optimal dtw mapping path
             M: Warping matrix
             D: Distance matrix (by squared Euclidean distance)
    """
    M = []
    m = len(a)
    k = 0
    # Instead of using matrix of size O(m^2) or O(mr), we will reuse two arrays of size O(r)
    cost = [float('inf')] * (2 * r + 1)
    cost_prev = [float('inf')] * (2 * r + 1)
    for i in range(0, m):
        k = max(0, r - i)  # k is an index to control the recursion for every row with lens is (2 * r +1)
        for j in range(max(0, i - r), min(m - 1, i + r) + 1):
            # Initialize the first cell
            if i == 0 and j == 0:
                cost[k] = (a[0] - b[0]) ** exp  # Distance metric for two data points in template and sample series.
                k += 1
                continue
            # float('inf') infinite number, full outers of warping window by 'inf'
            y = float('inf') if j - 1 < 0 or k - 1 < 0 else cost[k - 1]
            x = float('inf') if i < 1 or k > 2 * r - 1 else cost_prev[k + 1]
            z = float('inf') if i < 1 or j < 1 else cost_prev[k]
            # Dynamic programming to construct the cost matrix
            cost[k] = min(x, y, z) + (a[i] - b[j]) ** exp  # current cell = minimum of 3 candidates + cell's distance
            # dis.append(d*d)
            k += 1
        # Move current array (cost matrix) to previous array
        cost_prev = cost
        c = cost_prev.copy()
        M.append(c)
        # D.append(dis)
        # dis = []
    # The DTW distance is in the last cell in the cost matrix of size O(m^2) or !!At the middle of our array!!
    i = m - 1
    j = r
    rj = len(b) - 1
    path = [[len(a) - 1, len(b) - 1]]
    k -= 1
    while i != 0 or rj != 0:  # DP from [n,m] to [0,0] in cost matrix to find optimal path
        x = M[i][j - 1] if j - 1 >= 0 else float('inf')  # candidate (i, j-1)
        y = M[i - 1][j] if i - 1 >= 0 else float('inf')  # candidate (i-1, j-1)
        z = M[i - 1][j + 1] if i - 1 >= 0 and j + 1 <= 2 * r else float('inf')  # candidate (i-1, j)
        # Save the real location index of optimal warping path point a_i mapping with point b_j.
        if min(x, y, z) == y:
            path_temp = [i - 1, rj - 1]
            i = i - 1
            rj = rj - 1
        elif min(x, y, z) == x:
            path_temp = [i, rj - 1]
            j = j - 1
            rj = rj - 1
        else:
            path_temp = [i - 1, rj]
            i = i - 1
            j = j + 1
        path.append(path_temp)
    return cost_prev[k], path
def assemble_extra_data(a, b, N, r):
    """
:param a: Time series a
:param b: Time series b
:param N: Divide time series into n parts.
:return: pairwise sub-series of n (number of slicing) time series partitions.
"""
    if len(a) == len(b):
        x = []
        y = []
        x1 = []
        y1 = []
        l = math.floor(len(a) / N)
        x.append(a[0:l])
        y.append(b[0:l])
        x1.append([0] + x[0] + a[l:l + r + 1])
        y1.append([0] + y[0] + b[l:l + r + 1])
        if N != 2:
            for i in range(1, N - 1):
                p = a[int(i * l): int((i + 1) * l)]
                x.append(p)
                p = b[int(0 + i * l): int((i + 1) * l)]
                y.append(p)
                x1.append([1] + a[i * l - (r + 1) :(i + 1) * l + r + 1])
                y1.append([1] + b[i * l - (r + 1) :(i + 1) * l + r + 1])
                i += 1
        x.append(a[(N - 1) * l:])
        y.append(b[(N - 1) * l:])
        x1.append([2] + a[(N - 1) * l - (r + 1): (N - 1) * l] + x[N - 1])
        y1.append([2] + b[(N - 1) * l - (r + 1): (N - 1) * l] + y[N - 1])
    else:
        print('Please align! Now we not support different time stamps.')
    return x1,y1

def PDTW(a,b,r):
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
    c = a[1:]
    d = b[1:]
    dis, p = luo_dtw(a[1:], b[1:], r, exp=2)
    E = []
    path = []
    #print(d,p)
    if a[0] == 0:
        #print('f')
        for i in range(len(p)):
            if p[i][0]> len(c)-r-2:
                E.append(p[i])
                #print(a[p[i][0]],b[p[i][1]])
                #print(E)
                Euclidean_d = (c[p[i][0]]-d[p[i][1]])
                #print(Euclidean_d)
                dis = dis - (Euclidean_d*Euclidean_d)
                #print(dis)
            else:
                path.append(p[i])
    elif a[0] == 1:
        for i in range(len(p)):
            if p[i][0] < r+1 or p[i][0]> len(c)-r-2:
                E.append(p[i])
                # print(a[p[i][0]],b[p[i][1]])
                #print(E)
                Euclidean_d = (c[p[i][0]]-d[p[i][1]])
                #print(Euclidean_d)
                dis = dis - (Euclidean_d*Euclidean_d)
                #print(dis)
            else:
                path.append(p[i])
    elif a[0] == 2:
        #print('b')
        for i in range(len(p)):
            if p[i][0] < r+1:
                E.append(p[i])
                # print(a[p[i][0]],b[p[i][1]])
                Euclidean_d = (c[p[i][0]]-d[p[i][1]])
                #print(Euclidean_d)
                dis = dis - (Euclidean_d*Euclidean_d)
                #print(dis)
            else:
                path.append(p[i])
    #print(E)
    return dis, path
def main():
    a = [2, 6, 4, 7, 1, 5, 2, 4, 9, 4, 3, 5, 7, 6, 4, 9, 5, 6, 7, 8, 4, 2, 3, 4, 1, 2, 3, 4, 5, 6]
    b = [3, 6, 7, 5, 2, 2, 4, 8, 8, 7, 5, 4, 1, 2, 5, 5, 2, 9, 4, 3, 8, 5, 1, 2, 6, 7, 7, 8, 9, 2]
    print(luo_dtw(a,b,4,exp=2))
    a ,b = assemble_extra_data(a,b,30,3)
    print(a,b,len(a),len(b))

if __name__ == '__main__':
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("Time:", end - start)
