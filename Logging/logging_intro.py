import logging

# Basic Config

logging.basicConfig(level=logging.INFO,
                    filename='app.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(filename)s - %(levelname)s - Line: %(lineno)d - %(message)s')

logging.info('uh hello')

# Adding this comment to test branch
# Custom logger

logger = logging.getLogger(__name__)
logger.setLevel('CRITICAL')

file_handler = logging.FileHandler('test.log', mode = 'w')
logger.addHandler(file_handler)

file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(filename)s - %(levelname)s - Line: %(lineno)d - %(message)s')

file_handler.setFormatter(file_formatter)

logger.propagate = False

# logger.info('This is an info message')
logger.critical('This is a critical message')