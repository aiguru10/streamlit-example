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
        messages=[{"role": "user", "content": "As an intelligent AI model, if you could be any fictional character, who would you choose and why?"}]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            max_tokens=100,
            temperature=1.2,
            messages = message)
        # Send the prompt to the OpenAI API
        #response = openai.ChatCompletion.create(engine="gpt-4", prompt=user_input, max_tokens=500)
        st.write(response.choices[0].text.strip())

if __name__ == "__main__":
    main()
