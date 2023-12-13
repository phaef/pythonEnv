# my_script.py

import os
from dotenv import load_dotenv

def load_credentials():
    """
    Load sensitive credentials from the .env file.
    """

    # Check if the .env file exists
    if not os.path.isfile('.env'):
        raise FileNotFoundError("The .env file is not found. Please create one.")

    # Load environment variables from .env
    load_dotenv()

    # Access the environment variables
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')

    return username, password

def main():
    """
    Main function to demonstrate using credentials loaded from .env.
    """
    try:
        # Load credentials
        username, password = load_credentials()

        print(f"The username is {username} and the password is {password}")
        
        # Your main application logic here

    except Exception as e:
        print(f"Error: {e}")
        # Handle the exception gracefully

if __name__ == "__main__":
    main()



