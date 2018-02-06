from __future__ import division
import numpy as np
class showClass(object):
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
        
def numpyFunctions():
    class1_ind = np.where(X[:, 0] <= threshold)
    class1_ind = X[:, 0] <= threshold
    # copy array elements
    ith_feature = oob_sample[:, i].copy()
    randomPermute = np.random.choice(ith_feature, len(ith_feature), replace=True)
    #Use map as recorder
    uniqueY = np.unique(Y)
    recorder = {x: 0 for x in uniqueY}
    for yi in Y:
        recorder[yi] += 1
    values = np.array(recorder.values())
    #一个list所有值都执行一个操作
    newArray = np.array([func_1(x) for x in X_test])
    #检查矩阵A中每个元素Ai是否属于矩阵B, invert 即is not in
    in_mask = np.isin(A, B, invert = True)
    # 矩阵连接,X,Y,Z dimension: h*w*1
    concat_array = np.concatenate((X,Y,Z), axis = 2)
    # 升维，2-dimension->3 dimension, eg. h*w -> h*w*1
    exp_array = np.expand_dims(X, axis = 2)
    # Element-wise division, A, B should be same dimension
    divide_res = np.divide(A,B)
    # Element-wise multiplication
    mul_res = np.multiply(A,B)
    # element wise maximum
    array = np.maximum(1, array)
def buildInFunction():
    predictLabel = max(recorder, key=recorder.get)
    for idx, item in enumerate(L):
        item+=1
        #which equals to
        #for i in range(len(L)):
        #    item = L[i]
    x = [1,2,3]
    y = [4,5,6]
    # length of list
    len(x)
    xy = np.array([x,y])
    zipped = zip(x, y)
    zipList1 = list(zipped)
    zipList2 = zip(*xy)
    # zipList1 equals to zipList2  [(1, 4), (2, 5), (3, 6)]
    zipList[::-1] # equals to zipList.reverse() the third parameter means step
    zipList[::2] #>>> L = range(10)>>> L[::2][0, 2, 4, 6, 8]
def scipyFunctions():
    # Equal to conv2(x,y,mode="same") in Matlab, 这么麻烦是因为matlab和python的center focus 不同，若mode ="full"就不需要这样了
    # filter2 -> conv2(x, rot90(y))
    convolve_res = np.rot90(signal.convolve2d(np.rot90(x, 2), np.rot90(y, 2), mode=mode), 2)
def getCurrentWorkingDir():
    import os
    print os.getcwd()
    os.chdir('/root/....')
def fileIO():
    try:
        fp = open(path, 'r')
        filenameSet = fp.readlines()
    finally:
        fp.close()
    # with open() as fp
    for idx, file in enumerate(filenameSet):
        split_items = file.split('/')
        addr = path + '/'.join(p for p in split_items[:4]) + '/.txt'
def main():
    numpyFunctions()
    buildInFunction()
    scipyFunctions()
if __name__ == '__main__':
    main()
