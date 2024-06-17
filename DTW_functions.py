import timeit
import math


# Description: This file contains the implementation of the DTW algorithm with global window constraint.
def luo_dtw(a, b, r, exp, return_path=False):
    """ Compute the DTW distance between 2 time series with a global window constraint (max warping degree)
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
    cost = [float('inf')] * (2 * r + 1)
    cost_prev = [float('inf')] * (2 * r + 1)
    for i in range(0, m):
        k = max(0, r - i)
        for j in range(max(0, i - r), min(m - 1, i + r) + 1):
            # Initialize the first cell
            if i == 0 and j == 0:
                cost[k] = (a[0] - b[0]) ** exp
                k += 1
                continue
            y = float('inf') if j - 1 < 0 or k - 1 < 0 else cost[k - 1]
            x = float('inf') if i < 1 or k > 2 * r - 1 else cost_prev[k + 1]
            z = float('inf') if i < 1 or j < 1 else cost_prev[k]
            cost[k] = min(x, y, z) + (a[i] - b[j]) ** exp
            k += 1
        # Move current array (cost matrix) to previous array
        cost_prev = cost
        if return_path:
            M.append(cost_prev.copy())
    # The DTW distance is in the last cell in the cost matrix of size O(m^2) or !!At the middle of our array!!
    if return_path:
        i = m - 1
        j = r
        rj = m - 1
        path = [[m - 1, m - 1]]
        k -= 1
        while i != 0 or rj != 0:
            # From [n,m] to [0,0] in cost matrix to find optimal path
            x = M[i][j - 1] if j - 1 >= 0 else float('inf')
            y = M[i - 1][j] if i - 1 >= 0 else float('inf')
            z = M[i - 1][j + 1] if i - 1 >= 0 and j + 1 <= 2 * r else float('inf')
            # Save the real location index of optimal warping path point a_i mapping with point b_j.
            if min(x, y, z) == y:
                path.append([i - 1, rj - 1])
                i = i - 1
                rj = rj - 1
            elif min(x, y, z) == x:
                path.append([i, rj - 1])
                j = j - 1
                rj = rj - 1
            else:
                path.append([i - 1, rj])
                i = i - 1
                j = j + 1
        return cost_prev[k], path
    else:
        return cost_prev[k - 1]


def assemble_extra_data(a, b, N, r):
    """
:param a: Time series a
:param b: Time series b
:param r: warping window size in CDTW
:param N: Divide time series into n parts.
:return: pairwise subsequences of n (number of slicing) time series partitions.
"""
    x, y = [], []
    x1, y1 = [], []
    if len(a) == len(b):
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
                x1.append([1] + a[i * l - (r + 1):(i + 1) * l + r + 1])
                y1.append([1] + b[i * l - (r + 1):(i + 1) * l + r + 1])
                i += 1
        x.append(a[(N - 1) * l:])
        y.append(b[(N - 1) * l:])
        x1.append([2] + a[(N - 1) * l - (r + 1): (N - 1) * l] + x[N - 1])
        y1.append([2] + b[(N - 1) * l - (r + 1): (N - 1) * l] + y[N - 1])
    else:
        print('Please align! Now we do not support different time stamps.')
    return x1, y1


def pdtw(a, b, r):
    """
    :param a: full template series
    :param b: full sample series
    :param r: max warping window / extra window size
    :return:
    """
    c = a[1:]
    d = b[1:]
    dis, p = luo_dtw(a[1:], b[1:], r, exp=2, return_path=True)
    E = []
    path = []
    for i in range(len(p)):
        Euclidean_d = (c[p[i][0]] - d[p[i][1]])
        if a[0] == 0 and p[i][0] > len(c) - r - 2:
            E.append(p[i])
            dis -= Euclidean_d * Euclidean_d
        elif a[0] == 1 and (p[i][0] < r + 1 or p[i][0] > len(c) - r - 2):
            E.append(p[i])
            dis -= Euclidean_d * Euclidean_d
        elif a[0] == 2 and p[i][0] < r + 1:
            E.append(p[i])
            dis -= Euclidean_d * Euclidean_d
        else:
            path.append(p[i])
    return dis, path


def assemble_extra_data_overflow(a, b, N, r):
    """
    :param a: Time series a
    :param b: Time series b
    :param N: Divide time series into n parts.
    :return: pairwise subsequence of n (number of slicing) time series partitions.
    """
    l = math.floor(len(a) / N)
    x, y = [], []
    x1, y1 = [], []
    if len(a) == len(b):
        l = math.floor(len(a) / N)
        x.append(a[0:l])
        y.append(b[0:l])
        x1.append([0] + x[0] + a[l:l + r + 1])
        y1.append([0] + y[0] + b[l:l + r + 1])
        if N != 2:
            d = (r + 1) / l
            for i in range(1, N - 1):
                p = a[int(i * l): int((i + 1) * l)]
                x.append(p)
                p = b[int(0 + i * l): int((i + 1) * l)]
                y.append(p)
                if i < d + 1:
                    x1.append([1.1] + a[0:(i + 1) * l + r + 1])
                    y1.append([1.1] + b[0:(i + 1) * l + r + 1])
                elif (len(a)-(i+1)*l) < r+1:
                    x1.append([1.2] + a[i * l - (r + 1):])
                    y1.append([1.2] + b[i * l - (r + 1):])
                else:
                    x1.append([1] + a[i * l - (r + 1):(i + 1) * l + r + 1])
                    y1.append([1] + b[i * l - (r + 1):(i + 1) * l + r + 1])
                i += 1
        x.append(a[(N - 1) * l:])
        y.append(b[(N - 1) * l:])
        x1.append([2] + a[(N - 1) * l - (r + 1): (N - 1) * l] + x[N - 1])
        y1.append([2] + b[(N - 1) * l - (r + 1): (N - 1) * l] + y[N - 1])
    else:
        print('Please align! Now we not support different time stamps.')
    return x1, y1, l

def direct_slicing_data(a, b, N):
    """
