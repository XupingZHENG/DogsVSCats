import os
import shutil
import glob


def copyData(srcFolder, trainFolder, numTrain, valFolder, numVal):
    srcFiles = os.listdir(srcFolder)
    os.mkdir(trainFolder)
    os.mkdir(valFolder)
    for i in range(numTrain):
        srcFile = os.path.join(srcFolder, srcFiles[i])
        dstFile = os.path.join(trainFolder, srcFiles[i])
        shutil.copy(srcFile, dstFile)
    for i in range(numTrain,(numTrain + numVal)):
        srcFile = os.path.join(srcFolder, srcFiles[i])
        dstFile = os.path.join(trainFolder, srcFiles[i])
        shutil.copy(srcFile, dstFile)


prefix = 'mid'
numTrain = 5000
numVal = 1000

trainCat = prefix + '/train/cat'
trainDog = prefix + '/train/dog'
valCat = prefix + '/val/cat'
valDog = prefix + '/val/dog'
os.makedirs(trainCat, exist_ok=True)
os.makedirs(trainDog, exist_ok=True)
os.makedirs(valCat, exist_ok=True)
os.makedirs(valDog, exist_ok=True)

def copyImages(src, dstTrain, numTrain, dstVal, numVal):
    for i in range(numTrain):
        srcFile = src[i]
        fileName = srcFile.split('\\')[-1]
        dstFile = os.path.join(dstTrain, fileName)
        shutil.copy(srcFile, dstFile)
    for i in range(numTrain, numTrain + numVal):
        srcFile = src[i]
        fileName = srcFile.split('\\')[-1]
        dstFile = os.path.join(dstVal, fileName)
        shutil.copy(srcFile, dstFile)


catImages = glob.glob('train\\cat*.jpg')
copyImages(catImages, trainCat, numTrain, valCat, numVal)

dogImages = glob.glob('train\\dog*.jpg')
copyImages(dogImages, trainDog, numTrain, valDog, numVal)
