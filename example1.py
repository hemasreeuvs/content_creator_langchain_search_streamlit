#Integrate our code OpenAI API 

#understand prompts
#understand chains
#understand main.py code

import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langachin.memory import ConversationBufferMemory

import streamlit as st ## we can also flask , but really realiable

os.environ["OPENAPI_API_KEY"] = openai_key

#streamlit framework

st.title('Conten creator search results')
input_text = st.text_input("search the topic u want")



#prompt template
first_input_prompt = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me about  famous {name}"

)
llm = OpenAI(templerature = 0)
chain1= LLMChain(llm=llm , prompt= first_input_prompt , verbose = True , output_key = 'title')



#prompt template
second_input_prompt = PromptTemplate(
    input_variables = ['born'],
    template = " when was the content creator {born}"

)

chain2 = LLMChain(llm=llm , prompt= first_input_prompt , verbose = True , output_key = 'dob')

parent_chain = SimpleSequentialChain(chains =[chain1,chain2], input_variables =['name'], output_variables = ['name','dob'],verbose = True)


third_input_prompt = PromptTemplate(
    input_variables = ['name'],
    template = " mention 5 major events happened around {dob} in the world"

)

chain3 = LLMChain(llm=llm , prompt= third_input_prompt , verbose = True , output_key = 'description')



parent_chain = SequentialChain([chain1,chain2,chain3], input_variables =['name'], output_variables = ['name','dob','description'],verbose = True)

#memory

name_memory = ConversationBufferMemory(input_key = 'name' , memory_key = 'chat_history')
dob_memory = ConversationBufferMemory(input_key = 'dob' , memory_key = 'chat_history')
person_memory = ConversationBufferMemory(input_key = 'description' , memory_key = 'description_history')


#openai LLms
llm_model = OpenAI(temperature =0.8)  # how much control that agent can have 
chain1= LLMChain(llm=llm , prompt= first_input_prompt , verbose = True , output_key = 'title' , memory = name_memory)
 

if input_text:
    st.write(llm_model(input_text)) # chain.run


if input_text:
    st.write(parent_chain ({'name': input_text})) # chain.run