:param a: Time series a
:param b: Time series b
:param N: Divide time series into n parts.
:return: pairwise subsequences of n (number of slicing) time series partitions.
"""
    x, y = [], []
    if len(a) == len(b):
        l = math.floor(len(a) / N)
        x.append(a[0:l])
        y.append(b[0:l])
        if N != 2:
            for i in range(1, N - 1):
                p = a[int(i * l): int((i + 1) * l)]
                x.append(p)
                p = b[int(0 + i * l): int((i + 1) * l)]
                y.append(p)
                i += 1
        x.append(a[(N - 1) * l:])
        y.append(b[(N - 1) * l:])
    else:
        print('Please align! Now we do not support different time stamps.')
    return x, y

def pdtw_overflow(a, b, r, l):
    """
    :param a: full template series
    :param b: full sample series
    :param r: max warping window / extra window size
    :param l: the length of the subsequence
    :return: the PDTW distance and align path
    """
    c = a[1:]
    d = b[1:]
    dis, p = luo_dtw(a[1:], b[1:], r, exp=2, return_path=True)
    E = []
    path = []
    for i in range(len(p)):
        Euclidean_d = (c[p[i][0]] - d[p[i][1]])
        if a[0] == 0 and p[i][0] > len(c) - r - 2:
            E.append(p[i])
            dis -= Euclidean_d * Euclidean_d
        elif a[0] == 1.1 and (p[i][0] < len(a) - 1 - l - r - 1 or p[i][0] >= len(a) - r - 2):
            E.append(p[i])
            dis -= Euclidean_d * Euclidean_d
        elif a[0] == 1.2 and (p[i][0] < r + 1 or p[i][0] >= l + r + 1):
            E.append(p[i])
            dis -= Euclidean_d * Euclidean_d
        elif a[0] == 1 and (p[i][0] < r + 1 or p[i][0] > len(c) - r - 2):
            E.append(p[i])
            dis -= Euclidean_d * Euclidean_d
        elif a[0] == 2 and p[i][0] < r + 1:
            E.append(p[i])
            dis -= Euclidean_d * Euclidean_d
        else:
            path.append(p[i])
    return dis, path

def dirct_slicing_cdtw(a, b, N, r):
    dis = 0
    path = []
    l = math.floor(len(a) / N)
    a1, b1 = direct_slicing_data(a, b, N)
    for i in range(N):
        d, p = luo_dtw(a1[i], b1[i], r, exp=2, return_path=True)
        p.reverse()
        if i == 0:
            path += p
        else:
            path += [[k + i*l, j + i*l ] for [k, j] in p]
        i += 1
        dis += d
    path.reverse()
    return dis, path

def full_pdtw(a, b, N, r):
    dis = 0
    path = []
    a1, b1 = assemble_extra_data(a, b, N, r)
    l = math.floor(len(a) / N)
    for i in range(N):
        d, p = pdtw(a1[i], b1[i], r)
        p.reverse()
        if i == 0:
            path += p
        else:
            path += [[k + (l - r - 1) + (i - 1) * l, j + (l - r - 1) + (i - 1) * l] for [k, j] in p]
        i += 1
        dis += d
    path.reverse()
    return dis, path

def part_contri(a, b):
    """
    :param a: time series 1
    :param b: time series 2
    :return: sum of Euclidean distance difference of every data point.
    """
    c = [abs(a[i]-b[i]) for i in range(len(a))]
    Eucli_dis = sum(c)
    return Eucli_dis

def full_pdtw_overflow(a,b,N,r):
    distance = 0
    path = []
    a1, b1, l = assemble_extra_data_overflow(a,b,N,r)
    d = (r + 1) / l
    for i in range(N):
        dis, p = pdtw_overflow(a1[i], b1[i], r, l)
        #print(p)
        p.reverse()
        if i ==0:
            path += p
        elif i < d+1:
            path +=p
            #path += [[k + (len(a1)-1 - r - 1-l) + (i - 1) * l, j + (len(a1)-1 - r - 1-l) + (i - 1) * l] for [k, j] in p]
        else:
            path += [[k+(l-r-1)+(i-1)*l, j+(l-r-1)+(i-1)*l] for [k,j] in p]
        distance += dis
    path.reverse()
    return distance, path


def main():
    a = [2, 6, 4, 7, 1, 5, 2, 4, 9, 4, 3, 5, 7, 6, 4, 9, 5, 6, 7, 8, 4, 2, 3, 4, 1, 2, 3, 4, 5, 6]
    b = [3, 6, 7, 5, 2, 2, 4, 8, 8, 7, 5, 4, 1, 2, 5, 5, 2, 9, 4, 3, 8, 5, 1, 2, 6, 7, 7, 8, 9, 2]
    print(luo_dtw(a, b, 3, 2, return_path=True))
    print(full_pdtw(a, b, 5, 3))
    print(full_pdtw_overflow(a, b, 30, 3))
    print(dirct_slicing_cdtw(a, b, 30, 5))



if __name__ == '__main__':
    main()

