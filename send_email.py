from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

import smtplib

import config





def send_email(subject,message):
	try:
		recipients = ['']
		cc = ['']
		bcc = ['']
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL_ADDRESS,config.PASSWORD)

		msg = MIMEMultipart('alternative')

		msg['Subject'] = subject
		msg['From'] = formataddr((str(Header('gmail', 'utf-8')), config.EMAIL_ADDRESS))
		msg['To'] = ", ".join(recipients)
		msg['Cc'] = ", ".join(cc)

		msg.attach(MIMEText(message,'html'))

		server.sendmail(config.EMAIL_ADDRESS, recipients + cc + bcc, msg.as_string())

		server.quit()
		print("Success Email Sent !")
		
	except Exception as e:
		print(e)
		print("Email Failed to send !")
	

subject = ''
msg = ''

send_email(subject,msg)	

