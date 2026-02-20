import json
import logging

# Configure logging
logging.basicConfig(filename='memory_management.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MemoryManager:
    def __init__(self, storage_file='memory_data.json'):
        self.storage_file = storage_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.storage_file, 'r') as file:
                self.data = json.load(file)
                logging.info('Data loaded successfully.')
        except FileNotFoundError:
            self.data = {}
            logging.warning('Storage file not found, starting with empty data.')
        except json.JSONDecodeError:
            self.data = {}
            logging.error('Storage file is corrupted, starting with empty data.')

    def save_data(self):
        try:
            with open(self.storage_file, 'w') as file:
                json.dump(self.data, file, indent=4)
                logging.info('Data saved successfully.')
        except Exception as e:
            logging.error(f'Error saving data: {e}')

    def get(self, key):
        return self.data.get(key, None)

    def set(self, key, value):
        self.data[key] = value
        self.save_data()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_data()
        else:
            logging.error(f'Key {key} not found.')