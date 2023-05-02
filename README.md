# EA_DTW：Universal acceleration dynamic time warping (DTW) algorithm with early abandoning (EA).


* **luo_dtw** is the constraint dynamic time warping used Sakoe-Chiba band as max warping window.

* **EAdtw** is the proposed method.

* **sliceNrebuild(a,b,n,r)** can reassemble a and b series into n series, with add contribution and location information in [0] and [1] for every sub-series. Contribution: large means more contributions for similarity judgement. Location: 0 -> first series, 1 -> middle series, 2-> end series. 

__More information please check the source code and code comment.__

Also provide time series dataset by txt file, CinCECGTorso and Phoneme. You can also find dataset [here](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/).

Please run quickly start to know functions outputs.

**Example**:

data:
```
a = [2,6,4,7,1,5,2,4,9,4,3,5,7,6,4,9,5,6,7,8,4,2,3,4,1,2,3,4,5,6]

b = [3,6,7,5,2,2,4,8,8,7,5,4,1,2,5,5,2,9,4,3,8,5,1,2,6,7,7,8,9,2]
```

cdtw:

```
dis,path = luo_dtw(a, b, 5)

>>>dis = 90

>>>path = [[29, 29], [28, 29], [27, 29], [26, 29], [25, 29], [24, 28], [23, 27], [23, 26], [23, 25], [23, 24], [23, 23], [23, 22], [22, 21], [21, 20], [20, 19], [20, 18], [20, 17], [19, 16], [18, 16], [17, 15], [16, 14], [15, 13], [14, 12], [14, 11], [13, 10], [12, 10], [11, 9], [10, 9], [9, 8], [8, 8], [7, 8], [6, 7], [6, 6], [6, 5], [5, 4], [4, 4], [3, 3], [3, 2], [2, 1], [1, 1], [0, 0]]
```

EAdtw:

```
ep, suc = EA_DTW(a,b,2,5,91)

>>>ep = 90
>>>suc = 1
``` 

```
ep, suc = EA_DTW(a,b,3,5,91)

>>>ep = 90
>>>suc = 1 
```

```
ep, suc = EA_DTW(a,b,3,5,88)

>>>ep = 88
>>>suc = 0
```

Time series reassemble:

```
sliceNrebuild(a,b,3,5)

>>>([[20, 0, 2, 6, 4, 7, 1, 5, 2, 4, 9, 4, 3, 5, 7, 6, 4, 9], [32, 1, 1, 5, 2, 4, 9, 4, 3, 5, 7, 6, 4, 9, 5, 6, 7, 8, 4, 2, 3, 4, 1, 2], [37, 2, 4, 9, 5, 6, 7, 8, 4, 2, 3, 4, 1, 2, 3, 4, 5, 6]], [[20, 0, 3, 6, 7, 5, 2, 2, 4, 8, 8, 7, 5, 4, 1, 2, 5, 5], [32, 1, 2, 2, 4, 8, 8, 7, 5, 4, 1, 2, 5, 5, 2, 9, 4, 3, 8, 5, 1, 2, 6, 7], [37, 2, 5, 5, 2, 9, 4, 3, 8, 5, 1, 2, 6, 7, 7, 8, 9, 2]])
```


### If these codes can help you, please give a STAR. :smile:

### If you use these code or idea in your research/software/product, please cite our paper :smiling_face_with_three_hearts::

`TBD update`


Be sure your using follows the lisence.
