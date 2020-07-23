# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:36:22 2020

@author: ribau
"""
def send_email(receiver_email,subject,message):
    import smtplib, ssl
    import please_no_looky
    
    port=465
    smtp_server="smtp.gmail.com"
    sender_email="Pythonchallengetestemail@gmail.com"
    text = 'Subject: {}\n\n{}'.format(subject, message)
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        please_no_looky.very_secret_function(server,sender_email)
        server.sendmail(sender_email, receiver_email, text)





