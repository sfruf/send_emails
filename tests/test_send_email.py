import pytest
import send_email.py
# Functionality that I want to test 
# load email and password from a .env file
# connect to gmail using smtp
# send a message
# read a class list from a .csv file
# read class information from .csv 
# send emails in the future
# batch set up a week of emails

#TODO:
#I clearly don't know how to make two packages talk to each other. Tomorrow I need to move test_send_email and send_email into the same folder and go from there
#I'm not clear how to get send_email to run from this file either
#Actually write the code that raises a name error


#check that there is a variable named sender 
def test_env_load():
    with pytest.raises(NameError,match='SENDER'):
        send_email()
#Notes 5/16/22: once I started trying to write the code that would fail this test, I realized that it's a bit silly
#Essentially you need to write bad code (which uses a variable I know doesn't exist) to get the error


#Check that after you load SENDER, that it's a gmail.com address
#def test_sender_gmail():
#    send_email
#    assert sender contains 'gmail.com'

