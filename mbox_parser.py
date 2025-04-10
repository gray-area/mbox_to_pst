import mailbox
from email.utils import parsedate_to_datetime

def parse_mbox(mbox_file):
    """Parse the MBOX file and return a list of emails."""
    emails = []
    
    mbox = mailbox.mbox(mbox_file)
    for message in mbox:
        email = {
            "subject": message["subject"],
            "from": message["from"],
            "to": message["to"],
            "date": parsedate_to_datetime(message["date"]),
            "body": message.get_payload(decode=True),
        }
        emails.append(email)
    
    return emails
