from transformers import GPT2Tokenizer, GPT2LMHeadModel

class GPT2:
    """
    This class represents a wrapper for the GPT-2 language model using the huggingface's transformers library.
    """

    def __init__(self):
        """
        Initializes the GPT2 class with the pre-trained GPT-2 tokenizer and model.
        """

        # Tokenizer used to convert text into numerical representations used by GPT-2
        self._tokenizer_ = GPT2Tokenizer.from_pretrained("gpt2")

        # GPT-2 original model with a head for language modeling
        self._model_ = GPT2LMHeadModel.from_pretrained("gpt2")

    def run(self, inpt: str):
        """
        Runs the GPT-2 model on the provided input text and generates text.

        Args:
            inpt (str): The input text to start the generation.

        Returns:
            str: The generated text based on the input.
        """

        # Encode the input text using the tokenizer, converting it into token IDs
        inpt_t = self._tokenizer_.encode(inpt, return_tensors='pt')

        # Generate text using the model based on the encoded input
        output = self._model_.generate(inpt_t)

        # Decode the generated output tokens into text, skipping special tokens like padding
        output_text = self._tokenizer_.decode(output[0], skip_special_tokens=True)

        return output_text