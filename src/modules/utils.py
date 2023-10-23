import os
import pandas as pd
import streamlit as st
import pdfplumber

from modules.chatbot import Chatbot
from modules.embedder import Embedder
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from modules.embedder import Embedder

class Utilities:

    @staticmethod
    def load_api_key():
        """
        Loads the OpenAI API key from the .env file or 
        from the user's input and returns it
        """
        if not hasattr(st.session_state, "api_key"):
            st.session_state.api_key = None
        #you can define your API key in .env directly
        if os.path.exists(".env") and os.environ.get("OPENAI_API_KEY") is not None:
            user_api_key = os.environ["OPENAI_API_KEY"]
            st.sidebar.success("API key loaded from .env", icon="🚀")
        else:
            if st.session_state.api_key is not None:
                user_api_key = st.session_state.api_key
                st.sidebar.success("API key loaded from previous input", icon="🚀")
            else:
                user_api_key = st.sidebar.text_input(
                    label="#### Your OpenAI API key 👇", placeholder="sk-...", type="password"
                )
                if user_api_key:
                    st.session_state.api_key = user_api_key

        return user_api_key

    
    @staticmethod
    def handle_upload(file_types, key):
        """
        Handles and display uploaded_file
        :param file_types: List of accepted file types, e.g., ["csv", "pdf", "txt"]
        """
        if key == "prod":
            label = "#### Production payroll data:"
        else:
            label = "#### Development payroll data:"

        uploaded_file = st.sidebar.file_uploader(
            label= label, 
            type=file_types, 
            # label_visibility="collapsed",
            key=key
            )
        if uploaded_file is not None:

            def show_csv_file(uploaded_file, key):
                data_type = ""
                if key == 'prod':
                    data_type = 'Production'
                else:
                    data_type = 'Development'
                file_container = st.expander(f"{data_type} Payroll:")
                uploaded_file.seek(0)
                shows = pd.read_csv(uploaded_file)
                file_container.write(shows)

            def show_pdf_file(uploaded_file):
                file_container = st.expander("Your PDF file :")
                with pdfplumber.open(uploaded_file) as pdf:
                    pdf_text = ""
                    for page in pdf.pages:
                        pdf_text += page.extract_text() + "\n\n"
                file_container.write(pdf_text)
            
            def show_txt_file(uploaded_file):
                file_container = st.expander("Your TXT file:")
                uploaded_file.seek(0)
                content = uploaded_file.read().decode("utf-8")
                file_container.write(content)
            
            def get_file_extension(uploaded_file):
                return os.path.splitext(uploaded_file)[1].lower()
            
            file_extension = get_file_extension(uploaded_file.name)

            # Show the contents of the file based on its extension
            if file_extension == ".csv" :
               show_csv_file(uploaded_file, key)
            if file_extension== ".pdf" : 
                show_pdf_file(uploaded_file)
            elif file_extension== ".txt" : 
                show_txt_file(uploaded_file)

        else:
            st.session_state["reset_chat"] = True

        #print(uploaded_file)
        return uploaded_file

    @staticmethod
    def setup_chatbot(model, temperature, df_dev, df_prod):
        """
        Sets up the chatbot with the uploaded file, model, and temperature
        """
        embeds = Embedder()

        with st.spinner("Processing..."):
            
            # Get the document embeddings for the uploaded file
            # # TODO: Scrape from URL using Langchain URL Loader
            # loader = TextLoader("./data/fairwork_award.txt")
            # fairwork_data = loader.load()
            
            # # Use OpenAI Embeddings
            # embeddings = OpenAIEmbeddings()

            # # Save embeddings into a FAISS vector store/db/index
            # if os.path.exists("embeddings/faiss_index"):
            #     vectors = FAISS.load_local("embeddings/faiss_index", embeddings)
            # else: 
            #     vectors = FAISS.from_documents(fairwork_data, embeddings)
            #     vectors.save_local("embeddings/faiss_index")

            data_path = "data/fairwork_award.txt"
            embedder = Embedder()

            vectors = embedder.getDocEmbeds(original_filename= data_path)

            # Create a Chatbot instance with the specified model and temperature
            chatbot = Chatbot(model, temperature, vectors, df_dev, df_prod)
        st.session_state["ready"] = True

        return chatbot


    
