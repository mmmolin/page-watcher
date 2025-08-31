import smtplib
import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(subject, message):
    script_config = config.read_config()
    print(f'To: {script_config['email']}')
    print(f'Sending mail: {subject}')
    print(f'Message: {message}')