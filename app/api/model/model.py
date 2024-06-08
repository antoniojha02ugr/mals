from model.gpt2 import GPT2
from model.llama2 import Llama2
from model.gemini import Gemini

class Model:
    """
    This class provides an abstraction for handling different language models.
    """

    def __init__(self):
        """
        Initializes the Model object.

        The internal model is initially set to None. You need to call the `load` method to load a specific model.
        """

        self._model_ = None  # Internal model variable (initially None)

    def load(self, id: str):
        """
        Loads a specific model based on the provided identifier.

        Args:
            id (str): The identifier for the model to be loaded.

        Returns:
            bool: True if the id corresponds to a correct model, False otherwise.
        """

        if id == 'gpt2':
            self._model_ = GPT2()
        elif id == 'llama2':
            self._model_ = Llama2()
        elif id == 'gemini':
            self._model_ = Gemini()
        else:
            return False

        return True

    def run(self, inpt: str):
        """
        Runs the loaded model on the provided input data.

        Args:
            inpt: The input data for the model.

        Returns:
            str: The generated text based on the input. Output will be an empy string if there is no model selected.
        """
        
        if self._model_ != None:
            return self._model_.run(inpt)
        else:
            return ''