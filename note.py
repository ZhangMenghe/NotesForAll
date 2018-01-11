from __future__ import division
import numpy as np
class showClass(object):
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
        
def numpyFunctions():
    class1_ind = np.where(X[:, 0] <= threshold)
    class1_ind = X[:, 0] <= threshold
    #
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

def buildInFunction():
    predictLabel = max(recorder, key=recorder.get)
    for idx, item in enumerate(L):
        item+=1
        #which equals to
        #for i in range(len(L)):
        #    item = L[i]
    x = [1,2,3]
    y = [4,5,6]
    xy = np.array([x,y])
    zipped = zip(x, y)
    zipList1 = list(zipped)
    zipList2 = zip(*xy)
    # zipList1 equals to zipList2  [(1, 4), (2, 5), (3, 6)]
    zipList[::-1] # equals to zipList.reverse() the third parameter means step
    zipList[::2] #>>> L = range(10)>>> L[::2][0, 2, 4, 6, 8]
def getCurrentWorkingDir():
    import os
    print os.getcwd()
    os.chdir('/root/....')
def main():
    numpyFunctions()
    buildInFunction()
if __name__ == '__main__':
    main()
