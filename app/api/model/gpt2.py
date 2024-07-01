from model.modeltemplate import ModelTemplate
from transformers import pipeline, set_seed

class GPT2(ModelTemplate):
    """
    This class represents a wrapper for the GPT-2 language model using the huggingface's transformers library.
    """

    def __init__(self):
        """
        Initializes the GPT2 class with a pipeline for text generation using the GPT-2 model.
        """

        self.id = 'gpt2'

        self._model = pipeline('text-generation', model='gpt2')

    def run(self, inpt: str, max_length: int, temperature: float, top_p: float, top_k: int):
        """
        Runs the GPT-2 model on the provided input text and generates text.

        Args:
            inpt (str): The input data for the model.
            max_length (int): Maximum number of tokes of the generated sequence.
            temperature (float): Temperature parameter for temperature sampling.
            top_p (float): nucleus sampling parameter, controls the cumulative probability.
            top_k (int): top-k sampling parameter, considers only the top k tokens.

        Returns:
            str: The generated text based on the input.
        """

        return self._model(inpt, num_return_sequences=1, max_new_tokens=max_length, temperature=temperature, top_p=top_p, top_k=top_k)[0]['generated_text'][len(inpt):]