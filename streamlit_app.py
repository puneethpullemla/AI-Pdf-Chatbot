import streamlit as st
from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.vectorstore import create_vector_store
from utils.llm import get_llm
from langchain_classic.chains import RetrievalQA
from utils.embeddings import get_embeddings

st.title(" AI PDF Chatbot")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    documents = load_pdf("temp.pdf")

    docs = split_documents(documents)

    embeddings = get_embeddings()

    db = create_vector_store(docs, embeddings)

    llm = get_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever()
    )

    question = st.text_input("Ask a question about the PDF")

    if question:
        response = qa_chain.run(question)

        st.write("### 🤖 Answer")
        st.write(response)