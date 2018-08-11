import smtplib
from email.mime.text import MIMEText
from email.header import Header

message=MIMEText('Python testing\n','plain','utf8')
message['From']=Header('root','utf8')
message['To']=Header('bob@localhost','utf8')
message['Subject']=Header('mail teest','utf8')

sender='root@redhat.com'
recievers=['bob@localhost','alice@localhost']
smtp_obj=smtplib.SMTP('localhost')
smtp_obj.sendmail(sender,recievers,message.as_string())