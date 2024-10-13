from taipy.gui import Gui
from langchain_helper import get_qa_chain

# Define variables to hold user input and response
question = ""
response = ""

# Define a function to handle the creation of knowledge base
def create_knowledge_base(state):
    # You can add your logic for creating the knowledge base here
    pass

# Define a function to handle user input and chain response
def handle_question(state):
    if state.question:
        chain = get_qa_chain()
        state.response = chain(state.question)["result"]

# Define the layout of the Taipy app
layout = """
# Codebasic QA

<|layout|columns=1 1|gap=10px|
<|Create Knowledgebase|button|on_action=create_knowledge_base|>
|>

### Ask a Question:
<|{question}|input|label=question|on_change=handle_question|>

<|Response: {response}|>

"""

# Create the Gui object
gui = Gui(page=layout)

# Run the app
gui.run()
