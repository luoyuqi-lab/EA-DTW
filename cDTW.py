def luo_dtw(a, b, r):
    """ Compute the DTW distance between 2 time series with a globel window constraint (max warping degree)
    :param a: the time series array 1, template, in x-axis direction
    :param b: the time series array 2, sample, in y-axis direction
    :param r: the size of Sakoe-Chiba warping band
    :return: c_pre[k]: the DTW distance
             path: the optimal dtw mapping path
             M: Warping matrix
             D: Distance matrix (by squared Euclidean distance)
    """
    M = []
    # dis = []
    # D = []
    m = len(a)
    k = 0
    # Instead of using matrix of size O(m^2) or O(mr), we will reuse two arrays of size O(r). c array and c_pre array
    c = [float('inf')] * (2 * r + 1)
    c_pre = [float('inf')] * (2 * r + 1)
    for i in range(0, m):
        k = max(0, r - i) # k is a index to control the recursion for every row with lens is (2 * r +1)
        for j in range(max(0, i - r), min(m - 1, i + r) + 1):
            # Initialize the first cell
            if i == 0 and j == 0:
                dis = a[0] - b[0]
                c[k] = dis * dis # squared Euclidean distance of two data points in template and sample series.
                k += 1
                continue
            # float('inf') infinite number, full outers of warping matrix by 'inf'
            y = float('inf') if j - 1 < 0 or k - 1 < 0 else c[k - 1]
            x = float('inf') if i < 1 or k > 2 * r - 1 else c_pre[k + 1]
            z = float('inf') if i < 1 or j < 1 else c_pre[k]
            # Classic DTW calculation
            d = a[i] - b[j]
            c[k] = min(x, y, z) + (d * d) # current cell = mininum of 3 candidates + squared Euclidean distance
            # dis.append(d*d)
            k += 1
        # Move current array to previous array
        c_pre = c
        mm = c_pre.copy()
        M.append(mm)
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
    return c_pre[k], path

