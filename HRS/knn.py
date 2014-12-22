from numpy import *
import operator

'''
function: img2vector
input: filename
return: returnVect
introduction: This function is used to converts the image to a vector
'''
def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect


