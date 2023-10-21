# Import necessary libraries
import streamlit as st
import openai

# Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
openai.api_key = st.secrets["API"]

# Streamlit app
def main():
    st.title("OpenAI Prompt App")

    # Input text box for the prompt
    user_input = st.text_input("Enter your prompt:")

    # Submit button
    if st.button("Submit"):
        message=[{"role": "user", "content": user_input}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=750,
            temperature=1.2,
            messages = message)
        # Send the prompt to the OpenAI API
        #response = openai.ChatCompletion.create(engine="gpt-4", prompt=user_input, max_tokens=500)
        st.write(response)

if __name__ == "__main__":
    main()
