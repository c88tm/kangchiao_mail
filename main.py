#!/usr/bin/python
# -*- coding: UTF-8 -*-
from mail_api import MailSender
import ConfigParser
msg_template ="""
親愛的家長您好：
 
我是資訊奧林匹亞G8班老師蔡毓聰。
每次課程進度和學生學習狀況寄送給您，讓您了解貴子弟在奧林匹亞班學習狀況。

學生：{a[name]}
本週上課進度：{a[study]}
本週小考： {a[quiz]}
本週作業：{a[homework]}
出席狀況：準時
上課態度：{a[attitude]}
學習狀況：{a[studycase]}
特殊狀況報告：無

{a[specialword]}

敬祝
順心如意

毓聰 敬上
"""

config = ConfigParser.ConfigParser()
config.read('mail.cfg')
for section in config.sections():
    if section in 'DEFAULT':
        continue
    student = {'name':section}
    for attr in ['quiz','study','studycase','attitude','date','homework','specialword','email_list']:
        student[attr] = config.get(section,attr,vars={})
    msg = msg_template.format(a = student)

    print "Demo"
    print "==================================="
    print msg
    print "==================================="
    print student['email_list'].split()
    while True:
        ans = raw_input('要寄出嗎 (y/n): ')
        if ans in 'yn':
            break
        print "請輸入 y 或 n"
    if ans in 'n':
        continue
    mailer = MailSender(student['email_list'].split())
    date = config.get('DEFAULT','date')
    mailer.write_message(msg,date)
    mailer.send()
