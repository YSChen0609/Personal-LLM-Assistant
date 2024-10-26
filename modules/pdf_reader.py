from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import GPT4All

class PDFReader:
    def __init__(self):
        self.llm = GPT4All(model="./ggml-gpt4all-j-v1.3-groovy.bin")
        self.embeddings = HuggingFaceEmbeddings()

    def read(self, pdf_path, question):
        pdf_reader = PdfReader(pdf_path)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        knowledge_base = FAISS.from_texts(chunks, self.embeddings)
        docs = knowledge_base.similarity_search(question)

        chain = load_qa_chain(self.llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=question)

        return response

