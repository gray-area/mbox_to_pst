import libpff
import logging

def create_pst(mbox_folder, pst_filename):
    try:
        # Create the PST file object
        pst = libpff.file()
        pst.create()

        # Create a root folder in the PST
        root_folder = pst.root_folder

        # Iterate through mbox files and add their emails to the PST
        for mbox_file in mbox_folder:
            for message in mbox_file.messages:
                email = root_folder.add_message(message)
                logging.info(f"Added message to PST: {email.subject}")

        # Save the created PST file
        pst.save(pst_filename)
        logging.info(f"Created PST file: {pst_filename}")
    except Exception as e:
        logging.error(f"Error creating PST file: {str(e)}")
        raise
