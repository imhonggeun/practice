#pip install datasets
from datasets import load_dataset
import os

data = load_dataset("json", data_files="pair.jsonl") #문서로되어있는건 다 가능
#print(data) #로컬에 있는걸 데이터 셋으로 한번 읽어보기
dir = "honggeun/test1"
token = os.getenv("Hugging_Face")
data.push_to_hub(dir, token=token)
