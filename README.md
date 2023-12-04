# LLM Q and A

This is a Q and A system using the PaLM LLM. You will need the google API key to be able to access PaLM LLM. This project uses the FAISS vector database to perfom RAG (Retrieval Augmented Generation).

## How To Run
1. You can create virtual environment, if you create it, use the virtual environment
2. Run <code>pip install -r requirements.txt</code> to install the necessary packages
3. Run the <b>langchain_helper.py</b> file (<code>py langchain_helper.py</code> or the equivalent), this will create the vector database and save it in the path <b>VECTORDB_FILE_PATH</b> in the .env file
3. Run <code>streamlit run main.py</code> and wait until the streamlit UI is opened on your browser, you can see the streamlit local URL in the terminal

## Pictures
The LLM will try to use the information from the RAG to answer the question, here the LLM uses and combines information from 2 answers to answer the question.
![Combining 2 answers](https://github.com/davidkarelh/Basic-Q-and-A-LLM/blob/master/pictures/Biggest%20Palace%20in%20Germany.png)

The LLM can even infer information from the retrieved documents even though there is no specific question from that is the same as the inputted question.
![Inferring information](https://github.com/davidkarelh/Basic-Q-and-A-LLM/blob/master/pictures/Dilute%20Solution.png)

The LLM is specificcaly requested to say <b>I don't know</b> if the informations doesn't exist in the vector database.
![Information doesn't exist](https://github.com/davidkarelh/Basic-Q-and-A-LLM/blob/master/pictures/George%20Washington.png)