# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:25:27 2020




import cv2
import numpy as np
import os
import pytesseract
import imutils
import re
import CheckingRecords
###############################################################################################################

#MAIN FUNCTION : START OF PROGRAM
def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    originalIMg = cv2.imread("images/img5.jpg")
    if(originalIMg is None):
        print("\n error reading image from file")
        os.system("pause")
        return
    else:
        cv2.imshow("original Image ",originalIMg)
        
    
    
    
    edgedImg,grayScaledImg = preprocess(originalIMg)
    cv2.imshow("Image after being processed ",edgedImg)
    
    
    
    numberPlateImg = findingNumberPlate(edgedImg,originalIMg,grayScaledImg)
    cv2.imshow("Number plate detected",numberPlateImg)
    cv2.imwrite('1.jpg',numberPlateImg)
    
    
    
    
    licenseNumber = findingLicenseNumber(numberPlateImg)
    licenseNumber = re.sub('[\W_]+','',licenseNumber)
    
    for i in range(1) :
        if(licenseNumber[i]=='6'):
            licenseNumber = licenseNumber.replace("6","G",1)
        if(licenseNumber[i]=='5'):
            licenseNumber = licenseNumber.replace("5","",1)
        
        
    
    print("The license number of the car is :",licenseNumber)
    
    
    charSegmentation(numberPlateImg)
    
    emailid = CheckingRecords.findUserDetails(licenseNumber)
    if(emailid!=""):
        CheckingRecords.sendNotification(emailid,licenseNumber)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
########################################################################################################    
 
#FUNCTION WHERE IMAGE IS CONVERTED INTO GRAYSCALE AND IS FILTERED TO REMOVE NOISE AND IS CONVERTED INTO AN EDGED IMAGE
def preprocess(image):
        imgGrayScaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        imgBlurred = cv2.GaussianBlur(imgGrayScaled, (5, 5), 0)
        imgFiltered = cv2.bilateralFilter(imgBlurred, 11, 17, 17)
        c_edge = cv2.Canny(imgFiltered, 170, 200)
        
        return c_edge,imgFiltered
    
##########################################################################################################    
   # FUNCTION FOR NUMBER PLATE LOCALIZATION 
     
def findingNumberPlate(imageEdged,originalImg,grayImage):
    cnt, new = cv2.findContours(imageEdged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnt = sorted(cnt, key = cv2.contourArea, reverse = True)[:30]
    NumberPlateCount = None
    im2 = originalImg.copy()
    cv2.drawContours(im2, cnt, -1, (0,255,0), 3)
    cv2.imshow("winname", im2)
    count =0 
    for c in cnt:

        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
        

        if len(approx) == 4:
            NumberPlateCount = approx
            count+=1

            break

    print(count)        
    x,y,w,h = cv2.boundingRect(NumberPlateCount)
    masked = np.zeros(grayImage.shape,np.uint8)
    new_image = cv2.drawContours(masked,[NumberPlateCount],0,255,-1)
    new_image = cv2.bitwise_and(originalImg,originalImg,mask=masked)
    new_image = new_image[y:y+h,x:x+w]
    return new_image

###########################################################################################################

#FUNCTION TO GET THE FINAL LICENSE NUMBER
    
def findingLicenseNumber(image):
    configr = ('-l eng --oem 1 --psm 3')
    
    text_char = pytesseract.image_to_string(image, config=configr)
    if(text_char==""):
        text_char = "not found"
    
    
    return text_char

###########################################################################################################
  
    # SEGMENTING CHARACTERS FROM NUMBER PLATE
def charSegmentation(img):
    
    img = imutils.resize(img,width=300)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    #cv2.imshow('gray', gray)
    
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    
    kernel = np.ones((2,2), np.uint8)
    
    img_erode = cv2.erode(thresh, kernel, iterations = 1)
    img_dilate = cv2.dilate(img_erode, kernel, iterations = 1)
    
    #cv2.imshow('img_erode', img_erode)
    cv2.imshow('img_dilate', img_dilate)
    
    ctrs, hier = cv2.findContours(img_dilate.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr))
    
    number_plate = ""
    
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
    
        roi = img[y:y + h, x:x + w]
    
        area = w*h
        #print("ef",area)
        
    
        if 250 < area < 1500:
            #print(area)
            new_img=img[y:y+h,x:x+w].copy()
            rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            new_img = imutils.resize(new_img,width=50,height=50)
           # cv2.imshow("winname", new_img)
            #cv2.imwrite("1.jpg",new_img)
            #cv2.waitKey(0)
           
            
            
            
    
    
    cv2.imshow('rect', rect)
    print(number_plate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
##############################################################################################################
    
if __name__ == "__main__":
    main()
    

   
