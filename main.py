#!/usr/bin/python
# -*- coding: UTF-8 -*-
from mail_api import MailSender
msg_template ="""
親愛的家長您好：
 
我是資訊奧林匹亞G7班老師陳佳佑。
每次課程進度和學生學習狀況寄送給您，讓您了解貴子弟在奧林匹亞班學習狀況。
{specialword}

學生：{person[name]}
本週上課進度：{study}
本週小考： 無
本週作業：{homework}
出席狀況：準時
上課態度：{person[attitude]}
學習狀況：{person[studycase]}
特殊狀況報告：無


敬祝
順心如意

佳佑 敬上
"""

students = [
    {
        'name':'謝知我',
        'studycase':'優良',
        'attitude':'優良',
        'email':['b04611015@csie.ntu.edu.tw']},
    
    {
        'name' : '蔡嘉恩',
        'studycase':'優良',
        'attitude':'優良',
        'email':['b04611015@csie.ntu.edu.tw']},
    
    {
        'name' : '孫詠灝',
        'studycase':'優良',
        'attitude':'優良',
        'email':['b04611015@csie.ntu.edu.tw']}
    ]


homework =raw_input('請輸入作業: ')
study = raw_input('請輸入課程進度: ')
date = raw_input('日期: ')
for student in students:
    print "給 "+student['name']+" 的家長"
    special_word = ""

    while True:
        ans = raw_input('有沒有特別想對 '+student['name']+ ' 的家長說的話(y/n): ')
        if ans == "y":
            special_word=raw_input('請輸入想對家長說的話: ')
            print "輸入完成"
            break
        if ans == "n":
            break
        print "請輸入 y 或 n"
    
    while True:
        ans = raw_input('是否更改\"上課態度\"(預設 優良) (y/n): ')
        if ans == "y":
            student['attitude']=raw_input('請輸入上課態度評語: ')
            print "輸入完成"
            break
        if ans == "n":
            break
        print "請輸入 y 或 n"
   

    while True:
        ans = raw_input('是否更改\"學習狀況\"(預設 優良) (y/n): ')
        if ans == "y":
            student['attitude']=raw_input('請輸入學習狀況評語: ')
            print "輸入完成"
            break
        if ans == "n":
            break
        print "請輸入 y 或 n"
   

    msg = msg_template.format(person=student,homework=homework,study=study,specialword=special_word)

    print "Demo"
    print "==================================="
    print msg
    print "==================================="
    
    while True:
        ans = raw_input('要寄出嗎 (y/n): ')
        if ans in 'yn':
            break
        print "請輸入 y 或 n"
    
    if ans in 'n':
        continue
    
    mailer = MailSender(student['email'])
    mailer.write_message(msg,date)
    mailer.send()
