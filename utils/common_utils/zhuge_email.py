# coding=utf-8

# 邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# from email import encoders
from email.header import Header
# from email.utils import parseaddr
from email.utils import formataddr
import smtplib
# import json
import traceback


# 发送邮件
def sendmail(title, content, from_email, to_emails, cc_emails=[], attachs=[]):
    # receivers = ['Lemon <lemon@zhugefang.com>','18610316376@qq.com']
    # receivers = to_emails.split(',')
    # if cc_emails != '':
    #   cc = cc_emails.split(',')
    #   receivers.extend(cc)
    # print receivers
    tos = ','.join(to_emails)
    ccs = ','.join(cc_emails)
    if len(cc_emails) > 0:
        to_emails.extend(cc_emails)

    # 创建一个带附件的实例
    message = MIMEMultipart()
    from_name = from_email.split('@')[0].upper()  # .capitalize()
    message['From'] = formataddr([from_name, from_email])
    message['To'] = tos
    message['Cc'] = ccs
    message['Subject'] = Header(title, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText(content, 'html', 'utf-8'))

    # 根据文件路径构造附件
    for x in attachs:
        filename = x.split("/")[-1]
        att1 = MIMEText(open(x, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = ('attachment; filename="%s"' % filename)
        message.attach(att1)

    try:
        port = 465
        smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', port)
        smtpObj.login('008@zhuge.com', 'Zhu1118')
        smtpObj.sendmail('008@zhuge.com', to_emails, message.as_string())
        print("send success")
    except Exception:
        print("send fail")
        traceback.print_exc()


if __name__ == '__main__':
    sendmail('这是标题', '<p>1111</p>', 'ci@zhugefang.com',
             ['sunbowen@zhuge.com', 'sunbowen@zhuge.com'], ['sunbowen@zhuge.com', 'sunbowen@zhuge.com'], [])
