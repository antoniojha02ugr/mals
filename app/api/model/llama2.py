from model.modeltemplate import ModelTemplate
from llama_cpp import Llama

class Llama2(ModelTemplate):
    """
    This class represents a wrapper for the Llama2 language model using the llama_cpp (python bindings for llama.cpp) library.

    **Key Point** 
    
    The model used here is a quantized version of Llama2, which means it has been optimized for smaller size and faster inference at the cost of some potential accuracy loss.
    """

    def __init__(self):
        """
        Initializes the Llama2 class with a quantized version of the model.
        """

        self.id = 'llama2'

        # Loads the model from the specified repository, the model is stored at virtual enviroment cache for future executions
        self._model = Llama.from_pretrained(repo_id="TheBloke/Llama-2-7B-Chat-GGUF", filename="llama-2-7b-chat.Q4_K_M.gguf", verbose=False, n_gpu_layers=-1)

    def run(self, inpt: str, max_length: int, temperature: float, top_p: float, top_k:int):
        """
        Runs the Llama2 model on the provided input text and generates text.

        Args:
            inpt (str): The input data for the model.
            max_length (int): Maximum number of tokes of the generated sequence.
            temperature (float): Temperature parameter for temperature sampling.
            top_p (float): nucleus sampling parameter, controls the cumulative probability.
            top_k (int): top-k sampling parameter, considers only the top k tokens.

        Returns:
            str: The generated text based on the input.
        """

        output = self._model(inpt, max_tokens=max_length, temperature=temperature, top_p=top_p, top_k=top_k)

        # llama_cpp generates completions in an OpenAI compatible format (using a dictionary)

        return output['choices'][0]['text']