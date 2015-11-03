from twilio.rest import TwilioRestClient
import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_DOWN)

def sendsms():
    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACCOUNT ID"
    AUTH_TOKEN = "AUTH TOKEN"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="Doorbell has been rung",  # Message body, if any
        to="NUMBER TO SMS",
        from_="YOUR TWILIO PHONE NUMBER",
    )
    print(message.sid)
    time.sleep(5)

while True:
    GPIO.wait_for_edge(17, GPIO.FALLING)
    sendsms()
        


