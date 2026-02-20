import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class MemoryManager:
    def __init__(self, filename='memory.json'):
        self.filename = filename
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_memory(self):
        with open(self.filename, 'w') as f:
            json.dump(self.memory, f)

    def update_memory(self, key, value):
        self.memory[key] = value
        self.save_memory()

class WhatsAppIntegration:
    def __init__(self):
        self.memory_manager = MemoryManager()

    def send_message(self, message, contact):
        try:
            logging.info(f'Sending message to {contact}: {message}')
            # Here would be the code to integrate with WhatsApp API
            # For example: whatsapp_api.send(contact, message)

            # Simulated success response
            self.memory_manager.update_memory(contact, message)
            logging.info('Message sent successfully.')
        except Exception as e:
            logging.error('Error sending message', exc_info=e)

    def receive_message(self, message, contact):
        logging.info(f'Received message from {contact}: {message}')
        # Process received message

# Example usage
whatsapp_integration = WhatsAppIntegration()
whatsapp_integration.send_message('Hello, this is a test message!', '+1234567890')
