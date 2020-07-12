import smtplib, ssl
import linkedInInfo

class Email():

    def __init__(self):
        self._port = 465
        self._smtpServer = "smtp.gmail.com"
        """
            Save senderEmail and receiverEmail in linkedInInfo.py as follows:
                senderEmail = your_senderEmail
                receiverEmail = yout_receiverEmail
        """
        self._senderEmail = linkedInInfo.senderEmail
        self._receiverEmail = linkedInInfo.receiverEmail

    def port(self): return self._port

    def smtpServer(self): return self._smtpServer

    def senderEmail(self): return self._senderEmail

    """
        Save emailPassword in linkedInInfo.py as follows:
            emailPassword = your_senderEmailPassword
    """
    def senderPassword(self): return linkedInInfo.emailPassword

    def receiverEmail(self): return self._receiverEmail


    def message(self):
        return """
            Hello human being,

            Test mail.
        """

    def send(self):
        print("Sending mail\n")
        server = smtplib.SMTP_SSL(self.smtpServer(), self.port())
        server.login(self.senderEmail(), self.senderPassword())
        server.sendmail(self.senderEmail(), self.receiverEmail(), self.message())
        server.quit()

