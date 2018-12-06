import win32com.client as win32
import warnings
import sys
import smtplib

warnings.filterwarnings('ignore')

def sendemail(sub,body):
    outlook = win32.Dispatch('outlook.application')
    receivers = ['572857852@qq.com','kalista.yuan@utstarcom.cn']
    mail = outlook.CreateItem(0)
    mail.To = receivers[0]
    mail.Subject = sub
    mail.Body = body
    # 添加附件
    # mail.Attachments.Add('D:\Users\xxx\Desktop\email.log')
    mail.Send()

#sendemail('aaa','bbb')
