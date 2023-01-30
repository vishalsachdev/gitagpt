
# Adapted from notion-Qa to answer questions from a text file created from a PDF of the Gita . Deployed on Streamlit with code on main.py 


💪 Built with [LangChain](https://github.com/hwchase17/langchain)

# 🌲 Environment Setup

In order to set your environment up to run the code here, first install all requirements:

```shell
pip install -r requirements.txt
```

Then set your OpenAI API key (if you don't have one, get one [here](https://beta.openai.com/playground))

```shell
export OPENAI_API_KEY=....
```

# 📄 What is in here?
- Example data from Blendle 
- Python script to query Notion with a question
- Code to deploy on StreamLit
- Instructions for ingesting your own dataset

## 📊 Example Data
This repo uses the PDF at https://ocoy.org/wp-content/uploads/Bhagavad-Gita-For-Awakeninging-full-2-2021.pdf 

## 💬 Ask a question
In order to ask a question, run a command like:

```shell
python3 qa.py "What is the work from home policy"
```

You can switch out `What is the work from home policy` for any question of your liking!

This exposes a chat interface for interacting with a Notion database.
IMO, this is a more natural and convenient interface for getting information.

## 🚀 Code to deploy on StreamLit

The code to run the StreamLit app is in `main.py`. 
Note that when setting up your StreamLit app you should make sure to add `OPENAI_API_KEY` as a secret environment variable.

## 🧑 Instructions for ingesting your own dataset. Use the python script below to convert the PDF to text offline 
import PyPDF2

# Open the PDF file
pdf_file = open('enterfilename.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Loop through each page
text = ''
for page in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[page].extract_text()


# Close the PDF file
pdf_file.close()

# Write the text to a file
text_file = open('enterfilename.txt', 'w')
text_file.write(text)
text_file.close()



Run the following command to ingest the data.

```shell
python ingest.py
```

Boom! Now you're done, and you can ask it questions like:

```shell
python qa.py "What is the work from home policy"
```
