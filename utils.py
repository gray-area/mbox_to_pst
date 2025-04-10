import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def log(message):
    """Log a message to the console."""
    logging.info(message)

def check_pst_exists(pst_file):
    """Check if the PST file exists."""
    return os.path.exists(pst_file)
