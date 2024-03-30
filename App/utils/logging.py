import os
import logging
from logging.handlers import RotatingFileHandler
from .config import LOG_LEVEL


def setup_logging():
    """
    Create logs directory if it doesn't exist
    Configure logging
    """
    # Create logs directory if it doesn't exist
    logs_dir = 'logs'
    os.makedirs(logs_dir, exist_ok=True)

    # Configure logging
    log_file_path = os.path.join(logs_dir, 'operations.log')
    logging.basicConfig(
        level=LOG_LEVEL,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler(log_file_path, maxBytes=10000, backupCount=5),
        ]
    )

    logging.info("Logging setup complete.")