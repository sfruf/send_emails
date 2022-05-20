import email
import os
from dotenv import load_dotenv, find_dotenv
from email.message import EmailMessage
import smtplib
import csv 

def load_cred():
    # find .env automagically by walking up directories until it's found
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    SENDER= os.environ.get("SENDER")
    PASSWORD = os.environ.get("PASSWORD")

    return SENDER,PASSWORD

def load_batch():
    # load class_list.txt and read classes, bodies
    with open('class_list.txt') as f:
        lines=f.readlines()
    classes=[]
    bodies=[]
    for line in lines:
        if line.strip():
            if "Hello" not in line:
                classes.append(line.strip())
            else:
                bodies.append(line.strip())

    return classes,bodies

def make_message(recipient, subject, body,SENDER=None):
    if "@" not in recipient:
        recipients=[]
        with open(f'{recipient}_emails.csv') as csvfile:
            emails=csv.reader(csvfile)
            for row in emails:
                recipients.append(row)
    else:
        recipients=recipient

    msg=EmailMessage()
    msg.set_content(body)
    msg["Subject"]=subject
    msg["From"]=SENDER 
    msg["To"]=recipients
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

def send_email(recipient="test",body="This is a test"):
    SENDER,PASSWORD=load_cred()
    msg=make_message(recipient, "Test", body,SENDER=SENDER)
    sent=connect_send(msg,SENDER=SENDER,PASSWORD=PASSWORD)
    return sent    

def batch_send():
    # Looks for a class_list.txt file and send emails to each of the classes
    classes,bodies=load_batch()
    sentcount=0
    for class1,body in zip(classes,bodies):
        sentcount+=send_email(recipient=class1,body=body)     
    return sentcount

if __name__=='__main__':
    sentcount=batch_send()
    print(sentcount)
