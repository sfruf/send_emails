import pytest
import send_email

# Functionality that I want to test 
# load email and password from a .env file (test+pass)
# connect to gmail using smtp
# send a message
# read a class list from a .csv file
# read class information from .csv 
# send emails in the future
# batch set up a week of emails

#TODO:
# Write smtp test
# Write a send message test


#check that there is a variable named sender 
#def test_env_load():
#    with pytest.raises(NameError,match='SENDER'):
#       send_email.send_email()
#Notes 5/16/22: once I started trying to write the code that would fail this test, I realized that it's a bit silly
#Essentially you need to write bad code (which uses a variable I know doesn't exist) to get the error
# 5/17/22: Removing it not that this passed since any future version of the code will fail this test 

#Check that after you load SENDER, that it's a gmail.com address
def test_sender_gmail():
    sender,password=send_email.load_cred()
    assert 'gmail.com' in sender

