import cv2 
import numpy as np


def executeMedian(WindowSize, inputimg, x, y, nx, ny):
    Maxsize = 5;
    mask = np.zeros((WindowSize * WindowSize),dtype=np.double)
    Dx = np.zeros((WindowSize * WindowSize),dtype=np.double)
    Dy = np.zeros((WindowSize * WindowSize),dtype=np.double)

    Index = 0
    for a in range(- int(WindowSize / 2),int(WindowSize / 2)+1):
        for b in range(- int(WindowSize / 2),int(WindowSize / 2)+1):
            #print(b)
            Dx[Index] = a;
            Dy[Index] = b;
            Index=Index+1;
    
    Max_gray_Value = 0
    Min_gray_Value = 0
    Med_gray_Value = 0
    PixelValue = 0 
    A1 = 0
    A2 = 0
    B1 = 0
    B2 = 0
    NewY = 0
    NewX = 0
    ArrayLength = 0
    Max_gray_Value = 0
    Min_gray_Value = 255
    PixelValue = inputimg[x, y]
    #print(inputimg.shape)

    for c in range(WindowSize * WindowSize):
        NewX = x + Dx[c]
        NewY = y + Dy[c]
        if (NewX >= 0 and NewX < nx and NewY >= 0 and NewY < ny):
                mask[ArrayLength] = inputimg[int(NewX),int(NewY)]
                if (mask[ArrayLength] > Max_gray_Value):
                    Max_gray_Value = mask[ArrayLength]
                
                if (mask[ArrayLength] < Min_gray_Value):
                    Min_gray_Value = mask[ArrayLength]
                
                ArrayLength=ArrayLength+1

    #print(ArrayLength)
            
    mask.sort()
    Min_gray_Value = mask[0]
    Med_gray_Value = mask[int(ArrayLength / 2)]
    A1 = Med_gray_Value - Min_gray_Value
    A2 = Med_gray_Value - Max_gray_Value
    
    if (A1 > 0 and A2 < 0):
        B1 = PixelValue - Min_gray_Value
        B2 = PixelValue - Max_gray_Value
        if (B1 > 0 and B2 < 0):
            return PixelValue
        else:
            if(WindowSize + 2 <= Maxsize):
                return executeMedian(WindowSize + 2, inputimg, x, y, nx, ny)
            else:
                return Med_gray_Value
    else:
        return Med_gray_Value

def AdaptiveMedian(inputimg):
    nx = inputimg.shape[1]
    ny = inputimg.shape[0]
    WindowSize = 3


    out = np.zeros((nx,ny),dtype=np.uint8)


    for x in range(nx):
        for y in range(ny):
            out[x,y] = executeMedian(WindowSize, inputimg, x, y, nx, ny)
            
    return out


img = cv2.imread("test.bmp")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
print(img.shape)





result = AdaptiveMedian(img)
cv2.imwrite("filteredimage.bmp",result)

cv2.imshow("teste",result)
cv2.waitKey(0)


