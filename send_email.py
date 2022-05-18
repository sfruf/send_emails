import os
from dotenv import load_dotenv, find_dotenv
from email.message import EmailMessage
import smtplib

def load_cred():
    # find .env automagically by walking up directories until it's found
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    SENDER= os.environ.get("SENDER")
    PASSWORD = os.environ.get("PASSWORD")

    return SENDER,PASSWORD

def make_message(recipient, subject, body,SENDER=None):
    msg=EmailMessage()
    msg.set_content(body)
    msg["Subject"]=subject
    msg["From"]=SENDER 
    msg["To"]=recipient
    return msg

def connect_send(msg,SENDER=None,PASSWORD=None):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    try:
        server.login(SENDER, PASSWORD)
        server.send_message(msg)
        server.quit()
        sent=True
    except:
        sent=False
    return sent

def send_email():
    SENDER,PASSWORD=load_cred()
    msg=make_message(SENDER, "Test", "This is a test",SENDER=SENDER)    
    #send some email stuff here

if __name__=='__main__':
    send_email()
