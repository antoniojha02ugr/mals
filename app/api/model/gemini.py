import google.generativeai as genai

class Gemini:
    """
    This class represents a wrapper for the Gemini language model using the GenAI library.

    **Important Security Note**

    This code snippet reads an API key directly from a file located outside the project's directory. 
    Storing API keys in plain text files is a security risk. It's highly recommended to use a more secure method for storing and retrieving API keys, such as environment variables or a dedicated secrets manager.
    """

    def __init__(self):
        """
        Initializes the Gemini class with the correspondent model.
        """

        # Read the API key from a file outside the project directory (path begins from main.py location at execution time) and remove whitespaces and new line characters
        with open('../../../keys/gemini.txt', 'r') as file:
            key = file.read()

        key = key.strip()

        # Authenticate in the GenAI API using the key
        genai.configure(api_key=key)

        # Create the instance of the gemini-1.0-pro model
        self._model_ = genai.GenerativeModel('gemini-1.0-pro')

    def run(self, inpt: str):
        """
        Runs the Gemini model on the provided input text and generates text.

        Args:
            inpt (str): The input text to start the generation.

        Returns:
            str: The generated text based on the input.
        """

        return self._model_.generate_content(inpt).text