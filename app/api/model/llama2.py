from llama_cpp import Llama

class Llama2:
    """
    This class represents a wrapper for the Llama2 language model using the llama_cpp (python bindings for llama.cpp) library.

    **Key Point** 
    
    The model used here is a quantized version of Llama2, which means it has been optimized for smaller size and faster inference at the cost of some potential accuracy loss.
    """

    def __init__(self):
        """
        Initializes the Llama2 class with a very quantized version of the model.
        """

        # Loads the model from the specified repository, the model is stored at virtual enviroment cache for future executions
        self._model_ = Llama.from_pretrained(repo_id="TheBloke/Llama-2-7B-Chat-GGUF", filename="llama-2-7b-chat.Q3_K_M.gguf", verbose=False)

    def run(self, inpt: str):
        """
        Runs the Llama2 model on the provided input text and generates text.

        Args:
            inpt (str): The input text to start the generation.

        Returns:
            str: The generated text based on the input.
        """

        output = self._model_(inpt)

        # llama_cpp generates completions in an OpenAI compatible format (using a dictionary)

        return output['choices'][0]['text']