from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
CSV_FILE_PATH = os.getenv("CSV_FILE_PATH")
VECTORDB_FILE_PATH = os.getenv("VECTORDB_FILE_PATH")

llm = GooglePalm(google_api_key=GOOGLE_API_KEY, temperature=0.2)

instructor_embeddings = HuggingFaceInstructEmbeddings()

def create_vector_db():
    # loader = CSVLoader(file_path = CSV_FILE_PATH, source_column="prompt", encoding='cp1252')
    loader = CSVLoader(file_path = CSV_FILE_PATH, source_column="Question", encoding='cp1252')
    docs = loader.load()
    vectordb = FAISS.from_documents(documents=docs, embedding=instructor_embeddings)
    vectordb.save_local(VECTORDB_FILE_PATH)

def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(VECTORDB_FILE_PATH, instructor_embeddings)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    # prompt_template = """Given the following context and a question, generate an answer based on this context only.
    # In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    # If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    # CONTEXT: {context}

    # QUESTION: {question}"""

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "Answer" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know.". Don't try to make up an answer. If there is nothing in the context, kindly state "I don't know.".

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain

if __name__ == "__main__":
    create_vector_db()