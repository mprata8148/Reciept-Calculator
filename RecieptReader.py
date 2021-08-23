import cv2 as cv
import numpy as np
import pytesseract

img = cv.imread('Costco0723.jpeg')
def resize_image(img,scale=0.75):
    width = int (img.shape[1]*scale) 
    height = int (img.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

### Detecting Characters with Boxes
def boximg(img):
    Wimg = img.shape[1]
    Height = img.shape[0]
    boxes = pytesseract.image_to_boxes(img)
    #print(boxes)
    for b in boxes.splitlines():
        b = b.split(' ')
  
        
        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
        if(int(ord(b[0])) < 58 and int(ord(b[0])) > 47):
            cv.rectangle(img,(x,Height-y),(w,Height-h),(0,0,255),1)
    
    return img


###Inverts the Image


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

def OrganizeInfo(info):
    info = info.upper()

    info = info.replace('\n'," ")
    WORDLIST = info.split(' ')
    val = ''
    
    try: 
        while True:
            WORDLIST.remove(val)
    except ValueError:
        pass
    try: 
        while True:
            WORDLIST.remove('E')
    except ValueError:
        pass
    try: 
        while True:
            WORDLIST.remove('|')
    except ValueError:
        pass
    for i in range(len(WORDLIST)):
        
        if ',' in  WORDLIST[i] and len(WORDLIST[i])< 7:
            WORDLIST[i] = WORDLIST[i].replace(',','.')
            
    
    print(WORDLIST)
    return WORDLIST
#resizes the image
def PriceofItems(WORDLIST,NumItems, Total):
    
    i = j = 0
    Prices = []
    for i in range(len(WORDLIST)):
        string = WORDLIST[i]
        try:
        #if it is an integer 
           
            if(float(WORDLIST[i]) or WORDLIST[i] == '0.00'):
         #Finding if the value has a decimal
              if(WORDLIST[i].find('.') != -1):
                    item = float(WORDLIST[i])
                    item = "{:.2f}".format(item)
                    Prices.append(item)
                    
              else:
                continue
            else:
                continue
        except ValueError:
            continue
    if str(Total) in Prices:
        Prices.remove(str(Total))
        Prices = Prices[:int(NumItems)+1]
    print(Prices)
    return Prices
def NameofItems(WORDLIST,Prices):
    ItemNames = []
    i = 0
    for i in range(len(Prices)):
        if(str(Prices[i]) in WORDLIST):
            index = WORDLIST.index(str(Prices[i]))
            ItemNames.append(WORDLIST[index-1])
        if(Prices[i] == 0.0):
            index = WORDLIST.index('0.00')
            ItemNames.append(WORDLIST[index-1])
    print('Items are:',ItemNames)
    return ItemNames
    
def Questionare(WORDLIST, Prices, NumofItems, ItemNames):
    NumofItems = int(NumofItems)
    Totals = {'Matt':[0], 'Sahil': [0],'Tim':[0],'Adrian':[0] } 
    i = 0
    print(Totals)
    #Row 0 = Matt
    #Row 1 = Tim
    #Row 2 = Sahil
    #Row 3 = Adrian
    for i in range(NumofItems+1):
        print(f"Who paid for {ItemNames[i]}: {Prices[i]}")
        payment = input()
        payment = sorted(payment)
        if(len(payment)== 0):
            break
        owed = float(Prices[i])/len(payment)
        if('M' in payment or 'm' in payment):
            Totals['Matt'].append(owed)

        if('T' in payment or 't' in payment):
            Totals['Tim'].append(owed)
        if('S' in payment or 's' in payment):
            Totals['Sahil'].append(owed)
        if('A' in payment or 'a' in payment):
            Totals['Adrian'].append(owed)

    print(f"Matt Owes: {sum(Totals['Matt']) }")
    print(f"Tim Owes: {sum(Totals['Tim']) }")
    print(f"Sahil Owes: {sum(Totals['Sahil']) }")
    print(f"Adrian Owes: {sum(Totals['Adrian'])}")
    
    print(Totals)
    
    return Totals
       
def avg(img):
    average_color1 = np.average(img, axis = 0)
    average_color = np.average(average_color1,axis = 0)
    print(average_color)
    return average_color
#CODE Begins

average_color2 = avg(img)
img = invimg(img,average_color2)
small_img = resize_image(img,.4)


#changing color of image (type)
small_img = cv.cvtColor(small_img,cv.COLOR_BGR2RGB)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

info = pytesseract.image_to_string(img)

#grabs information from image
#print(info)
print("Before Wordlist")
WORDLIST = OrganizeInfo(info)

NumofItems = WORDLIST[WORDLIST.index('SOLD:')+11]
Total = float(WORDLIST[WORDLIST.index('SUBTOTAL')+1]) + float(WORDLIST[WORDLIST.index('TAX')+1])
print("The Total of this trip was: ",Total)
print("Number of Items is:", NumofItems)
Prices = PriceofItems(WORDLIST,NumofItems,Total)
ItemNames = NameofItems(WORDLIST,Prices)
Totals = Questionare(WORDLIST,Prices,NumofItems, ItemNames)

#drawing boxes
img = boximg(img)
small_img = boximg(small_img)


#Finding Number of Items 
#TotalItems = FindTotal(img)
#print("The total Number of Items is:",TotalItems)

cv.imshow('Reciept',small_img)
cv.waitKey(0)

