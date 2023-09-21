# Partial DTW (Pdtw) and EAdtw
A novel highly accurate DTW slicing method and the application combine it with early abandoning (EA) strategy.

Also include the txt file input code, time series slicing code, and dataset CinCECGTorso.

***
### Important: Please run **`quickly start.py`** to know function outputs. More detailed comments are also in it.
***

***`d , suc = EA_DTW(a, b, n, r, e)`, EAdtw in the paper.***

+ a, b: two time series. One as the template, and another as the sample.

+ n: slice a full DTW calculation into n parts.

+ r: size of Sakoe-Chiba band.

+ e: a threshold epsilon, to determine if the sample is the 'best-so-far' candidate.

+ d: distance of EAdtw.

+ suc: 1 means the sample will be the 'best-so-far' candidate.

***`d = partial_dtw(a, b, n, location=)`, Pdtw in the paper.***

+ a, b: two time series. One as the template, and another as the sample.

+ n: slice a full DTW calculation into n parts.

+ location: the location of the sub-series in the full time series.

+ d: the Pdtw distance of a sub-series pair.

`luo_dtw(a, b, r)` is the constraint dynamic time warping using Sakoe-Chiba band as the max warping window, with saving memory.

***

### Example:

`a = [2,6,4,7,1,5,2,4,9,4,3,5,7,6,4,9,5,6,7,8,4,2,3,4,1,2,3,4,5,6]`

`b = [3,6,7,5,2,2,4,8,8,7,5,4,1,2,5,5,2,9,4,3,8,5,1,2,6,7,7,8,9,2]`

**cdtw**:

`dis,path = luo_dtw(a, b, 5)`

+ `dis = 90`
+ `path = [[29, 29], [28, 29], [27, 29], [26, 29], [25, 29], [24, 28], [23, 27], [23, 26], [23, 25], [23, 24], [23, 23], [23, 22], [22, 21], [21, 20], [20, 19], [20, 18], [20, 17], [19, 16], [18, 16], [17, 15], [16, 14], [15, 13], [14, 12], [14, 11], [13, 10], [12, 10], [11, 9], [10, 9], [9, 8], [8, 8], [7, 8], [6, 7], [6, 6], [6, 5], [5, 4], [4, 4], [3, 3], [3, 2], [2, 1], [1, 1], [0, 0]]`


**EAdtw**:

`ep, suc = EA_DTW(a,b,2,5,91)`

+ `ep = 90`
+ `suc = 1` 

`ep, suc = EA_DTW(a,b,3,5,91)`

+ `ep = 90`
+ `suc = 1 `

`ep, suc = EA_DTW(a,b,3,5,88)`

+ `ep = 88`
+ `suc = 0`
  
***

### Time series reassemble:

**`sliceNrebuild(a,b,3,5)`**

`([[20, 0, 2, 6, 4, 7, 1, 5, 2, 4, 9, 4, 3, 5, 7, 6, 4, 9], [32, 1, 1, 5, 2, 4, 9, 4, 3, 5, 7, 6, 4, 9, 5, 6, 7, 8, 4, 2, 3, 4, 1, 2], [37, 2, 4, 9, 5, 6, 7, 8, 4, 2, 3, 4, 1, 2, 3, 4, 5, 6]], [[20, 0, 3, 6, 7, 5, 2, 2, 4, 8, 8, 7, 5, 4, 1, 2, 5, 5], [32, 1, 2, 2, 4, 8, 8, 7, 5, 4, 1, 2, 5, 5, 2, 9, 4, 3, 8, 5, 1, 2, 6, 7], [37, 2, 5, 5, 2, 9, 4, 3, 8, 5, 1, 2, 6, 7, 7, 8, 9, 2]])`

#### If divide the full calculation into *n* segments:

**`EAdtw(a, b, n, r, infinite) = Pdtw(a1, b1, r) + Pdtw(a2, b2, r) + Pdtw(a3, b3, r) + ... + Pdtw(an, bn, r)`**

***

***If these codes can help you, please give a STAR.*** :smiley:

***If you use these codes or ideas in your research/software/product, please cite our paper:*** :+1:

`TBD update`


#### Be sure your use follows the license. :zap:
