import smtplib
import ssl
import os

class Informer:

    mail_adress = ""
    password = ""
    receiver = ""

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    CREDENTIALS = os.path.join(THIS_FOLDER, 'credentials.txt')

    with open(CREDENTIALS, "r") as credentials_file:
        mail_adress = credentials_file.readline()
        password = credentials_file.readline()
        receiver = credentials_file.readline()

    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login(mail_adress, password)

    def mail(self, content : list, kommun: str, omrade: str):
        message = "Subject: New listings for "+omrade+", "+kommun+"\n\n"+"""
            """+"following links lead to the new listings: \n"+str(content)
        self.server.sendmail(self.mail_adress, self.receiver, message)
        self.server.close