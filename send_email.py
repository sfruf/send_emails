import os
from dotenv import load_dotenv, find_dotenv

def load_cred():
    # find .env automagically by walking up directories until it's found
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    SENDER= os.environ.get("SENDER")
    PASSWORD = os.environ.get("PASSWORD")

    return SENDER,PASSWORD
    
def send_email():
    SENDER,PASSWORD=load_cred()    
    #send some email stuff here

if __name__=='__main__':
    send_email()
