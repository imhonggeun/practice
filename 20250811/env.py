import os
from datasets import load_dataset

print(os.getenv("Hugging_Face"))

dataset = load_dataset("royboy0416/ko-alpaca")
print(dataset)