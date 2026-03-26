#Integrate our code OpenAI API 

import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st ## we can also flask , but really realiable

os.environ["OPENAPI_API_KEY"] = openai_key

#streamlit framework

st.title('Langchain demo with with openai API')
input_text = st.text_input("search the topic u want")

#openai LLms
llm_model = OpenAI(temperature =0.8)  # how much control that agent can have 

if input_text:
    st.write(llm_model(input_text))