import cv2



class GetImg():
    def __init__(self,):
        self.cap = cv2.VideoCapture(0)


    def getImg(self,display= False,size=[480,240]):
        _, img = self.cap.read()
        if _ :
            img = cv2.resize(img,(size[0],size[1]))
            if display:
                cv2.imshow('IMG',img)
            return img
        else :
            return None




if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        img = getImg(True)
        cv2.waitKey(1)