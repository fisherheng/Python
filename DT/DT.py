from math import log

#######################################################################
#
# Function: calcShannonEnt
# Input: dataSet
# output: shannonEnt
# Introduction: This function is used to calculate the shannon value
#
#######################################################################
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for fetVec in dataSet:
        currentLabel = fetVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

#######################################################################
#
# Function: splitDataSet
# Input: dataSet, axis, value
# Output: retDataSet
# IntroDuction: This function can split dataSet
#
#######################################################################
def splitDataSet(dataSet, axis, value):
    retDataSet = []             #Create a separate list
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

#######################################################################
#
# Function: chooseBestFeature
# Input: dataSet
# Output: bestFeature
# Introduction: This function trys to choose the best feature
#
#######################################################################
def chooseBestFeature(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

























