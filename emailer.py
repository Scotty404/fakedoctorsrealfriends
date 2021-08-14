import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import logging
import os
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def send_email(username, receiver, password):
    """
    Method sets up gmail smtp connection and sends email
    :param username: Email address of user sending the email
    :param receiver: Person to receive the email
    :param password: App password of gmail account
    :return:
    """
    message = set_up_message(username, receiver)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.ehlo()
            server.login(username, password)
            server.sendmail(username, receiver, message.as_string())
            logger.debug('Mail Sent')
    except Exception:
        logger.debug('Exception thrown when connecting to or sending email', exc_info=True)

def set_up_message(username,receiver):
    """
    Method sets up MIME message for the emailer
    :param username: Email address of user sending the email
    :param receiver: Person to receive the email
    :return: message object of MIME Multipart
    """
    message = MIMEMultipart()
    if os.path.isfile('realfriends.jpeg'):
        with open('realfriends.jpeg', 'rb') as pic:
            img = MIMEImage(pic.read())
        img.add_header('Content-ID', '<{}>'.format('realfriends.jpeg'))
        message.attach(img)
    # Image not available within repo
    message['From'] = username
    message['To'] = receiver
    message['Subject'] = 'Guest submission for Fake Doctors Real Friends'
    message.attach(MIMEText(email_body(), 'HTML'))
    return message


def email_body():
    """
    :return: Pre-defined email template
    """
    return """<html>
    <body>
    Hi Joelle,<br><br>
    
    Really loving the content you all are putting out and I have gone through some effort to hopefully
    be noticed in the thousands of emails you must received weekly! <br><br>
    
    So first, I would like to state as of writing this I am currently on episode 312 of the podcast so a
    little behind but gaining ground fast! I am listening during work, on walks with the dog and I just 
    received my Fake Doctors, Real Friends Squad tank top to really hit those workouts hard.<br><br>
    
    <img src="cid:realfriends.jpeg" width="200" height="300" alt=""><br>
    
    As far as questions go I hope I don't repeat anything that is in the future episodes:<br>
    1. This ones for Danl and Joelle, How is it interacting with Zach and Donald weekly and experiencing 
    their bro-mance or "Guy Love" from the start of the series until now?<br>
    2. For Donald Pitch Perfect is one of my go too feel good movies, How was is being
     in the first one? And Zach do you think would be able to direct, ie. control, Donald if he was
     given a big solo acapella scene.<br>
    3. (If I get to ask a sacred third question) I about to spend some time in California in the bay area, 
    what things must I do? and I promise whatever the answer is I'll go experience it. <br><br>
    
    If you guys are still running the worlds favourite part of the show where Zach and Donald fix my life,
    I would like them to give me advise on staying motivated on dieting and exercising. Currently, like a
    lot of people I last a couple of weeks being healthy and exercising, then a couple a weeks ordering food
    and drinking to undo everything. So what the real secret to actors getting in shape?<br><br>
    
    Lastly, I would like to admit I have cheated to send this mail and probably many more. I wrote a 
    script to help me get on the show. You can check out the code here: 
    https://github.com/Scotty404/fakedoctorsrealfriends <br><br>
    
    Big shout out to Bill for an amazing podcast. <br><br>
    
    Thanks,<br>
    Scott
    </body>
    </html>
    """