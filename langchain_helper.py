from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest",google_api_key='AIzaSyDb-cnvqx9gF5BVUikLbYqRcOCYFvYKH0Q',temperature=0.1)

#from langchain.document_loaders.csv_loader import CSVLoader
#loader=CSVLoader(file_path='codebasics_faqs.csv',source_column="prompt",encoding='ISO-8859-1')
#data=loader.load()

from langchain.embeddings import HuggingFaceBgeEmbeddings
embeddings=HuggingFaceBgeEmbeddings()
VectorDatabase_path="vsector_save"
#from langchain.vectorstores import FAISS
#VectorDatabase=FAISS.from_documents(data,embeddings)

def get_qa_chain():
    VectorDatabase=FAISS.load_local("vsector_save",embeddings)

    retriever=VectorDatabase.as_retriever(search_type="similarity")

    prompt_template=""" Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""
    PROMPT=PromptTemplate(template=prompt_template,input_variables=["context","question"])
    chain=RetrievalQA.from_chain_type(llm=llm,chain_type="stuff"
            ,retriever=retriever,input_key="query"
            ,return_source_documents=True)
    return chain

if __name__=="__main__":
    chain=get_qa_chain()

    print(chain("do you provide internship? do you have emi option"))
