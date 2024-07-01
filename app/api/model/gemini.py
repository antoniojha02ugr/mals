from model.modeltemplate import ModelTemplate
import google.generativeai as genai

class Gemini(ModelTemplate):
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

        self.id = 'gemini'

        # Read the API key from a file outside the project directory (path begins from main.py location at execution time) and remove whitespaces and new line characters
        with open('../../../keys/gemini.txt', 'r') as file:
            key = file.read()

        key = key.strip()

        # Authenticate in the GenAI API using the key
        genai.configure(api_key=key)

        # Create the instance of the gemini-1.0-pro model
        self._model = genai.GenerativeModel('gemini-1.0-pro')

    def run(self, inpt: str, max_length: int, temperature: float, top_p: float, top_k: int):
        """
        Runs the Gemini model on the provided input text and generates text.

        Args:
            inpt (str): The input data for the model.
            max_length (int): Maximum number of tokes of the generated sequence.
            temperature (float): Temperature parameter for temperature sampling.
            top_p (float): nucleus sampling parameter, controls the cumulative probability.
            top_k (int): top-k sampling parameter, considers only the top k tokens.

        Returns:
            str: The generated text based on the input.
        """

        # Temperature cannot be greater than 2 in Gemini
        temperature = min(temperature, 2)

        config = genai.GenerationConfig(max_output_tokens=max_length, temperature=temperature, top_p=top_p, top_k=top_k)

        return self._model.generate_content(inpt, generation_config=config).text