
import logging

# 7. Create a Named Logger
# Create a logger named "app_logger" that:

# Logs messages to a file app.log

# Uses a format like: %(asctime)s - %(levelname)s - %(message)s

# Logs only messages INFO and above

# Write 3 log statements using this logger.


logger = logging.getLogger(__name__)
logger.setLevel('INFO')

file_handler = logging.FileHandler(filename='q4.log', mode='w')

file_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.info("This is an info statement.")
logger.warning("This is a warning statement.")
logger.error("This is an error statement.")
logger.critical("This is a critical statement.")