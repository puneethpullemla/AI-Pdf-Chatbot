def get_relevant_docs(vectorstore, query, k=3):

    docs = vectorstore.similarity_search(
        query,
        k=k
    )

    return docs