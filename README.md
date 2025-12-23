# AI Ollama Chatbot

A simple chatbot application built with Ollama and LangChain for local AI conversations. This project demonstrates basic integration with Ollama models and is designed to be extended for more advanced chatbot features.

## Features

- Local AI chatbot using Ollama models
- Integration with LangChain for easy model management
- Configurable model parameters (temperature, timeout)
- Virtual environment support for dependency management

## Prerequisites

- Python 3.10 or higher
- Ollama installed and running
- Git (for cloning the repository)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd ai-ollama-chatbot
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and setup Ollama:**
   - Download and install Ollama from [ollama.ai](https://ollama.ai)
   - Pull the required model:
     ```bash
     ollama pull gemma:2b
     ```
   - Start Ollama service

## Usage

1. Ensure Ollama is running
2. Activate the virtual environment
3. Run the chatbot:
   ```bash
   python main.py
   ```

The script will send a sample query to the AI model and print the response.

## Configuration

Modify `main.py` to:
- Change the model: Update the `model` parameter in `ChatOllama()`
- Adjust parameters: Modify `temperature`, `timeout`, etc.
- Customize prompts: Edit the `msg` list with your own system and user messages

## Project Structure

```
ai-ollama-chatbot/
├── main.py              # Main chatbot script
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── .venv/              # Virtual environment (not committed)
└── README.md           # This file
```

## Future Enhancements

- Interactive chat interface
- Support for multiple models
- Conversation history
- Web-based UI
- Integration with other AI services
- Custom model fine-tuning

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Support

For issues or questions:
- Check Ollama documentation
- Review LangChain docs
- Open an issue in the repository