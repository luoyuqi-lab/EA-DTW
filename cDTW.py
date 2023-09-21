from file_read import txtinput
import timeit
def luo_dtw(a, b, r):
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
    # dis = []
    # D = []
    m = len(a)
    k = 0
    # Instead of using matrix of size O(m^2) or O(mr), we will reuse two arrays of size O(r)
    cost = [float('inf')] * (2 * r + 1)
    cost_prev = [float('inf')] * (2 * r + 1)
    for i in range(0, m):
        k = max(0, r - i) # k is a index to control the recursion for every row with lens is (2 * r +1)
        for j in range(max(0, i - r), min(m - 1, i + r) + 1):
            # Initialize the first cell
            if i == 0 and j == 0:
                c = a[0] - b[0]
                cost[k] = c * c # squared Euclidean distance of two data points in template and sample series.
                k += 1
                continue
            # float('inf') infinite number, full outers of warping matrix by 'inf'
            y = float('inf') if j - 1 < 0 or k - 1 < 0 else cost[k - 1]
            x = float('inf') if i < 1 or k > 2 * r - 1 else cost_prev[k + 1]
            z = float('inf') if i < 1 or j < 1 else cost_prev[k]
            # Classic DTW calculation
            d = a[i] - b[j]
            cost[k] = min(x, y, z) + (d * d) # current cell = mininum of 3 candidates + squared Euclidean distance
            # dis.append(d*d)
            k += 1
        # Move current array to previous array
        cost_prev = cost
        c = cost_prev.copy()
        M.append(c)
        # D.append(dis)
        # dis = []
    # The DTW distance is in the last cell in the matrix of size O(m^2) or at the middle of our array
    i = m-1
    j = r
    rj = len(b) - 1
    path = [[len(a) - 1, len(b) - 1]]
    while i != 0 or rj != 0: #recursion from [n,m] to [0,0] in template and sample series
        x = M[i][j - 1] if j - 1 >=0 else float('inf') #real dtw candidate (i, j-1)
        y = M[i-1][j] if i - 1 >=0 else float('inf') #real dtw candidate (i-1, j-1)
        z = M[i-1][j+1] if i - 1 >=0 and j+1 <= 2 * r else float('inf') #real dtw candidate (i-1, j)
        # Save the real location index of optimal warping path in two input time series.
        if min(x, y, z) == y:
            path_temp = [i-1, rj - 1]
            path.append(path_temp)
            i = i-1
            j = j
            rj = rj - 1
        elif min(x, y, z) == x :
            path_temp = [i , rj - 1]
            path.append(path_temp)
            i = i
            j = j - 1
            rj = rj -1
        else:
            path_temp = [i - 1 ,rj]
            path.append(path_temp)
            i = i - 1
            j = j + 1
    k -= 1
    return cost_prev[k], path

# # a = txtinput(r'C:\Users\luoyu\OneDrive\桌面\a.txt',0)
# # b = txtinput(r'C:\Users\luoyu\OneDrive\桌面\b.txt',0)
# #
# a1 = [1,1,2,2,3,3,2,2,3,2]
# b1 = [3,3,3,4,5,5,4,5,5,5]
# a = [2,6,4,7,1,5,2,4,9,4,3,5,7,6,4,9,5,6,7,8,4,2,3,4,1,2,3,4,5,6]
# b = [3,6,7,5,2,2,4,8,8,7,5,4,1,2,5,5,2,9,4,3,8,5,1,2,6,7,7,8,9,2]
# d, p= luo_dtw(b,a,5)
# print(d,p)

# dc = 0
# for i in range(len(p)):
#     dc = dc + (b1[p[i][0]]-a1[p[i][1]])**2
# print(dc)
# print(d,'Optimal dtw warping path:', p, 'Warping matrix:',wm,'Distance matrix:', dm)