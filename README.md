
# Neuron

Neuron, the dynamic chatbot crafted with Gemma LLM by Google from Hugging Face, offering intuitive interactions and insightful responses.

[Try Neuron](https://neur0n.streamlit.app)
## Environment Variables

To run this project, you will need to add the Hugging Face Read API Token as environment variable to your .env file

`HUGGINGFACE_API_TOKEN`

Get your Hugging Face API token from [Here](https://huggingface.co/settings/tokens)

## Run Locally

Clone the project

```bash
  git clone https://github.com/ShahDishank/neuron
```

Go to the project directory

```bash
  cd neuron
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Change st.secrets to os.getenv in neuron.py file

```python
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
# HUGGINGFACE_API_TOKEN = st.secrets["HUGGINGFACE_API_TOKEN"]
```

Run the program

```bash
  streamlit run neuron.py
```


## Tech Stack

**Frontend:** Streamlit

**LLM:** Gemma


## Resources Used

 - Gemma LLM
    - [Google Gemma Website](https://ai.google.dev/gemma/docs)
    - [Hugging Face Gemma Model](https://huggingface.co/google/gemma-7b-it)
## Feedback

If you have any feedback, please reach out to me at shahdishank24@gmail.com

## Author

- [@shahdishank](https://www.github.com/ShahDishank)

