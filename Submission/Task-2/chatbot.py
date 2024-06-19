import streamlit as st
from streamlit_chat import message
import google.generativeai as genai

st.title('My AI Assistant')

API_KEY = 'AIzaSyCNmlrWGWjhWUOLimzKZj9D7xFZ8361ZRE'  # Replace with your actual API key
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

def get_ai_response(prompt):
    result = model.generate_content(prompt)
    return result.text

def get_user_input():
    return st.text_input("Your message:", key='input')


if 'responses' not in st.session_state:
    st.session_state['responses'] = []
if 'inputs' not in st.session_state:
    st.session_state['inputs'] = []

user_input = get_user_input()

if user_input:
    ai_response = get_ai_response(user_input)

    st.session_state.inputs.append(user_input)
    st.session_state.responses.append(ai_response)

if st.session_state['responses']:
    for i in range(len(st.session_state['responses']) - 1, -1, -1):
        message(st.session_state['responses'][i], key=str(i))  
        message(st.session_state['inputs'][i], key="user"+str(i), is_user=True) 
