import cv2 as cv
import numpy as np
import pytesseract
imgloc = r"C:\Users\Matthew Prata\Documents\Reciept Calculator\Test4.jpg"
img = cv.imread("Costco092021.jpeg")
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def avg(img):
    average_color1 = np.average(img, axis = 0)
    average_color = np.average(average_color1,axis = 0)
    print(average_color)
    return average_color

def invimg(img,avg_color):
    i,j=0,0
    width = img.shape[1]
    height = img.shape[0]

    for i in range(width):
        for j in range(height):
            color = img[j,i]
            
            if color[2] > avg_color[2]- 50: 
                
          
            #if color[0] < 116 and color[1] < 90 and color[2] < 100:
                color = [0,0,0]
           
            else: 
                color = [255,255,255]
            img[j,i] = color
    #img = abs(img-255)
    print("Returning the inverted image")
    return img

average_color = avg(img)
img = invimg(img,average_color)
info = pytesseract.image_to_string(img)
print(info)
cv.imshow('Reciept',img)
cv.waitKey(0)
