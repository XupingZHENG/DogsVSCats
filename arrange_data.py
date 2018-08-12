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


trainCat = 'small/train/cat'
trainDog = 'small/train/dog'
valCat = 'small/val/cat'
valDog = 'small/val/dog'
os.makedirs(trainCat, exist_ok=True)
os.makedirs(trainDog, exist_ok=True)
os.makedirs(valCat, exist_ok=True)
os.makedirs(valDog, exist_ok=True)

numTrain = 1000
numVal = 400


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


# catImages = glob.glob('train\\cat*.jpg')
# copyImages(catImages, trainCat, numTrain, valCat, numVal)

dogImages = glob.glob('train\\dog*.jpg')
copyImages(dogImages, trainDog, numTrain, valDog, numVal)
