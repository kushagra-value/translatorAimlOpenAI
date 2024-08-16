import os

# Configuration for the application

# OpenAI API key (you should set this as an environment variable for security)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")

# Function to validate if API key is present
def check_config():
    if not OPENAI_API_KEY or OPENAI_API_KEY == "your-default-api-key":
        raise ValueError("Please set the OPENAI_API_KEY in your environment or config.py file")

# Call this function at the start of your application to ensure everything is configured
check_config()
