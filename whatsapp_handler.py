import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class WhatsAppHandler:
    def __init__(self):
        # Initialize handler
        logging.info('WhatsAppHandler initialized')

    def send_message(self, recipient, message):
        logging.info(f'Sending message to {recipient}')
        try:
            # Logic to send message
            logging.info('Message sent successfully')
        except Exception as e:
            logging.error(f'Error sending message: {e}')

    def receive_message(self):
        logging.info('Listening for messages...')
        try:
            # Logic to receive messages
            pass
        except Exception as e:
            logging.error(f'Error receiving message: {e}')

    def handle_error(self, error):
        logging.error(f'An error occurred: {error}')
        # Additional error handling logic

# Example usage
if __name__ == '__main__':
    handler = WhatsAppHandler()
    handler.send_message('1234567890', 'Hello, WhatsApp!')