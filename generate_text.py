# Install necessary libraries
# pip install transformers torch

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT model and tokenizer
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_text(prompt, max_length=100):
    """
    Generate text based on the input prompt using GPT-2 model.
    
    Args:
    prompt (str): The input text prompt.
    max_length (int): The maximum length of the generated text.
    
    Returns:
    str: The generated text.
    """
    try:
        # Encode the input prompt
        inputs = tokenizer.encode(prompt, return_tensors='pt')

        # Generate text
        outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, early_stopping=True)

        # Decode the generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return generated_text
    except Exception as e:
        return f"An error occurred: {e}"

# User prompt
prompt = "The future of artificial intelligence is"

# Generate text
generated_text = generate_text(prompt)

# Print the generated text
print("Generated Text:\n", generated_text)
