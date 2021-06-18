import cv2
import numpy as np
import utlis
import time

curveList = []
avgVal=10
 
def getLaneCurve(img,display=2):
 
    imgCopy = img.copy()
    imgResult = img.copy()
    
    #### mask the image and get the white A4 paper 
    imgThres = utlis.thresholding(img)
 
    #### Wrap the image to get Bird's-eye view
    hT, wT, c = img.shape
    points = [[128,147],[352,147],[49,240],[431,240]]
    imgWarp = utlis.warpImg(imgThres,points,wT,hT)
    
    # draw the points
    if display != 0 :
        imgWarpPoints = utlis.drawPoints(imgCopy,points)
 

    #### get the middle point to calculate the curve
    middlePoint,imgHist = utlis.getHistogram(imgWarp,display=True,minPer=0.8,region=4)
    curveAveragePoint, imgHist = utlis.getHistogram(imgWarp, display=True, minPer=0.9)
    curveRaw = curveAveragePoint - middlePoint
 
    # average the last'10' curve
    curveList.append(curveRaw)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))
 
    # displays
    if display != 0:
        imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT, inv=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
        imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
        midY = 450
        cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
        cv2.line(imgResult, (wT // 2, midY), (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)
        cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = wT // 20
            cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
        # fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        # cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230, 50, 50), 3)
    if display == 2:
        imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoints, imgWarp],
                                             [imgHist, imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)
        cv2.waitKey(1)
    elif display == 1:
        cv2.imshow('Resutlt', imgResult)
        cv2.waitKey(1)
 
    # NORMALIZATION
    curve = curve/100
    if curve>1: curve ==1
    if curve<-1:curve == -1

    return curve
 
 
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    frameCounter = 0
    while True:
        _, img = cap.read()
        img = cv2.resize(img,(480,240))
        curve = getLaneCurve(img,display=2)
        print("curve: ",curve)
        cv2.waitKey(1)