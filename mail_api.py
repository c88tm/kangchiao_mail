#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailSender(object):
    def __init__ (self,mail_list):
        self.mail_host= "smtp.gmail.com"  
        self.mail_user= "6@gmail.com" # Gmail 信箱
        self.mail_pass= "" # 密碼
        self.sender = '36@gmail.com' # 信箱名
        self.receivers = mail_list
    def send(self):
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(self.mail_host, 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(self.mail_user,self.mail_pass)  
            print "成功登入"
            smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            print "恭喜您成功寫完聯絡簿"
        except smtplib.SMTPException:
            print "嗚嗚 聯絡簿發不出去QAQ"
    
    def write_message(self,mail_msg,date):
        self.message = MIMEText(mail_msg, 'plain', 'utf-8')
        self.message['From'] = Header("陳佳佑", 'utf-8')
        self.message['To'] =  Header("學生家長", 'utf-8')
        subject = date+' 陳佳佑班課程進度及學生學習狀況'
        self.message['Subject'] = Header(subject, 'utf-8')
