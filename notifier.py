import smtplib
import config
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(subject, message):
    script_config = config.read_config()
    password = os.environ.get('EMAIL_PASSWORD')
    if password is None:
        raise ValueError('Missing EMAIL_PASSWORD env variable')
    
    with smtplib.SMTP(script_config['smtp_server'], script_config['smtp_port']) as server:
        server.starttls()
        server.login(script_config['from_email'], password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = script_config['from_email']
        msg['To'] = script_config['to_email']
        server.sendmail(script_config['from_email'], script_config['to_email'], msg.as_string())
