from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from PIL import ImageGrab
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


# 邮件正文是MIMEText:
msg = MIMEMultipart()
import os,time
import smtplib

os.popen("D:\常用软件\TeamViewe12\TVClientID.exe")
time.sleep(60)

# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
bbox = (0, 0, 1440, 900)
im = ImageGrab.grab(bbox)
# 参数 保存截图文件的路径
im.save('as.png')

# 输入Email地址和口令:
#from_addr = input('From: ')
from_addr = "572857852@qq.com"
#password = input('Password: ')
password = "gkbcpagewyjsbege"
# 输入收件人地址:
#to_addr = input('To: ')
to_addr = "572857852@qq.com"
# 输入SMTP服务器地址:
#smtp_server = input('SMTP server: ')
smtp_server = "smtp.qq.com"

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('TeamViewer地址', 'utf-8').encode()

with open('C:\\Users\\utsc0990\\Desktop\\startup_Script\\as.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='as.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='as.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)


server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
