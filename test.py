import os
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete
from lightrag.llm import hf_model_complete, hf_embedding
from transformers import AutoModel, AutoTokenizer
from lightrag.utils import EmbeddingFunc
import torch
from openai import OpenAI
from huggingface_hub import login
import glob
login(token = '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')
#########
# Uncomment the below two lines if running in a jupyter notebook to handle the async nature of rag.insert()
# import nest_asyncio
# nest_asyncio.apply()
#########
torch.device("cuda" if torch.cuda.is_available() else "cpu")
WORKING_DIR = "./dickens"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)



#Initialize LightRAG with Hugging Face model
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=hf_model_complete,  # Use Hugging Face model for text generation
    llm_model_name='meta-llama/Meta-Llama-3-8B-Instruct',  # Model name from Hugging Face
    addon_params = {"example_number": 2,"language": "Vietnamese", "entity_types": ["tên ngành", "điểm", "tổ hợp môn", "thời gian đào tạo", "học phí", "mã ngành"], },
    # Use Hugging Face embedding function
    embedding_func=EmbeddingFunc(
        embedding_dim=384,
        max_token_size=4096,
        func=lambda texts: hf_embedding(
            texts,
            tokenizer=AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2"),
            embed_model=AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        )
    ),
)
# rag = LightRAG(
#     working_dir=WORKING_DIR,
#     llm_model_func=gpt_4o_mini_complete  # Use gpt_4o_mini_complete LLM model
#     # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
# )
folder_path = "dickens"
    # Lấy danh sách tất cả các file ảnh trong thư mụcq
paths = glob.glob(f"{folder_path}/*.txt*")  # Tìm mọi file (có thể lọc bằng *.png, *.jpg, ...)
for path in paths:
    with open(path, "r", encoding="utf-8") as f:
        rag.insert(f.read())

# Perform naive search
#print(
#    rag.query("Giới thiệu ngành công nghệ thông tin", param=QueryParam(mode="naive"))
#)
    #folder_path = "open_cv_data/thieuchieurong"

if __name__ == "__main__":
    while True:
        string = input("User: ")
        if string.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            break
        print("Bot: " + rag.query(string, param=QueryParam(mode="naive")))
