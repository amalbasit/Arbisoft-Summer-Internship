
import logging

# 1. Basic Configuration
# Write a script that logs the following messages using logging:

# A debug message: "This is a debug message"

# An info message: "Starting program"

# A warning message: "Low disk space"

# An error message: "File not found"

# A critical message: "System crash imminent"

# Only use basicConfig(). Ensure all messages appear in a file.


logging.basicConfig(
    filename='q1.log', 
    filemode='w', 
    level=logging.DEBUG, 
    format = '%(asctime)s - %(name)s - %(filename)s - %(levelname)s - Line: %(lineno)d - %(message)s')

logging.debug("This is a debug message")
logging.info("Starting program")
logging.warning("Low disk space")
logging.error("File not found")
logging.critical("System crash imminent")