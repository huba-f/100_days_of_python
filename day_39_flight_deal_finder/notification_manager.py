from twilio.rest import Client
import smtplib

TWILIO_SID = "ACaabfffdbce4d6cb8426d1988720c0b88"
TWILIO_AUTH_TOKEN = "8b47b412d441be4193e0c1793a87e61f"
TWILIO_VIRTUAL_NUMBER = "+12674891940"
TWILIO_VERIFIED_NUMBER = "+xxxx"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, email, text):
        my_email = 'nyelrugosibakugan@gmail.com'
        my_password = 'xxxx'

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:new flight\n\n{text}")
