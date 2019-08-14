from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

def send_email(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("自动化测试报告",'utf-8')

    smtp=smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("xxxx@qq.com","12345")
    smtp.sendmail("xxxx@qq.com","xxxx@qq.com",msg.as_string())
    smtp.quit()
    print('email has aend out')

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__=='__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './mooc/report/'+now+'result.html'
    fp=open(filename,'wb')
    runner = HTMLTestRunner(stream =fp,
                            title = '社区自动化测试报告',
                            description = '环境：windows 10 浏览器：Chrome')
    discover =unittest.defaultTestLoader.discover('./mooc/test_case',pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path=new_report('./mooc/report/')
    send_email(file_path)
