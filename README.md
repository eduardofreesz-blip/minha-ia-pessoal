# Minha IA Pessoal

## Documentation

### Architecture
This project is structured into several modules that facilitate the functionality and improve maintainability. The key modules are:

- **memory.py**: This module handles the memory management system of the AI, allowing it to remember and retrieve information.
- **ollama_ai.py**: This module integrates the Ollama AI functionalities.
- **whatsapp_handler.py**: This module manages interactions through WhatsApp, ensuring smooth communication.
- **logger_config.py**: This module is responsible for configuring the logging system to keep track of actions and errors.

### Usage Instructions
To use this project, simply clone the repository and ensure you have the necessary dependencies installed. You can start by running the main script which orchestrates the modules.

### Module Descriptions
1. **memory.py**: This module provides functionality for storing and retrieving data in a structured JSON format. Here's an example of how to use it:
   ```python
   from memory import Memory
   
   memory = Memory()
   memory.save_data("key", "value")
   data = memory.get_data("key")
   print(data)  # Output: value
   ```

2. **ollama_ai.py**: This module interacts with the Ollama services. Here's how to use it:
   ```python
   from ollama_ai import OllamaAI
   
   ai = OllamaAI()
   response = ai.get_response("Hello, how are you?")
   print(response)
   ```

3. **whatsapp_handler.py**: This module helps manage WhatsApp messages. Usage example:
   ```python
   from whatsapp_handler import WhatsAppHandler
   
   handler = WhatsAppHandler()
   handler.send_message("Hello World", "1234567890")
   ```

4. **logger_config.py**: This module sets up the logging configuration. Example usage:
   ```python
   from logger_config import setup_logging
   
   setup_logging()
   logging.info("This is an log message")
   ```

### JSON Memory Structure
The memory is structured as follows:
```json
{
   "key": "value"
}
```
Make sure to handle the memory data accurately to ensure the functionality of the AI.

## Troubleshooting
- Ensure all dependencies are installed and updated.
- Check the logs for any error messages that may indicate misconfigurations.
- If there's an issue with memory management, verify that memory.json file is accessible and writable.

For additional help, refer to the [issues section](https://github.com/eduardofreesz-blip/minha-ia-pessoal/issues) of the repository for community support and troubleshooting.
