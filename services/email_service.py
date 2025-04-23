from flask_mail import Message
from flask import current_app
from extensions import mail
import os


class EmailSender:
    def __init__(self):
        self.mail = mail

    def send_application_email(self, subject, rec_sender):
        msg = Message(subject, sender= os.getenv('DEL_EMAIL'), recipients= [rec_sender])
        msg.body = "DENY APPLICATION EMAIL"
        self.mail.send(msg)
