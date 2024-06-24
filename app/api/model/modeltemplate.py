from abc import ABC, abstractmethod

class ModelTemplate(ABC):
    """
    Interface to force models to have the same methods to be used by the Model class.
    """

    @abstractmethod
    def __init__(self):
        """
        Abstract method: Default constructor, initializes the model and other attributes.
        """

        pass 

    @abstractmethod
    def run(self, inpt: str, max_length: int, temperature: float, top_p: float, top_k:int):
        """
        Abstract method: Runs the model on the given input using specified parameters.

        Args:
            inpt (str): The input data for the model.
            max_length (int): Maximum number of tokes of the generated sequence.
            temperature (float): Temperature parameter for temperature sampling.
            top_p (float): nucleus sampling parameter, controls the cumulative probability.
            top_k (int): top-k sampling parameter, considers only the top k tokens.

        Returns:
            str: The generated text based on the input.
        """
        pass