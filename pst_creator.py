import libpff

def create_pst(emails, pst_file):
    """Create a PST file and add emails."""
    pst = libpff.file()
    pst.open(pst_file, 'w')
    
    root = pst.get_root_folder()
    
    # Create folder and add emails
    folder = root.create_sub_folder('Inbox')
    
    for email in emails:
        message = folder.create_message()
        message.set_subject(email["subject"])
        message.set_sender(email["from"])
        message.set_recipient(email["to"])
        message.set_date(email["date"].strftime("%Y-%m-%d %H:%M:%S"))
        message.set_body(email["body"].decode('utf-8', errors='ignore'))
    
    pst.write()
    pst.close()
