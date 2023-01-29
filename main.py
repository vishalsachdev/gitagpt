"""Python file to serve as the frontend"""
import streamlit as st
from streamlit_chat import message
import faiss
from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain
import pickle

# Load the LangChain.
index = faiss.read_index("docs.index")

with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

store.index = index
chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0), vectorstore=store)


# From here down is all the StreamLit UI.
# Set the page configuration for the Streamlit UI
st.set_page_config(page_title="Bhagvad Geeta Question Answer Bot", page_icon=":robot:")
# Add a header to the Streamlit UI with the title "Bhagvad Geeta Question Answer Bot"
st.header("Bhagvad Geeta Question Answer Bot")

# Check if "generated" is in the Streamlit session state
if "generated" not in st.session_state:
    # If not, initialize an empty list in the session state with key "generated"
    st.session_state["generated"] = []

# Check if "past" is in the Streamlit session state
if "past" not in st.session_state:
    # If not, initialize an empty list in the session state with key "past"
    st.session_state["past"] = []

# Define a function to get the user input text
def get_text():
    # Add a text input field to the Streamlit UI with label "You:"
    input_text = st.text_input("You: ", "Give me a summary of the bhagvad Geeta along with the main characters", key="input")
    # Return the user input text
    return input_text

# Call the function to get the user input
user_input = get_text()

# Check if the user input is not None
if user_input:
    # Call the chain function with the user input as the question
    result = chain({"question": user_input})
    # Format the answer and sources into a string
    output = f"Answer: {result['answer']}\nSources: {result['sources']}"

    # Append the user input to the "past" list in the session state
    st.session_state.past.append(user_input)
    # Append the formatted answer and sources to the "generated" list in the session state
    st.session_state.generated.append(output)

# Check if the "generated" list in the session state is not empty
if st.session_state["generated"]:
    # Loop through the list of generated outputs in reverse order
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        # Call the message function with the generated output and key value of i
        message(st.session_state["generated"][i], key=str(i)) 
        # Call the message function with the user input and key value of i + "_user", with is_user flag set to True
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")