#!/usr/bin/python

import smtplib
import time


sender = 'tongnghi@gmail.com'
receiver = 'nghi.tongchau@trade.nguyenkim.com'
message = """ This email was sent from Raspberry  """
try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('tongnghi@gmail.com', 'ChethiQAZ123')

    smtpObj.sendmail(sender, receiver, message)
    smtpObj.quit()

    print "Successfully sent email"
except:
    print "This is an error message!"
