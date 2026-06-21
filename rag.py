from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter



def create_vectorstore(text):


    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200

    )


    chunks = splitter.split_text(text)



    embeddings = HuggingFaceEmbeddings(

        model_name=
        "sentence-transformers/all-MiniLM-L6-v2"

    )



    vectorstore = FAISS.from_texts(

        chunks,

        embeddings

    )


    return vectorstore





def search_pdf(vectorstore, query):


    docs = vectorstore.similarity_search(

        query,

        k=4

    )


    context=""


    for doc in docs:

        context += doc.page_content + "\n"



    return context