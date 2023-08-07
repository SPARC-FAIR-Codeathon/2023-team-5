import argparse
import gradio as gr
import os
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.llms import HuggingFaceHub


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Query data from SPARC.")
    parser.add_argument('--hf_token', type=str, required=True,
                        help="HuggingFace account token.")
    parser.add_argument("--txt_folder", type=str,
                        default='./texts', help="Path to txt files.")
    args = parser.parse_args()

    txt_folder = args.txt_folder
    loaders = [TextLoader(os.path.join(txt_folder, fn)) for fn in
               os.listdir(txt_folder)]

    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-mpnet-base-v2')

    index = VectorstoreIndexCreator(
        embedding=embeddings,
        text_splitter=CharacterTextSplitter(chunk_size=2000,
                                            chunk_overlap=1)).from_loaders(
        loaders)

    llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct",
                         model_kwargs={"temperature": 0.05,
                                       "min_length": 2000,
                                       "max_length": 5000,
                                       "max_new_tokens": 100},
                         huggingfacehub_api_token=args.hf_token)

    qa = RetrievalQA.from_chain_type(llm=llm,
                                     chain_type="stuff",
                                     retriever=index.vectorstore.as_retriever())


    def ask(query):
        result = qa({"query": query})
        return result["result"]


    iface = gr.Interface(fn=ask,
                         inputs=gr.components.Textbox(lines=7,
                                                      label="Enter your text"),
                         outputs="text",
                         title="Ask your SPARC datasets anything!")

    iface.launch(share=True)