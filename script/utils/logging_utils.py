# script/utils/logging_utils.py

import os
import logging

def configure_logging(log_directory):
    """Configure logging settings."""
    os.makedirs(log_directory, exist_ok=True)

    # Create a file handler
    file_handler = logging.FileHandler(os.path.join(log_directory, 'access_verifier.log'))
    file_handler.setLevel(logging.INFO)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
