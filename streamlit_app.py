# Import necessary libraries
import streamlit as st
import openai

# Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
openai.api_key = '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'

# Streamlit app
def main():
    st.title("OpenAI Prompt App")

    # Input text box for the prompt
    user_input = st.text_input("Enter your prompt:")

    # Submit button
    if st.button("Submit"):
        # Send the prompt to the OpenAI API
        response = openai.Completion.create(engine="davinci", prompt=user_input, max_tokens=150)
        st.write(response.choices[0].text.strip())

if __name__ == "__main__":
    main()
