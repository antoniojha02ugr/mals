from transformers import pipeline, set_seed

class GPT2:
    """
    This class represents a wrapper for the GPT-2 language model using the huggingface's transformers library.
    """

    def __init__(self):
        """
        Initializes the GPT2 class with a pipeline for text generation using the GPT-2 model.
        """

        self.id = 'gpt2'

        self._model = pipeline('text-generation', model='gpt2')

    def run(self, inpt: str):
        """
        Runs the GPT-2 model on the provided input text and generates text.

        Args:
            inpt (str): The input text to start the generation.

        Returns:
            str: The generated text based on the input.
        """

        return self._model(inpt, num_return_sequences=1, max_length=100)[0]['generated_text']