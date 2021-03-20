import cv2
import main

cap = cv2.VideoCapture(main.CAMERA_PORT)

def getImg(display= False,size=[480,240]):
    _, img = cap.read()
    if _ :
        img = cv2.resize(img,(size[0],size[1]))
        if display:
            cv2.imshow('IMG',img)
        return img
    else :
        return None




if __name__ == '__main__':
    while True:
        img = getImg(True)
        cv2.waitKey(1)