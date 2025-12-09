def calculatePrecisionRecallF1(trueLabel, predictedLabels, k=3):
    truePos = 0
    falsePos = len(predictedLabels)
    falseNeg = 0
    if trueLabel in predictedLabels:
        truePos = truePos + 1
    if truePos == 1:
        falsePos = falsePos - 1
    if truePos == 0:
        falseNeg = falseNeg + 1
    precision = truePos / (truePos + falsePos + 0.0000000001) 
    recall = truePos / (truePos + falseNeg + 0.000000000001)
    F1 = 2 * precision * recall / (precision + recall + 0.0000000000001)
    return truePos,precision, recall, F1
