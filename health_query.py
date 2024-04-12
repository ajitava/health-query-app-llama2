import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

def chatbot(question):
    model = Ollama(model='medllama2')
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a medical chatbot. Answer the question based on user's input only   "),
        ("user", "{input}")
    ])

    chain = prompt | model

    return chain.invoke({"input": question})

#Use Streamlit

st.title("General Health Query")
st.write("Ask a question below related to your health")
st.write("**Please note that this is an AI generated answer and you should consult a prescribed doctor for diagnosis and treatment.**")

#Input Fields
question = st.text_input("Question")

if st.button('Submit'):
    answer = chatbot(question)
    st.text_area("Answer", value = answer, height=500)

