# encoding: utf-8
import csv
import os
import cv2
imgWidth = 3108
imgHeight = 2324
csvFilePath = "C:/Users/hp/Desktop/Tray/Ara2013-RPi/"  # 设置路径

dirs = os.listdir(csvFilePath)                    # 获取指定路径下的文件
for allFile in dirs:                             # 循环读取路径下的文件并筛选输出
    if os.path.splitext(allFile)[1] == ".csv":   # 筛选csv文件
        # name = allFile.split(".")[0].split("/")[-1]
        name = allFile.split("bbox")[0].split("/")[-1]
        imgName = csvFilePath + name + 'rgb.png'
        print(imgName)
        imgFile = cv2.imread(imgName)
        imgHeight = imgFile.shape[0]
        imgWidth = imgFile.shape[1]
        csvFile = os.path.join(csvFilePath, allFile)
        txtFile = csvFilePath + name + 'rgb.txt'
        with open(csvFile, 'r') as f:
            listText = open(txtFile, 'w')  # 清空文件
            reader = csv.reader(f)
            for row in reader:
                centerX = (int(row[0]) + int(row[4])) / 2
                centerY = (int(row[1]) + int(row[5])) / 2
                boxWidth = (int(row[4]) - int(row[0])) / 2
                boxHeight = (int(row[5]) - int(row[1])) / 2
                print(centerX / imgWidth, centerY / imgHeight, boxWidth / imgWidth, boxHeight / imgHeight)
                #print(row)
                print(imgWidth, imgHeight)
                listText.write("0 {} {} {} {}\n".format(centerX / imgWidth, centerY / imgHeight, boxWidth / imgWidth, boxHeight / imgHeight))
            listText.close()
