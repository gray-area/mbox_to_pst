import os
from mbox_parser import parse_mbox
from pst_creator import create_pst
from utils import check_pst_exists, log

def mbox_to_pst(mbox_file, pst_file):
    # Check if PST file already exists
    if check_pst_exists(pst_file):
        log(f"PST file already exists: {pst_file}")
        return
    
    # Parse the MBOX file
    log(f"Parsing MBOX file: {mbox_file}")
    emails = parse_mbox(mbox_file)
    
    # Create the PST file and add emails
    log(f"Creating PST file: {pst_file}")
    create_pst(emails, pst_file)
    log(f"Conversion complete: {pst_file}")

if __name__ == "__main__":
    # Example usage: python convert_mbox_to_pst.py mbox_file pst_file
    mbox_file = "example.mbox"
    pst_file = "output.pst"
    mbox_to_pst(mbox_file, pst_file)
