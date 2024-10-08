import google.generativeai as genai
import streamlit as st

# Configure the API key
API_KEY = "AIzaSyD2O5nI0ToBrCkV2y95hifoP9lvP6g34k0"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# # Initialize model
model = genai.GenerativeModel('gemini-1.5-flash')


# Define a function to interact with the model
def getResponseFromModel(user_input):
    response = genai.generate_text(prompt=user_input)
    # Access the generated text from the response
    return response.candidates[0]['output']

# Chatbot title
st.title("Gemini Chatbot")

# Get user input using a text input box
user_input = st.text_input("Enter your Prompt here = ")

if st.button("Get Response"):
    if user_input:
        output = getResponseFromModel(user_input)
        st.write(f"Chatbot response:  {output}")
    else:
        st.write("Please enter a prompt here.")
















# user_input = input("Enter your prompt here: ")
# output = getResponseFromModel(user_input)
# print(output)

