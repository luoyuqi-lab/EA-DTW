def partition(a, b, n):
    """
:param a: Time series a
:param b: Time series b
:param n: Divide time series into n parts.
:returm: a set of n time series partitions.
"""

    if len(a) == len(b):
        x = []
        y = []
        k = len(a)
        if k % n == 0:
            for i in range(0, n):
                p = a[int(0 + i * (k / n)) : int((i + 1) * (k / n))]
                x.append(p)
                p = b[int(0 + i * (k / n)): int((i + 1) * (k / n))]
                y.append(p)
                i += 1
        else:
            m = k % n
            i = 0
            for i in range(0, n-1):
                p = a[int(0 + i * ((k-m) / n)) : int((i + 1) * ((k-m) / n))]
                x.append(p)
                p = b[int(0 + i * ((k-m) / n)): int((i + 1) * ((k-m) / n))]
                y.append(p)
                i += 1
            while i == n-1:
                p = a[int(0 + i * ((k-m) / n)) : int(len(a))]
                x.append(p)
                p = b[int(0 + i * ((k-m) / n)): int(len(a))]
                y.append(p)
                i += 1
    else:
        print('Please align! Now we not support different durations.')

    return x, y

def part_contri(a, b):
    """
    :param a: time series 1
    :param b: time series 2
    :return: sum of difference of every data point.
    """
    c = [abs(a[i]-b[i]) for i in range(len(a))]
    index = sum(c)
    return index
