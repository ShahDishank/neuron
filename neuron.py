import streamlit as st
import time
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

st.set_page_config(
    page_title="Neuron",
    page_icon="media_files/ai.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'mailto:shahdishank24@gmail.com',
        'Report a bug': "mailto:shahdishank24@gmail.com",
        'About': "**Hi 👋, I am Neuron**"
    }
)

def stream_data(prompt):
    for word in prompt.split(" "):
        yield word + " "
        time.sleep(0.04)

chat = ""
def download():
    global chat
    for m in st.session_state.messages:
        if m["role"] == "user":
            chat += "User: "+m["content"]+"\n\n"
        else:
            chat += "Neuron: "+m["content"]+"\n\n"


img_path = "media_files/home_img.svg"
with open(img_path, 'r') as f:
    img = f.read()
st.sidebar.image(img, use_column_width=True)

st.sidebar.write("")
with st.sidebar.expander("**Desclaimer**", expanded=False):
    st.markdown("""
        - The chat history will not be saved and automatically cleared after refreshing or closing the website.
        """
        )


st.markdown("""
<h1 style="text-align:center">Neuron</h1>
""",
unsafe_allow_html=True)

con = st.container(height=440)

initial_user_msg = "Your Name is Neuron and you are a helpful assistant."
initial_assistant_msg = "Ok! Neuron is ready to help you. Please tell me what you need, and I'll do my best to answer."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "user", "content": initial_user_msg}, {"role": "assistant", "content": initial_assistant_msg}]

for message in st.session_state.messages:
    if message["role"] == "user" and message["content"] == initial_user_msg:
        pass
    elif message["role"] == "assistant" and message["content"] == initial_assistant_msg:
        pass
    elif message["role"] == "user":
        with con.chat_message(message["role"], avatar="media_files/user.png"):
            st.write("**You**")
            st.text(message["content"])
    else:
        with con.chat_message(message["role"], avatar="media_files/ai.png"):
            st.write("**Neuron**")
            st.markdown(message["content"])

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

openai = OpenAI(
    api_key=HUGGINGFACE_API_TOKEN,
    base_url="https://api-inference.huggingface.co/v1",
)

tokens = st.sidebar.slider("max_tokens", 1000, 5000, 3000)

msg = ""
if prompt:= st.chat_input("Ask to Neuron"):
    with con.chat_message("user", avatar="media_files/user.png"):
        st.write("**You**")
        st.text(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
    with con.chat_message("assistant", avatar="media_files/ai.png"):
        st.write("**Neuron**")
        with st.spinner('Generating response...'):
            chat_completion = openai.chat.completions.create(
                model="google/gemma-7b-it",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                temperature=0.5,
                max_tokens=tokens
            )
            res = chat_completion.choices[0].message.content
        ai_res = st.write_stream(stream_data(res))
        st.session_state.messages.append({"role": "assistant", "content": ai_res})

clear = st.sidebar.button("Clear Chat")
if clear:
    del st.session_state.messages
    st.rerun()

st.sidebar.download_button(
    on_click=download(),
    label="Download Chat",
    data=chat,
    file_name='chat_with_neuron.txt',
    mime='text'
)