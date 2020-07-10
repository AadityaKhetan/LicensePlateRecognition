# LicensePlateRecognition

A license Plate Recognition Application using Image Processing in Python.

Main Libraries used - OpenCV, Pytesseract, SMTPlib, mysql.connector

This application extracts the number plate Region from the raw, original car image and then the pytesseract module converts the image of Number plate into a string.

Therefore getting the license plate number as a string.

License Plate number is then searched in the dummy rto Database and a real time e-mail is sent to the car owner using SMTPlib.  

