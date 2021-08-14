import click
import datetime
import time
from emailer import send_email

@click.command()
@click.option('--receiver', default='', help='Email to send message to')
@click.option('--username', default='', help='Username of gmail account of sender')
@click.option('--password', default='', help='Password of gmail account of sender (Use single quotes to escape characters)')
def email(receiver, username, password):
    """
    Sends a pre-defined email to a recipient
    :param receiver: Person to receive the email
    :param username: Email address of user sending the email
    :param password: App password of gmail account
    :return:
    """
    while True:
        now_time = datetime.datetime.now().time()
        start = datetime.time(11, 0, 0)
        end = datetime.time(12, 0, 0)
        if start <= now_time <= end:
            send_email(username=username, receiver=receiver, password=password)
            time.sleep(3600)
            continue
        print('{}: Not within sending window {} - {}'.format(now_time,start,end))
        time.sleep(3600)
if __name__ == '__main__':
    email()