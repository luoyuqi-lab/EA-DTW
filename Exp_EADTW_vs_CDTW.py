from DTW_functions import assemble_extra_data,assemble_extra_data_overflow,pdtw_overflow,pdtw,luo_dtw,part_contri
from Data_loader import txt_loader
import math
import timeit


data_raw_train = txt_loader(r'C:\Users\luoyu\Desktop\Car\Car_TRAIN.txt')
data_raw_test = txt_loader(r'C:\Users\luoyu\Desktop\Car\Car_TEST.txt')
BSF_Full_EADTW_1NN = float('inf')
predicted_class_EADTW = float('inf')
BSF_CDTW_1NN = float('inf')
predicted_class_CDTW= float('inf')
Acc3 = []
Acc4 = []
time_EADTW = []
seg_Eu_dis= []
count_suc1 = 0
count_suc2 = 0
count_suc3 = 0
count_suc4 = 0

w = 6

for N in range(2, 17):
    start = timeit.default_timer()
    for i in range(len(data_raw_test)):
        for j in range(len(data_raw_train)):
            l = math.floor((len(data_raw_train[0]) - 1) / N)
            current_dis = 0
            if l > w:
                a, b = assemble_extra_data(data_raw_train[j][1:], data_raw_test[i][1:], N, w)
                seg_Eu_dis = []
                for k in range(N):
                    con = part_contri(a[k], b[k])
                    seg_Eu_dis.append(con)
                indexed_seg_Eu_dis = list(enumerate(seg_Eu_dis))
                sorted_indexed_seg_Eu_dis = sorted(indexed_seg_Eu_dis, key=lambda x: x[1], reverse=True)
                sorted_indices = [index for index, value in sorted_indexed_seg_Eu_dis]
                #print("#",sorted_indices)
                for e in range(N):
                    EADTW_dis, path = pdtw(a[sorted_indices[e]], b[sorted_indices[e]], w)
                    #print("##",EADTW_dis)
                    current_dis += EADTW_dis
                    #print("###",current_dis, BSF_Full_EADTW_1NN)
                    if current_dis < BSF_Full_EADTW_1NN and e == N-1:
                        predicted_class_EADTW = data_raw_train[j][0]
                        BSF_Full_EADTW_1NN = current_dis
                        #print("####",BSF_Full_EADTW_1NN)
                    elif current_dis > BSF_Full_EADTW_1NN:
                        break
                #print("#####",current_dis, BSF_Full_EADTW_1NN, "I,J",i,j)
            else:
                #print("overflow")
                a, b, l= assemble_extra_data_overflow(data_raw_train[j][1:], data_raw_test[i][1:], N, w)
                seg_Eu_dis = []
                for k in range(N):
                    con = part_contri(a[k], b[k])
                    seg_Eu_dis.append(con)
                indexed_seg_Eu_dis = list(enumerate(seg_Eu_dis))
                sorted_indexed_seg_Eu_dis = sorted(indexed_seg_Eu_dis, key=lambda x: x[1], reverse=True)
                sorted_indices = [index for index, value in sorted_indexed_seg_Eu_dis]
                for e in range(N):
                    EADTW_dis, path = pdtw_overflow(a[sorted_indices[e]], b[sorted_indices[e]], w, l)
                    current_dis += EADTW_dis
                    if current_dis < BSF_Full_EADTW_1NN and e == N - 1:
                        predicted_class_EADTW = data_raw_train[j][0]
                        BSF_Full_EADTW_1NN = current_dis
                    elif current_dis > BSF_Full_EADTW_1NN:
                        break
                    else:
                        e += 1
        if predicted_class_EADTW == data_raw_test[i][0]:
            # correct classification of Full EADTW
            count_suc3 += 1
            # continue to the next sample
        print('The sample', i, 'is finished.')
        BSF_Full_EADTW_1NN = float('inf')
    end = timeit.default_timer()
    t = '%.4f' % (end - start)
    a1 = float(count_suc3) / float(len(data_raw_test))
    Acc3.append(a1)
    time_EADTW.append(t)
    count_suc3 = 0
    print("EADTW: The N = ", N, " is finished.")

start = timeit.default_timer()
for i in range(len(data_raw_test)):
    for j in range(len(data_raw_train)):
        d, p = luo_dtw(data_raw_train[j][1:], data_raw_test[i][1:], w, 2,return_path=True)
        if d < BSF_CDTW_1NN:
            predicted_class_CDTW = data_raw_train[j][0]
            BSF_CDTW_1NN = d
    if predicted_class_CDTW == data_raw_test[i][0]:
        count_suc4 += 1
    BSF_CDTW_1NN = float('inf')
    print("Sample", i, " is finished by CDTW.")
a2 = float(count_suc4) / float(len(data_raw_test))
end = timeit.default_timer()
t2 = '%.4f' % (end - start)


print('EADTW Accuracy is:', Acc3, 'Time consumption is:', time_EADTW)
print('CDTW Accuracy is:', a2, 'Time consumption is:', t2)