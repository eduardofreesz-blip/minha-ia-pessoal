import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class OllamaAI:
    def __init__(self):
        pass

    def run_command(self, command):
        """Run a shell command and return the output."""
        try:
            logging.info(f'Running command: {command}')
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            logging.info('Command output: %s', result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error('An error occurred while running command: %s', e)
            return None

    def ExampleUsage(self):
        # Example usage of the run_command method
        output = self.run_command('echo "Hello from Ollama AI!"')
        if output is not None:
            logging.info(output)
        else:
            logging.error('Command failed.')
