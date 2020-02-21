import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders


class Email:
    def __init__(self, from_addr, from_password, to_addr, subject, body, files):
        self._from_address = None
        self._from_password = None
        self._to_address = None
        self._subject = None
        self._body = None
        self._mime_message = None
        self._files = None

        setattr(self, '_from_address', from_addr)
        setattr(self, '_from_password', from_password)
        setattr(self, '_to_address', to_addr)
        setattr(self, '_subject', subject)
        setattr(self, '_body', body)
        setattr(self, '_files', files)

        self._setup_message()
        self._attach_files()
        self._send_email()

    def _setup_message(self):
        mime_message = MIMEMultipart()
        mime_message['From'] = self._from_address
        mime_message['To'] = self._to_address
        mime_message['Subject'] = self._subject
        mime_message.attach(MIMEText(self._body, 'html'))
        setattr(self, '_mime_message', mime_message)

    def _attach_files(self):
        for f in self._files:
            with open(f, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-disposition', f'attachment; filename={f.split("/")[-1]}')
            self._mime_message.attach(part)

    def _send_email(self):
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(self._from_address, self._from_password)
        smtp_server.sendmail(self._from_address, self._to_address, self._mime_message.as_string())
        smtp_server.quit()



