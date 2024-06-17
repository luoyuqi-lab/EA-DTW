import timeit
from Data_loader import txt_loader
from DTW_functions import luo_dtw, full_pdtw, full_pdtw_overflow, dirct_slicing_cdtw
import math



data_raw_train = txt_loader(r'path\Car_TRAIN.txt')
data_raw_test = txt_loader(r'path\Car_TEST.txt')
BSF_Full_PDTW_1NN = float('inf')
predicted_class_Full_PDTW = float('inf')
BSF_directly_1NN = float('inf')
predicted_class_directly= float('inf')
Acc1 = []
Acc2 = []
Distance_FP = []
Distance_DS = []
count_suc1 = 0
count_suc2 = 0
w = 6

for N in range(2, 17):
    for i in range(len(data_raw_test)):
        for j in range(len(data_raw_train)):
            l = math.floor((len(data_raw_train[0]) - 1) / N)
            if l > w:
                Full_PDTW_dis, path = full_pdtw(data_raw_train[j][1:], data_raw_test[i][1:], N, w)
            else:
                Full_PDTW_dis, path = full_pdtw_overflow(data_raw_train[j][1:], data_raw_test[i][1:], N, w)
            Distance_FP.append(Full_PDTW_dis)
            if Full_PDTW_dis < BSF_Full_PDTW_1NN:
                predicted_class_Full_PDTW = data_raw_train[j][0]
                BSF_Full_PDTW_1NN = Full_PDTW_dis
        if predicted_class_Full_PDTW == data_raw_test[i][0]:
            # correct classification of Full PDTW
            count_suc1 += 1
        # continue to the next sample
        print('The sample', i, 'is finished.')
        BSF_Full_PDTW_1NN = float('inf')
    a1 = float(count_suc1) / float(len(data_raw_test))
    Acc1.append(a1)
    count_suc1 = 0
    print("FP: The N = ",N, " is finished.")

for N in range(13, 15):
    for i in range(len(data_raw_test)):
        for j in range(len(data_raw_train)):
            Directly_dis, path2 = dirct_slicing_cdtw(data_raw_train[j][1:], data_raw_test[i][1:], N, w)
            Distance_DS.append(Directly_dis)
            if Directly_dis < BSF_directly_1NN:
                predicted_class_directly = data_raw_train[j][0]
                BSF_directly_1NN = Directly_dis
        if predicted_class_directly == data_raw_test[i][0]:
        # correct classification of Directly sliced CDTW
            count_suc2 += 1
        # continue to the next sample
        print('The sample', i, 'is finished.')
        BSF_directly_1NN = float('inf')
    a2 = float(count_suc2) / float(len(data_raw_test))
    Acc2.append(a2)
    count_suc2 = 0
    print("DS: The N = ",N, " is finished.")


print('Pdtw Accuracy is:', Acc1,len(Distance_FP))
print('Directly sliced DTW Accuracy is:', Acc2,len(Distance_FP))
print('++++++++++++++NEXT DATASET+++++++++++++++++++++++++++++')


