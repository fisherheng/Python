'''
This function is used to transfer data file to matrix
'''
def file2matrix(filename):
    fr = open(filename)     #打开文件
    arrayOfLines = fr.readlines()   #文件按行创建一个数组
    numberOfLines = len(arrayOfLines)   #获取数组长度=文件行数
    returnMat = zeros((numberOfLines, 3))   #创建一个文件行数x3的空矩阵
    classLabelVector = []   #创建用于分类的标签向量
    index = 0
    for line in arrayOfLines:
        line = line.strip()     #删除空白符，包括\n \r \t
        listFromLine = line.split('\t')     
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,ClassLabelVector


