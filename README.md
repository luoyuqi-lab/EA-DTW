# Partial DTW (Pdtw) and EAdtw
A novel highly accurate DTW slicing method and the application combine it with the early abandoning (EA) strategy.

Also include the txt file input code, time series slicing code, and dataset Car. More datasets used in our experiments can be found at [UCR Archive](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/).

***
### Important: All DTW-related functions are in `DTW_functions.py`.
***

***`x, y = assemble_extra_data(a, b, N, r)`, assemble pairwise subsequences with extra data windows in PDTW.***

+ a, b: Original two time series. One as the template, and another as the sample.

+ N: slice a full DTW calculation into n parts.

+ r: size of Sakoe-Chiba band.

***`dis, path = pdtw(a, b, r)`, Pdtw in the paper.***

+ a, b: two time series. One as the template, and another as the sample.

+ n: slice a full DTW calculation into n parts.

+ dis: the PDTW distance of a sub-series pair.

+ path: the path of PDTW

***`dis, path = full_pdtw(a, b, N, r)`, the sum of all segments calculated by Pdtw in the paper.***

`luo_dtw(a, b, r, exp, return_path=False)` is our implement of constraint dynamic time warping using Sakoe-Chiba band as the max warping window.

***

### Example:

`a = [2,6,4,7,1,5,2,4,9,4,3,5,7,6,4,9,5,6,7,8,4,2,3,4,1,2,3,4,5,6]`

`b = [3,6,7,5,2,2,4,8,8,7,5,4,1,2,5,5,2,9,4,3,8,5,1,2,6,7,7,8,9,2]`

**cdtw**:

`dis,path = luo_dtw(a, b, 3, 2, return_path=True)`

+ `dis = 92`
+ `path = [[29, 29], [29, 28], [29, 27], [29, 26], [28, 25], [27, 24], [26, 23], [25, 23], [24, 23], [23, 23], [22, 23], [21, 22], [20, 21], [19, 20], [18, 20], [17, 20], [16, 19], [16, 18], [15, 17], [14, 16], [13, 15], [12, 14], [11, 14], [10, 13], [10, 12], [9, 11], [9, 10], [8, 9], [8, 8], [8, 7], [7, 6], [6, 6], [5, 6], [4, 5], [4, 4], [3, 3], [2, 3], [1, 2], [1, 1], [0, 0]]`

**full_pdtw**:

`dis,path = full_pdtw(a, b, 5, 3)`
+ `dis = 92`
+ `path = [[29, 29], [29, 28], [29, 27], [29, 26], [28, 25], [27, 24], [26, 23], [25, 23], [24, 23], [23, 23], [22, 23], [21, 22], [20, 21], [19, 20], [18, 20], [17, 20], [16, 19], [16, 18], [15, 17], [14, 16], [13, 15], [12, 14], [11, 14], [10, 13], [10, 12], [9, 11], [9, 10], [8, 9], [8, 8], [8, 7], [7, 6], [6, 6], [5, 6], [4, 5], [4, 4], [3, 3], [2, 3], [1, 2], [1, 1], [0, 0]]`


**direct_slicing_cdtw**:

`dis,path = dirct_slicing_cdtw(a, b, 5, 3)`
+ `dis = 233`
+ `path = [[29, 29], [29, 28], [29, 27], [29, 26], [28, 25], [27, 24], [26, 24], [25, 24], [24, 24], [23, 23], [22, 23], [21, 22], [20, 21], [19, 20], [18, 19], [18, 18], [17, 17], [16, 17], [15, 17], [14, 16], [13, 15], [13, 14], [13, 13], [12, 12], [11, 11], [10, 11], [9, 10], [8, 9], [8, 8], [8, 7], [7, 6], [6, 6], [5, 5], [4, 4], [3, 3], [2, 3], [1, 2], [1, 1], [0, 0]]`

**"overflow" means the functions version of the warping window size w could over the segment length N.**

**EADTW is achieved in Exp codes, in the processing of the sum of all PDTW segments.**
***
***If these codes can help you, please give a STAR.*** :smiley:

***If you use these codes or ideas in your research/software/product, please cite our paper:*** :+1:

`@article{luo2024accurate,

  title={An accurate slicing method for dynamic time warping algorithm and the segment-level early abandoning optimization},
  
  author={Luo, Yuqi and Ke, Wei and Lam, Chan-Tong and Im, Sio-Kei},
  
  journal={Knowledge-Based Systems},
  
  volume={300},
  
  pages={112231},
  
  year={2024},
  
  publisher={Elsevier}
}`


#### Be sure your use follows the license. :zap:
