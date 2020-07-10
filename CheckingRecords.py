# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:41:50 2020

@author: Sanyukta
"""


import mysql.connector
import smtplib


def findUserDetails(platenumber):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "admin",
        database = "rto"
        )
    
    mycursor = mydb.cursor()
    
    sql = "Select email_id from vehicle_details where vehicle_no=%s"
    
    mycursor.execute(sql,(platenumber,))
    
    myresult = mycursor.fetchone()
    emailid = "{email_id}".format(email_id=myresult[0])
    print(emailid)
    return emailid

def sendNotification(emailid,platenumber):
    rto_emailid = ''
    rto_pass = ''
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
    
        smtp.login(rto_emailid,rto_pass)
        
        subject = "RTO email notice for illegal actions"
        body = f"Your car with number plate {platenumber} was found parked in a prohibited area. You thus now need to pay a fine of Rs 1000 at your local RTO office branch"
        msg = f"Subject : {subject} \n\n\n{body}"
        smtp.sendmail('aadityakhetan123@gmail.com',emailid,msg)
