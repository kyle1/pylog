from config import FROM_EMAIL, EMAIL_PASSWORD, TO_EMAIL
from mail import Email
from log import Log

log = Log()
log.add_info('hello')
log.add_error('car')
log.add_warning('universe')
log.add_info('world')

attachments = ['attachments/attachment1.txt', 'attachments/attachment2.txt', 'attachments/2020-01-21_nba_odds.csv']
email = Email(FROM_EMAIL, EMAIL_PASSWORD, TO_EMAIL, 'pylog test', log.html_email_body, attachments)
