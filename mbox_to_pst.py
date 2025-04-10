import logging
import libpff

from pst_creator import create_pst
from mbox_parser import parse_mbox

def convert_mbox_to_pst(mbox_file, pst_filename):
    try:
        # Parse the .mbox file to get the list of emails
        mbox_folder = parse_mbox(mbox_file)

        # Create the PST file and add the emails
        create_pst(mbox_folder, pst_filename)
        logging.info(f"Conversion complete: {pst_filename}")
    except Exception as e:
        logging.error(f"Error during conversion: {str(e)}")
        raise
