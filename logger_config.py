import logging


def setup_logging(log_file='app.log'):
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


if __name__ == '__main__':
    setup_logging()  # Set up logging with default log file
