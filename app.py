from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import get_embeddings
from utils.vectorstore import create_vector_store
from utils.llm import get_llm
from utils.retriever import get_relevant_docs


def main():
    # Load and process document
    documents = load_pdf("data/sample.pdf")
    docs = split_documents(documents)

    embeddings = get_embeddings()
    vectorstore = create_vector_store(docs, embeddings)

    # Load LLM
    llm = get_llm()

    while True:
        query = input("\nAsk a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        # Retrieve relevant documents
        results = get_relevant_docs(vectorstore, query, k=5)

        # Combine context
        context = "\n\n".join([doc.page_content for doc in results])

        # Prompt
        prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question: {query}

Answer in 2 sentences.
"""

        # Generate response
        response = llm.invoke(prompt)

        # Convert to string safely
        answer = str(response).strip()

        # Handle empty output
        if not answer:
            answer = "No clear answer found in the document."

        print("\n🤖 Answer:\n")
        print(answer)
        print("\n" + "=" * 50)


if __name__ == "__main__":
    main()