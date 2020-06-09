#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib

class Mail():
    
    def send(self, sender, password, subject, body, server='smtp.gmail.com', port=587):
        
        recipient = sender

        body = "" + body + ""

        headers = ["From: " + sender,
                   "Subject: " + subject,
                   "To: " + recipient,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        session = smtplib.SMTP(server, port)

        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(sender, password)

        session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
        session.quit()