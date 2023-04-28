from cDTW import luo_dtw

def partial_dtw(a,b,r,location=''):
    """
    :param a: full template series
    :param b: full sample series
    :param r: max warping window / extra window size
    :return:
    DO NOT MAKE extra window out of full time series! Like full series is [0:30], warping window is r = 5
    calculate partial_dtw [20:26] is not supported, because 26+5+1 over the size of full time series length，30 !
    By this way, [4:10] is also can not be calculate, because 4 - 5 - 1 less than 0 !
    """
    d, p = luo_dtw(a, b, r)
    E = []
    dis = d
    if location == 'front':
        for i in range(len(p)):
            if p[i][0]> len(a)-r-2:
                E.append(p[i])
                # print(a[p[i][0]],b[p[i][1]])
                Euclidean_d = (a[p[i][0]]-b[p[i][1]])
                # print(Euclidean_d)
                dis = dis - (Euclidean_d*Euclidean_d)
                #print(dis)
    elif location == 'middle':
        #print('m')
        for i in range(len(p)):
            if p[i][0] < r+1 or p[i][0]> len(a)-r-2:
                E.append(p[i])
                # print(a[p[i][0]],b[p[i][1]])
                Euclidean_d = (a[p[i][0]]-b[p[i][1]])
                #print(Euclidean_d)
                dis = dis - (Euclidean_d*Euclidean_d)
                #print(dis)
    else: # if location == 'back'
        #print('b')
        for i in range(len(p)):
            if p[i][0] < r+1:
                E.append(p[i])
                # print(a[p[i][0]],b[p[i][1]])
                Euclidean_d = (a[p[i][0]]-b[p[i][1]])
                #print(Euclidean_d)
                dis = dis - (Euclidean_d*Euclidean_d)
                #print(dis)
    return dis